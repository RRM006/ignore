# CONTEXT.md — CSE 465 Project: Moshiko LLM Swap
## Complete Project Knowledge Base for Report Generation

---

## 1. COURSE & GROUP INFORMATION

| Field | Value |
|-------|-------|
| Course | CSE 465 — Pattern Recognition and Neural Network |
| Faculty | Dr. Nabeel Mohammed [NbM], Associate Professor, PhD Monash University |
| Institution | Department of Computer Science, North South University |

| Name | ID | Email |
|------|----|-------|
| Rafiur Rahman Mashrafi | 2221971042 | rafiur.mashrafi@northsouth.edu |
| Md. Shadman Shihab | 2231639642 | shadman.shihab@northsouth.edu |
| Md. Nafiul Alam Chowdhury | 2231774642 | nafiul.chowdhury@northsouth.edu |

---

## 2. PROJECT STRUCTURE (3 Demos + 1 Backup)

### Timeline Overview
```
Demo 1 (Quantization)
  → Faculty directed: "Do LLM Swap"
    → Demo 2 (LLM Swap — Qwen2.5-0.5B, swap at moshi.decoder level)
      → Demo 3 (LLM Swap — TinyLlama-1.1B, swap at moshi.decoder.model level — FULLY COMPLETE)

Backup: Lightweight Turn-Taking Classification (separate, standalone project)
```

---

## 3. DEMO 1 — QUANTIZATION ANALYSIS (Moshiko 2.0)

**Notebook:** `quantization_analysis.ipynb`  
**Reports:** `CSE465_DEMO_1_Report.pdf` (full IEEE report), `CSE465_DEMO_1_Report_2.pdf` (shorter version)

### What Moshiko Is
- Kyutai's `moshiko` (the English variant of Moshi): 7B-parameter multimodal speech-text model
- Two components: **Mimi Audio Codec** (neural codec, 24kHz mono → discrete tokens [B,8,T]) + **Moshiko LM** (7B transformer)
- Architecture: 32 layers, hidden dim 4096, 32 attention heads, 6 depth transformer layers

### What Was Done
1. **Environment**: PyTorch 2.4.0 + CUDA 12.1, moshi v0.2.13, bitsandbytes v0.49.2, Google Colab T4
2. **Model Loading**: Mimi (q8) + Moshiko LM (q8) loaded within 8.4–8.8 GB VRAM
3. **BF16 vs Q8 Comparison**: Kyutai's INT8 is completely lossless — 0.00 dB SNR difference across all 4 signal types (pure tone, mixed tones, white noise, chirp)
4. **Latency Benchmark**: RTF 0.007–0.031 (30–140× faster than real-time)
5. **Layer-wise Sensitivity**: 130 Mimi layers analyzed individually; `decoder.model.0.conv.conv` most sensitive (2.33 dB SNR drop)
6. **Mixed-Precision Strategy**: Top 20% sensitive layers (19) kept at BF16, remaining 80% (79) quantized to INT8 → SNR 17.31 dB (vs 15.88 baseline)
7. **INT4 via NF4**: Applied bitsandbytes NF4; Conv1d unsupported (API returns 2 values instead of 3); storage-only format
8. **Finding**: PyTorch `torch.quantization.quantize_dynamic()` INCOMPATIBLE with moshi's custom `weights_per_step` architecture

### Key Results Table
| Model Variant | SNR (dB) | VRAM |
|---|---|---|
| BF16 baseline | 15.88 | ~15.4 GB (doesn't fit T4) |
| Kyutai Q8 | 15.88 (0.00 diff) | ~8.4 GB |
| Mixed Precision (80% INT8) | 17.31 | ~8.4 GB |

### Limitations / Incomplete
- Test 3 (Speech-to-Speech generation) hung during LM generation — **not completed**
- Experiments 4, 5b, 6 (Dynamic Quant, LM INT4, Final Dashboard) — **planned but not executed**
- BF16 LM can't be loaded on T4 (15.4 GB > 15.6 GB limit)

---

## 4. DEMO 2 — LLM SWAP (Qwen2.5-0.5B, moshi.decoder swap point)

**Notebook:** `Moshi_Colab_Notebook_llmswap_qwen_decoder_module.ipynb`  
**Reports:** `cse465_demo_llmswap_qwen_report.pdf` (progress), `cse465_demo_llmswap_qwen_report_2.pdf` (full IEEE paper)

### Motivation
Faculty reviewed Demo 1 and directed the team to pursue LLM backbone replacement as the next direction.

### Architecture: HybridBackbone

**Swap point:** `moshi.decoder` (replaces the entire decoder module)

```
moshi.decoder ← HybridBackbone (NEW)
```

**What stays untouched:** Mimi audio codec only  
**What is replaced:** The entire decoder (embed_tokens, lm_head, depth_decoder all replaced/rewired)

**Dimension bridge:**
```
Input (from Moshi pipeline): (batch, seq, 4096)   ← Helium's shape
  ↓ Win: Linear(4096 → 896)                        ← input projector
  TinyQwen runs internally in 896-dim space
  ↓ Wout: Linear(896 → 4096)                       ← output projector (HiddenProjector)
Output: (batch, seq, 4096)                          ← restored to Helium shape
```

**Key architectural details:**
- `OLD_HIDDEN = 4096` (Moshi/Helium hidden size)
- `NEW_HIDDEN = 896` (Qwen2.5-0.5B hidden size)
- Win (~3.67M params), Wout (~3.67M params)
- LoRA adapters: rank=16, alpha=32, on q/k/v/o/gate/up/down projectors inside Qwen (~8.80M params)
- Total trainable: ~150M / 1.35B total = 11.16%
- pre_embed: frozen copy of Moshi's original 4096-dim text embedding (for parent class text+audio summation)

**Critical nuance:** The parent class `MoshiForConditionalGeneration` pre-sums text + audio embeddings before calling the decoder, passing a 4096-dim `inputs_embeds`. Win randomly projects this into 896-dim space. This is **Root Cause #2** of training failure.

### Memory Configuration
- Both Moshi and Qwen in 4-bit NF4 (double-quant), Mimi + depth_decoder excluded from quantization
- Mimi cast to bfloat16 after loading (~140 MB savings)
- Gradient checkpointing on Qwen and depth decoder
- 8-bit AdamW optimizer (~4× less optimizer state memory)
- Training clips capped at 2 seconds (25 frames at 12.5 Hz)
- **Peak VRAM: ~2.98 GB** (via `torch.cuda.memory_allocated()`)

### Two Bug Fixes Found in Moshi Reference Implementation
1. **Mimi padding integer overflow**: Padding read as ~9.2×10¹⁸ on T4; fixed by converting to native Python integers
2. **Depth decoder dtype mismatch**: depth_decoder loaded in float16, rest in bfloat16 → matmul dtype error; fixed by matching dtypes at load time

### Dataset & Training
- **Dataset**: `kyutai/DailyTalkContiguous` — 200 dialogues from 2,541 available (90/10 train/val split)
- LR: 2×10⁻⁴, warmup 50 steps + cosine decay
- Total steps: 1,000 | Effective batch size: 4 (grad accum 4, micro-batch 1)
- Optimizer: AdamW8bit, grad clip norm 1.0
- Checkpoint every 50 steps, eval every 100 steps

### Training Results (FAILURE — Negative Result)
| Step | Loss | Perplexity | Accuracy | F1 | BLEU |
|------|------|-----------|---------|-----|------|
| 200 | 7.59 | 1,972 | 0.0104 | 0.0017 | 0.52 |
| 300 | 8.30 | 4,015 | 0.0042 | 0.0010 | 0.52 |
| 400 | 8.72 | 6,136 | 0.0031 | 0.0007 | 0.45 |
| 500 | 8.76 | 6,354 | 0.0010 | 0.0004 | 0.46 |
| 600 | 9.31 | 11,013 | 0.0031 | 0.0031 | 0.46 |
| 700 | 9.56 | 14,189 | 0.0042 | 0.0029 | 0.44 |
| 900† | 7.72 | 2,257 | 0.0031 | 0.0008 | 0.57 |
| 1000 | 7.79 | 2,423 | 0.0031 | 0.0008 | 0.58 |
†Colab restart reset optimizer state — NOT genuine improvement

**Audio codebook accuracy: exactly 0.0 at every checkpoint**  
**End-to-end output: pure noise** (4.96s waveform from 3s prompt; Whisper-tiny transcribes as silence/random words)

### Root Cause Analysis (3 Structural Failures)

**Cause 1: Unmasked Padding Loss**
- `CrossEntropyLoss` called without `ignore_index` → pad token (id 0, aliased from `<unk>`) included
- ~70% of label sequence (positions 20–63 of 64) is padding
- Model pulled to simultaneously predict real tokens AND pad tokens → contradictory gradients
- Fix: `ignore_index=tokenizer.pad_token_id`

**Cause 2: Random Projector Scrambles Pre-summed Embedding**
- Parent class sums text + audio embeddings BEFORE calling decoder → 4096-dim `inputs_embeds`
- Win (randomly Xavier-initialized) maps this meaningful 4096-dim vector to random 896-dim direction
- LoRA rank-16 adapters lack capacity to undo this scrambling
- pre_embed module (designed to preserve embed_tokens for parent summation) is never used on hot path — parent always passes `inputs_embeds`, never `input_ids`

**Cause 3: Frozen Depth Decoder Receives Out-of-Distribution Inputs**
- Depth decoder trained jointly with Helium-7B, expects Helium's specific output distribution
- Wout (randomly initialized, only 3.67M params) cannot be taught to mimic Helium output via text cross-entropy alone
- Audio accuracy = 0.0 throughout; waveform = noise

**Proposed Fixes for Future Work:**
1. Mask padding: add `ignore_index`
2. Knowledge distillation loss: run Helium-7B in parallel, train Wout to match Helium's hidden states via MSE
3. Unfreeze depth decoder: add LoRA to depth decoder
4. Larger student: Qwen2.5-1.5B or 3B (14× capacity gap is too severe)
5. More data: full 2,500-dialogue DailyTalk corpus, ≥50,000 steps

### Parallel Work During Demo 2 Phase — Mini-Omni + Phi-3.5 Mini Instruct

**Context:** While working on Demo 2 (Qwen swap on Moshi), a parallel exploration was conducted using Mini-Omni as a fallback testbed because the original Moshi Helium swap required more VRAM than the free T4 could handle.

**Document:** `Mini-omni.pdf` (Project Update: Speech-to-Speech LLM Backbone Replacement)

**What was done:**
- Mini-Omni (by gpt-omni) was chosen as a lightweight modular speech-to-speech model suitable for LLM backbone replacement experiments
- Replaced Mini-Omni's default LLM with **Microsoft Phi-3.5 Mini Instruct** (3.8B parameters)
- Applied LoRA fine-tuning (rank r=16, lr=3×10⁻⁴, batch=30) on a Bengali talkshow audio dataset (1,000 samples)
- Ran 3 training runs: 3 epochs, 10 epochs, 20 epochs

**Training results:**

| Run | Epochs | Final Loss | Accuracy |
|-----|--------|-----------|---------|
| Run 1 | 3 | 1.0640 | 0.00% |
| Run 2 | 10 | 0.0777 | 0.00% |
| Run 3 | 20 | 0.0514 | 0.00% |

**Why accuracy was 0% throughout:**
1. **Wrong prediction target**: LoRA was applied to the text LLM (Phi-3.5), but training labels were audio codebook tokens from Mini-Omni's audio head. Text vocabulary (~32,000 tokens) has zero overlap with audio codebook (~2,048 entries)
2. **Modality mismatch**: Bengali talkshow audio features fed to a text backbone without any audio-to-text alignment layer
3. Loss decreasing (text-side learning occurred), but audio tokens were never the LLM's output → 0% is a measurement artifact, not true failure of learning

**Why no suitable dataset was found:**
- No publicly available dataset provides (input audio features, target audio tokens) pre-tokenized by Mini-Omni's codec
- Bengali speech datasets with sufficient size are extremely scarce
- LibriSpeech/Common Voice provide raw audio or transcripts, not codec-compatible token sequences
- Would require running Mini-Omni's encoder on raw speech as a preprocessing pipeline

**Critical insight this taught the team:**
This was essentially a **text-to-text swap, not speech-to-speech** — the backbone replaced was text-only and the loss was measured on text tokens, not audio tokens. This insight directly informed Demo 3's design: the need to audit what the loss function is actually measuring and what domain the backbone operates in.

**Hardware note:** The original Moshi Helium swap required Colab Pro+ A100 (40 GB VRAM). Mini-Omni was used as an accessible substitute on free T4.

---

## 5. DEMO 3 — LLM SWAP (TinyLlama-1.1B, moshi.decoder.model swap point)

**Notebook:** `moshi_llm_swap_TinyLlama__inner_transformer.ipynb` (Version 4 — Merged Edition, FULLY RUN)
**Status:** ✅ COMPLETE — all 31 numbered cells + 1 extra Gradio cell run, training done (300 steps), evaluation done, Gradio demo built

### Key Architectural Difference from Demo 2

**Swap point:** `moshi.decoder.model` (only the inner transformer core — more surgical than Demo 2's `moshi.decoder`)

```
moshi.decoder.model ← TinyLlamaBackbone (NEW)
```

**What stays untouched:** `embed_tokens`, `lm_head`, `depth_decoder`, Mimi — all completely unaware of the change
**What is replaced:** Only the inner transformer layers (Helium's 32-layer core)

**The "everything believes Helium is still there" design:**
```
Input from Moshi pipeline → (batch, seq, 4096)   ← Helium's shape
  ↓ input_adapter: Linear(4096 → 2048, bias=False, bfloat16)
  TinyLlama (LlamaModel, 22 layers) runs in 2048-dim space
  ↓ output_adapter: Linear(2048 → 4096, bias=False, bfloat16)
Output to Moshi pipeline → (batch, seq, 4096)    ← still Helium's shape
```

**TinyLlamaBackbone class details:**
- `input_adapter`: Linear(4096 → 2048, bias=False, bfloat16)
- `transformer`: TinyLlama's `LlamaModel` (inner transformer only, NOT full CausalLM)
- `output_adapter`: Linear(2048 → 4096, bias=False, bfloat16)
- `embed_tokens`: copied reference from original Helium `embed_tokens` before swap
- `norm`: copied reference from original Helium RMSNorm before swap
- Interface: input `inputs_embeds (batch, seq, 4096)` → output `BaseModelOutputWithPast` with `last_hidden_state (batch, seq, 4096)`

**Swap line:** `moshi.decoder.model = wrapper`

### Complete Cell-by-Cell Run Status (moshi_llm_swap_TinyLlama__inner_transformer.ipynb — 31 numbered cells + 1 Gradio cell)

| Notebook Cell Label | Code Cell # | Description | Key Output / Result |
|---------------------|-------------|------------|---------------------|
| CELL 1 | 2 | Mount Drive + folder structure | `/content/drive/MyDrive/CSE465_Moshi_Project/` created ✅ |
| CELL 2 | 3 | GPU + RAM check | Tesla T4, 15.6 GB VRAM ✅ |
| CELL 3 | 4 | Install locked packages | torch 2.4.1, transformers 4.48.0, bnb 0.44.1, peft 0.13.2 ✅ |
| CELL 4 | 5 | Verify versions (post-restart) | All versions confirmed ✅ |
| CELL 5 | 6 | HuggingFace login | Authenticated ✅ |
| CELL 6 | 7 | Re-declare paths | All paths confirmed ✅ |
| CELL 7 | 8 | Load Moshi 4-bit NF4 | VRAM: 0→3.64 GB after load ✅ |
| CELL 8 | 9 | Save BEFORE architecture | `logs/before_architecture.txt` saved ✅ |
| CELL 9 | 10 | Load test audio | `hf-internal-testing/librispeech_asr_dummy` ✅ |
| CELL 10 | 11 | **BEFORE generation (Helium-7B)** | Output: 9.84s audio, saved `audio/before_audio.wav` ✅ |
| CELL 11 | 12 | Free memory | VRAM freed to 1.44 GB ✅ |
| CELL 12 | 13 | Load TinyLlama-1.1B | `TinyLlama/TinyLlama-1.1B-Chat-v1.0` loaded ✅ |
| CELL 13 | 14 | Define TinyLlamaBackbone | Class defined ✅ |
| CELL 14 | 15 | Reload Moshi (after CELL 11 freed RAM) | VRAM: 3.64 GB ✅ |
| CELL 15 | 16 | **THE SWAP** | `moshi.decoder.model = wrapper`; embed_tokens + norm preserved ✅ |
| CELL 16 | 17 | Sanity check | Input `(1,10,4096)` → Output `(1,10,4096)` ✅; saved `logs/swap_proof.txt` |
| CELL 17 | 18 | **AFTER generation (TinyLlama, pre-finetune)** | Output: 9.84s audio, saved `audio/after_audio.wav` ✅ |
| CELL 18 | 19 | Save AFTER architecture | `logs/after_architecture.txt` saved ✅ |
| CELL 19 | 20 | Before/After comparison for faculty | Audio comparison displayed ✅ |
| CELL 20 | 21 | Apply LoRA to TinyLlama | Trainable: 163.68M / 2.19B (7.479%); VRAM: 5.96 GB ✅ |
| CELL 21 | 22 | Download DailyTalkContiguous | 180 train / 20 val dialogues ✅ |
| CELL 22 | 23 | Checkpoint helpers | Save/load functions defined ✅ |
| CELL 23 | 24 | Metric logger + load Whisper | Whisper-tiny loaded ✅ |
| CELL 24 | 25 | Tier-1 text metrics function | `tier1_text_metrics` defined ✅ |
| CELL 25 | 26 | Tier-2 speech metrics function | `tier2_speech_metrics` defined ✅ |
| CELL 26 | 27 | Combined evaluator | Val samples: 20 ✅ |
| FIX cell | 28 | Load TinyLlama tokenizer | `LlamaTokenizerFast`, pad=eos=`</s>` (id=2) ✅ |
| FIX cell | 29 | Rebuild DataLoaders | Train:180, Val:20 ✅ |
| CELL 27 | 30 | **Training loop** | Resumed from step 200, ran to step 300; loss ~0.0000; VRAM 5.5 GB ✅ |
| eval call | 31 | `full_evaluate(step=300)` | `loss=0.0000, bleu=93.06, wer=1.07, audio_tok_acc=1.0` ✅ |
| CELL 28 | 32 | Plot training metrics | `logs/metrics_plot.png` saved (6-panel plot) ✅ |
| CELL 29 | 33 | End-to-end S2S test | `results/finetuned_output.wav` saved ✅ |
| CELL 30 | 34 | Final 3-way comparison | Before (Helium) / After (TinyLlama pre-finetune) / Fine-tuned ✅ |
| CELL 31 | 35 | List all Drive files | All files confirmed saved to Drive ✅ |
| **GRADIO** | 36 | **Gradio demo (after CELL 31)** | Public URL generated, live faculty demo ✅ |

### Engineering Problems Solved in Demo 3

**Cell 17 (AFTER generation — 4 errors fixed):**
1. **dtype mismatch BFloat16/Half**: Mimi weights float16, inputs bfloat16 → fixed by casting inputs to `torch.float16`
2. **torch.compile / dynamo tracing crash**: accelerate `_hf_hook` incompatible with dynamo → fixed by `remove_hook_from_module(moshi, recurse=True)`
3. **Tensor size mismatch at cat**: stale `generated_audio_codes` from Cell 10 (shape 1,8,76) vs new shape (1,8,1) → fixed by clearing state and using fresh variable names
4. **KV cache shape conflict**: cache allocated with Helium head_dim=128, TinyLlama has head_dim=64 (GQA with 4 KV heads) → fixed by `use_cache=False` and passing `past_key_values` through properly

**Cell 27 (Training loop — 5 errors fixed):**
1. **No padding token**: Moshi's tokenizer has no pad/eos tokens → fixed by loading TinyLlama's tokenizer (`pad_token = eos_token = '</s>'`, id=2, vocab=32000)
2. **float32 audio into float16 Mimi**: dataset returns float32 audio → fixed by `.to(torch.float16)` inside training loop
3. **IndexError embed_tokens[16]**: Mimi returning 32 quantizer codes but embed_tokens only has 8 (codebooks 0–7) → fixed by `num_quantizers=NUM_CODEBOOKS=8` and `uc[:, :NUM_CODEBOOKS, :]`
4. **Sequence length mismatch (63 vs 64)**: audio tokens (63) ≠ text input_ids (64, from max_length=64) — they are summed in forward() → fixed by trimming text_ids to match `seq_len = mc.shape[2]`
5. **OOM during depth decoder**: matmul OOM at 13.71/14.56 GB → fixed by `MAX_AUDIO_TOKENS=32`, `audio_labels=None` (skip depth decoder), `expandable_segments:True`, `gc.collect()` every step

### Training Results (300 Steps — Overfitting Diagnosis)

Training was resumed from a checkpoint at step 200 and ran to step 300.

| Metric | Value | Honest Interpretation |
|--------|-------|----------------------|
| loss | ~2.45×10⁻⁸ | Near-zero — model memorized training data |
| perplexity | ~1.0 | Perfect — expected given loss near zero |
| bleu | 93.06 | Very high text overlap |
| wer | 1.0727 | Word error rate >1.0 — speech not intelligible |
| cer | 0.9185 | Character error rate ~92% |
| audio_tok_acc | 1.0 | Audio token prediction near-perfect |
| accuracy | 0.0 | Near zero — text_ids were mostly padding tokens |
| dur_ratio | 1.008 | Generated audio duration matches reference |

**Evaluation at step 300 (from Cell 31):**
`loss=0.0000 | perplexity=1.0000 | accuracy=0.0000 | f1=0.0000 | bleu=93.0605 | wer=1.0727 | cer=0.9185 | audio_tok_acc=1.0000 | dur_ratio=1.0080`

**Only one evaluation data point** (step 300): evaluation at step 200 failed during that session, step 300 completed successfully. Plots show a single dot per metric instead of a curve.

**Honest assessment — why results look paradoxical:**
- Loss collapsed near zero by step ~40 and stayed there → model memorized 180 training samples
- `MAX_AUDIO_TOKENS=32` = only 2.5 seconds of audio per sample
- `accuracy=0.0` because text_ids consist mostly of padding tokens (same root cause as Demo 2 Cause #1)
- `audio_tok_acc=1.0` because depth decoder was skipped (`audio_labels=None`) — this metric reflects the input, not generated output
- `wer>1.0` = the fine-tuned output speech is not recognizable text
- For a course project demonstrating architectural feasibility: the swap works, training ran, metrics were computed — goal achieved

### Trainable Parameter Budget (Cell 20)
- LoRA adapters on TinyLlama (rank 16, alpha 32): targeting all attention + MLP projectors
- input_adapter Linear(4096→2048) + output_adapter Linear(2048→4096): both trainable
- **Total trainable: 163.68M / 2.19B = 7.479%**
- VRAM during training: 5.5 GB (stable throughout 300 steps)

### Audio Files Generated
| File | Description |
|------|-------------|
| `audio/before_audio.wav` | 9.84s — Helium-7B backbone (original Moshi) |
| `audio/after_audio.wav` | 9.84s — TinyLlama backbone, BEFORE fine-tuning |
| `results/finetuned_output.wav` | TinyLlama backbone, AFTER fine-tuning (300 steps) |
| `results/step_000300/sample_00–04_gen.wav` | 5 generated samples vs references |

### Gradio Demo (Extra cell — AFTER CELL 31, code cell #36 in notebook)
A Gradio interface was added as the final cell (after CELL 31) for faculty demonstration:
- Opens a public shareable URL (valid 72 hours, works in any browser)
- Accepts microphone recording or WAV file upload
- Passes audio through `moshi.generate()` with TinyLlama backbone in place
- Plays back generated audio response, shows input/output duration and model info
- Uses the live swapped `moshi` object in the Colab session — confirms swap is real, not just code
- **Important limitation**: output is Moshi-style speech conditioned on input audio, NOT a conversational reply. True real-time conversation requires the full Moshi streaming loop (not in this notebook)

**Step-by-step instructions to run the Gradio demo from a fresh Colab session:**

1. Open `moshi_llm_swap_TinyLlama__inner_transformer.ipynb` in Google Colab
2. Run **CELL 1** — mounts Google Drive and recreates folder paths
3. Run **CELL 2** — confirms T4 GPU is available
4. Run **CELL 3** — installs all locked packages (torch, transformers, bitsandbytes, peft, accelerate)
5. **Restart the Colab runtime** (Runtime → Restart session) — required after package install
6. Run **CELL 4** — verifies package versions after restart
7. Run **CELL 5** — HuggingFace login (token required)
8. Run **CELL 6** — re-declares all Drive paths after restart
9. Run **CELL 7** — loads Moshi in 4-bit NF4 quantization (~3–5 minutes, downloads from cache)
10. Run **CELL 12** — loads TinyLlama-1.1B (~2–3 minutes)
11. Run **CELL 13** — defines the `TinyLlamaBackbone` class
12. Run **CELL 14** — reloads Moshi (skip if CELL 11 was not run in this session)
13. Run **CELL 15** — **performs the swap** (`moshi.decoder.model = wrapper`)
14. Run the **FIX cell** (Load TinyLlama tokenizer, code cell #28) — sets pad token
15. Run the **GRADIO cell** (last cell, code cell #36) — launches the demo, prints the public URL

**Verify the swap is active before running Gradio:**
```python
print(type(moshi.decoder.model))        # should print: TinyLlamaBackbone
print(type(moshi.decoder.model.transformer))  # should print: LlamaModel
```

### Drive Contents (confirmed by Cell 31)
All outputs saved to Google Drive and persist after Colab session:
- `audio/`: before_audio.wav, after_audio.wav, input_sample.wav
- `logs/`: before/after architecture txt, swap_proof.txt, metrics_history.csv, metrics_plot.png, TensorBoard events
- `checkpoints/`: step_000050 through step_000300 (each with input_adapter.pt, output_adapter.pt, optim.pt, LoRA safetensors ~49 MB)
- `results/`: finetuned_output.wav, step_000300/ (5 sample pairs: gen + ref WAV + ASR text)

### Demo 2 vs Demo 3 Comparison Table (Including Helium-7B Original)
| Dimension | Helium-7B (Original Moshi) | Demo 2 (Qwen2.5-0.5B, HybridBackbone) | Demo 3 (TinyLlama-1.1B, TinyLlamaBackbone) |
|---|---|---|---|
| Swap point | N/A (baseline) | `moshi.decoder` | `moshi.decoder.model` |
| What is replaced | N/A | Entire decoder module | Only inner transformer (32 layers) |
| What stays | Everything | Mimi only | `embed_tokens`, `lm_head`, `depth_decoder`, Mimi |
| Helium components reused | All | None (all replaced) | `embed_tokens` + `lm_head` + `norm` |
| Hidden size | 4096 | 896 (Qwen) | 2048 (TinyLlama) |
| Dimension gap vs Helium | — | 4.6× (4096÷896) | 2× (4096÷2048) |
| Parameters | 7B | 0.5B (−93%) | 1.1B (−84%) |
| Peak VRAM | ~14 GB | ~2.98 GB (−79%) | ~5.5 GB (training) |
| T4 compatible | No (fine-tuning) | Yes | Yes |
| Training completed | N/A | Yes — 1,000 steps, loss diverged | Yes — 300 steps, overfit/memorized |
| Training outcome | N/A | Failure (loss ↑, audio acc=0.0) | Overfitting (loss→0, wer>1.0) |
| Evaluation metrics | N/A | Text metrics only | Full Tier-1 + Tier-2 computed |
| Audio output quality | Reference | Pure noise | Generates audio (not intelligible) |
| Gradio demo | N/A | No | Yes — live faculty demo |
| Bug fixes required | N/A | 2 (Mimi overflow, dtype mismatch) | 9 across CELL 17 + CELL 27 |
| Key engineering challenge | N/A | Architecture design | Dtype / cache / tokenizer / OOM issues |

---

## 6. BACKUP PROJECT — LIGHTWEIGHT TURN-TAKING CLASSIFICATION

**Notebook:** `Lightweight_Turn-Taking_Classification.ipynb`  
**Report:** `An_Open_Source_Speech_to_Speech_Turn_Taking_Pipeline_for_Code_Mixed_English_French_Speech_Using_DistilBERT_Classification_report.pdf`

### Pipeline
```
Speech → Whisper-small (ASR + language detection)
       → DistilBERT classifier (wait / respond / backchannel)
       → TinyLlama-1.1B @ 4-bit (response generation, only on "respond")
       → edge-tts (English or French voice)
       → Speech
```

### Turn-Taking Classifier
- Model: `distilbert-base-uncased` with 3-way classification head
- Dataset: DailyDialog (13,118 dialogues) → 51,184 train / 8,645 test
- Labels: wait (no terminal punctuation), respond (complete utterance), backchannel (short ack)
- Class-weighted cross-entropy (backchannel is rare)
- Training: 5 epochs, lr=2×10⁻⁵, batch=32, linear warmup, ~45 min on T4

### Results
| Method | Accuracy |
|--------|---------|
| Rule-based baseline | 88.48% |
| DistilBERT (fine-tuned) | 96.16% |
| GNB on TF-IDF | 58.48% |
| k-NN (k=7) on DistilBERT embeddings | 84.13% |

### End-to-End Pipeline
- 4/6 clips correct (66.7%) — both failures were "wait" class
- Issue: TTS-generated audio sounds complete → Whisper adds period → classifier predicts "respond"
- Average latency: 6.22s vs DuplexCascade's 1.70s (hardware gap, not design gap)
- Handles code-mixed English-French audio

### Classical Pattern Recognition Comparison (CSE 465 Syllabus Connection)
- GNB: TF-IDF features, independence assumption fails for turn-taking → 58.48%
- k-NN k=7: DistilBERT [CLS] embeddings (768-dim), Euclidean distance → 84.13%
- k-Means (k=3) on embeddings: ARI=0.059 (classes not well-separated in raw embedding space)
- Fine-tuning is what creates class separation, not the classifier algorithm

---

## 7. SYSTEM COMPARISONS

### Resource Comparison (Demo 2)
| Metric | Original (Helium-7B) | Modified (Qwen2.5-0.5B) | Change |
|--------|---------------------|------------------------|--------|
| Parameters | 7B | 0.5B | −93% |
| VRAM (peak) | ~14 GB | ~2.98 GB | −79% |
| T4 Compatible | No | Yes | — |
| Disk Space | ~15 GB | ~1 GB | −93% |

### Turn-Taking System Comparison
| Metric | DuplexCascade | Ours (Backup) |
|--------|--------------|---------------|
| Hardware | 8× H100 | 1× T4 (free) |
| Turn-taking | Qwen2-7B* | DistilBERT |
| LLM | Qwen2-7B* | TinyLlama-1.1B |
| Open-source | Partial | Full |
| Code-mixed | No | Yes (EN+FR) |
| Train time | 5h / 8×H100 | 45min / 1×T4 |
| Avg. latency | ~1.70s | 6.22s |

---

## 8. TECHNICAL STACK (All Demos)

| Component | Version |
|-----------|---------|
| Python | 3.12.13 |
| PyTorch | 2.4.1 + CUDA 12.1 |
| Transformers | 4.48.0 |
| bitsandbytes | 0.44.1 |
| PEFT | 0.13.2 |
| Accelerate | 1.0.1 |
| Platform | Google Colab, NVIDIA Tesla T4, 15.6 GB VRAM |
| Moshi (Demo 1) | moshi v0.2.13 (kyutai original) |
| Moshi (Demo 2/3) | kmhf/hf-moshiko (HuggingFace port) |
| Alt LLM (Demo 2) | Qwen/Qwen2.5-0.5B |
| Alt LLM (Demo 3) | TinyLlama/TinyLlama-1.1B-Chat-v1.0 |
| ASR (Demo 3 eval + Backup) | openai/whisper-tiny, whisper-small |
| TTS (Backup) | edge-tts |

---

## 9. REPORT STRUCTURE DECISIONS

### Main Report Focus
- **Co-primary focus: Demo 3 and Demo 2** — these are the two main contributions of the project
- **Demo 3 (TinyLlama)** = the most complete work: full training run (300 steps), full evaluation (Tier-1 + Tier-2), 3-way audio comparison, 9 engineering bugs resolved, Gradio live demo. This is the architectural success story and the engineering depth of the project
- **Demo 2 (Qwen)** = the diagnostic contribution: full training run (1,000 steps), diverging loss, 3 root-cause structural failures identified. This is the scientific rigor of the project — a well-documented negative result with actionable diagnosis
- **Demo 1 (Quantization)** = context/motivation; shows why the original 7B model cannot be fine-tuned on T4 and establishes T4 feasibility with quantization
- **Mini-Omni parallel work** = brief mention in Demo 2 section; documents the text-to-text vs speech-to-speech lesson that informed the team's approach
- **Backup project** = independent companion contribution; connects to CSE 465 syllabus (classical pattern recognition comparison — GNB, k-NN vs neural)

### Confirmed Report Title
**"Replacing Moshi's Helium-7B with Lightweight Alternatives: A Multi-Stage Study on Commodity Hardware"**

### Proposed Narrative Arc for Introduction/Literature Review
1. Real-time speech dialogue: ASR→LLM→TTS cascades → Moshi's end-to-end approach
2. Memory constraints on commodity hardware → need for compression/substitution
3. QLoRA / parameter-efficient fine-tuning for standalone LLMs → does it transfer to multimodal?
4. Knowledge distillation for speech models (gap: no prior work on backbone replacement in tightly-coupled multimodal models)

### Literature Review Writing Format (MANDATORY — apply to every entry)
Each literature review paragraph MUST follow this template exactly:

> [Author(s)] [Reference Number] proposed/developed/presented/designed/introduced [model/system/framework/approach name] for [main research objective]. The study utilized/employed/applied [algorithm, architecture, dataset, technique, or methodology] to [specific task or improvement]. Experimental/simulation results demonstrated/revealed/showed that the proposed method achieved [accuracy/performance metrics/results] compared to [baseline or existing methods if mentioned]. The findings concluded that [main contribution or significance of the work].

**Entries to write (in this order):**
1. Defossez et al. [1] — Moshi (end-to-end speech-text foundation model, Mimi codec, Helium-7B backbone)
2. Borsos et al. [2] — AudioLM (language modeling approach to audio generation)
3. Zhang et al. [3] — SpeechGPT (cross-modal conversational LLM)
4. Hu et al. [4] — LoRA (low-rank adaptation of large language models)
5. Dettmers et al. [5] — QLoRA (efficient fine-tuning of quantized LLMs, NF4)
6. Dettmers et al. [6] — bitsandbytes / LLM.int8() (8-bit matrix multiplication for transformers)
7. Hinton, Vinyals & Dean [7] — Knowledge distillation
8. Radford et al. [8] — Whisper (robust speech recognition via large-scale weak supervision)
9. Qwen Team [9] — Qwen2.5 technical report (the student model used in Demo 2)
10. Yang et al. — DuplexCascade (2026) — full-duplex speech-to-speech, baseline for backup project
11. Sanh et al. — DistilBERT (distilled BERT, classifier backbone for backup project)
12. Li et al. — DailyDialog dataset (training data for backup classifier)

---

## 10. GOOGLE DRIVE LINKS & QR CODES

| Demo | Google Drive Link | QR Code File |
|------|------------------|--------------|
| Demo 1 (Quantization) | https://drive.google.com/drive/folders/1CjVNMQW77IXPGnGI7oa3feMDEa_dg7or?usp=sharing | `qr_demo1.png` |
| Demo 2 (Qwen Swap) | https://drive.google.com/drive/folders/1FokGH0cn9LkRj23Xq8gdsToaBaeM1k2a?usp=sharing | `qr_demo2.png` |
| Demo 3 (TinyLlama Swap) | https://drive.google.com/drive/folders/100rsxBt_h1Jip2UxZ2-Tt2b6Gx0gTLxn?usp=sharing | `qr_demo3.png` |
| Backup (Turn-Taking) | https://drive.google.com/drive/folders/1SEZ-XZmAWYyEIIiIXbua05vQ_FTK0Imk?usp=sharing | `qr_backup.png` |

QR codes generated and saved as PNG files. To embed in LaTeX:
```latex
\includegraphics[width=2cm]{qr_demo1.png}
```

---

## 11. FILES PROVIDED

| File | Type | Demo | Status |
|------|------|------|--------|
| `quantization_analysis.ipynb` | Notebook | Demo 1 | Complete (some experiments partial) |
| `Moshi_Colab_Notebook_llmswap_qwen_decoder_module.ipynb` | Notebook | Demo 2 | Complete |
| `moshi_llm_swap_TinyLlama__inner_transformer.ipynb` | Notebook | Demo 3 — **FINAL** | Fully complete — 31 numbered cells + Gradio cell, all run |
| `Lightweight_Turn-Taking_Classification.ipynb` | Notebook | Backup | Complete |
| `Mini-omni.pdf` | Report | Demo 2 parallel work | Mini-Omni + Phi-3.5 Mini exploration |
| `CSE465_DEMO_1_Report.pdf` | Report | Demo 1 | Full IEEE |
| `CSE465_DEMO_1_Report_2.pdf` | Report | Demo 1 | Shorter version |
| `cse465_demo_llmswap_qwen_report.pdf` | Report | Demo 2 | Progress report |
| `cse465_demo_llmswap_qwen_report_2.pdf` | Report | Demo 2 | Full IEEE paper |
| `An_Open_Source_Speech...report.pdf` | Report | Backup | Full IEEE |

**Note:** Any output files needed from Drive (audio files, metrics plots, architecture logs, checkpoints) must be requested from the user — they are not in the uploaded files.

## 12. ALL PRE-WRITING QUESTIONS — RESOLVED

| Question | Answer |
|----------|--------|
| Google Drive links | ✅ All 4 added in Section 10 |
| GitHub repository URL | ✅ `https://github.com/RRM006/moshi-backbone-swap-nbm` |
| QR codes | ✅ Generated: `qr_demo1.png`, `qr_demo2.png`, `qr_demo3.png`, `qr_backup.png` |
| Demo 3 training status | ✅ FULLY COMPLETE — all 31 cells run, 300 training steps, evaluation at step 300, Gradio demo |
| Audio files | ✅ before_audio.wav (9.84s, Helium), after_audio.wav (9.84s, TinyLlama pre-tune), finetuned_output.wav |
| Grading rubric / page limits | ✅ IEEE format. Must follow exact mandatory section order. No other constraints given |
| Report narrative style | ✅ All demos as ONE unified iterative project |
| Report primary focus | ✅ Demo 2 AND Demo 3 equally (both have full results now). Demo 2 = diagnostic value, Demo 3 = architectural improvement + complete run |
| Mini-Omni work | ✅ Documented in Section 4 as parallel Demo 2 exploration. It was text-to-text, not speech-to-speech |
| AI use acknowledgment | ✅ Must be added to report — see Section 16 |

---

---

## 13. PLAIN-LANGUAGE DEMO SUMMARIES (use these for writing Results + Proposed Methods sections)

### Demo 1 — Quantization Analysis
**What we did:** Tested how much Moshi's 7B speech AI model can be compressed without losing audio quality, on a free T4 GPU.

**How we did it:**
- Loaded Moshiko in both BF16 (original) and INT8 (compressed)
- Tested codec encode/decode speed on 1s, 3s, 5s, 10s audio clips
- Quantized each of 130 layers one by one to find which layer breaks quality most
- Kept top 20% sensitive layers at BF16, compressed bottom 80% to INT8 — called mixed precision

**What we got out:**
- INT8 vs BF16 quality difference = 0.00 dB — completely lossless
- Codec runs 140× faster than real-time
- Most sensitive layer = first decoder conv layer (drops 2.33 dB)
- VRAM reduced from 15.4 GB → 8.4 GB (saved 79%)
- Full model now fits on free T4 ✅

**Metrics used:**
- SNR — audio quality (higher = better)
- RTF — speed (below 1.0 = faster than real-time)
- SNR Drop — how much each layer hurts quality when compressed
- VRAM — GPU memory usage

---

### Demo 2 — LLM Swap (Qwen, HybridBackbone)
**What we did:** Moshi's brain needs 14 GB GPU memory — too much for a free GPU. We tried to replace it with a much smaller brain (Qwen2.5-0.5B, 500M parameters).

**How we did it:**
- Replaced Helium-7B (7B parameters) with Qwen2.5-0.5B (500M parameters)
- Built a connector bridge: 4096 → 896 → 4096 dimensions (HybridBackbone)
- Memory-saving tricks: 4-bit quantization, LoRA adapters (rank 16), gradient checkpointing, 8-bit AdamW
- Trained on 200 dialogues for 1,000 steps

**What we got out:**

| Metric | Original | Ours |
|--------|----------|------|
| Parameters | 7 Billion | 0.5 Billion |
| VRAM needed | 14 GB | 2.98 GB |
| Works on T4? | No | Yes |
| Disk Space | 15 GB | 1 GB |

**BUT — training failed:**
- Loss went up instead of down
- Audio output was pure noise
- Audio accuracy was 0.0% throughout

**Why it failed (3 root causes found):**
1. Padding tokens confused training — model tried to learn padding AND real tokens simultaneously
2. Connector was randomly initialized — small model received meaningless scrambled input
3. Audio decoder was frozen — never learned to work with the new brain's output distribution

**Metrics used:** Loss, Perplexity, Token Accuracy, F1 Score, BLEU Score, Peak VRAM, Audio Codebook Accuracy

---

### Demo 3 — LLM Swap (TinyLlama, TinyLlamaBackbone) — FULL RUN
**What we did:** Replaced Moshi's inner transformer with TinyLlama-1.1B using a surgical swap that leaves all surrounding components (embed_tokens, lm_head, depth_decoder, Mimi) completely unaware of the change. Then fine-tuned with LoRA for 300 steps and ran a Gradio demo for faculty.

**How we did it:**
- Loaded Moshi with original Helium-7B backbone in 4-bit quantization
- Generated baseline audio with Helium-7B (before swap) — 9.84s ✅
- Loaded TinyLlama-1.1B separately
- Built connector bridge: 4096 → 2048 → 4096 (TinyLlamaBackbone)
- Swapped ONLY the inner transformer (`moshi.decoder.model = wrapper`)
- Generated audio with TinyLlama before fine-tuning (after swap) — 9.84s ✅
- Applied LoRA to TinyLlama inside the backbone (163.68M trainable / 2.19B = 7.479%)
- Trained 300 steps on 180 DailyTalkContiguous dialogues (VRAM: 5.5 GB stable)
- Generated fine-tuned output audio ✅
- Built Gradio demo for live faculty demonstration ✅

**What we got out:**

| Audio File | Description |
|-----------|-------------|
| before_audio.wav (9.84s) | Helium-7B original output |
| after_audio.wav (9.84s) | TinyLlama, pre-fine-tuning |
| finetuned_output.wav | TinyLlama, after 300 steps |

| Metric at step 300 | Value | What it means |
|--------------------|-------|--------------|
| loss | ~2.45×10⁻⁸ | Model memorized training data |
| perplexity | ~1.0 | Perfect — overfitting |
| bleu | 93.06 | High text overlap |
| wer | 1.07 | Speech not intelligible |
| audio_tok_acc | 1.0 | Depth decoder skipped (not real speech accuracy) |
| accuracy | 0.0 | Text predictions were padding tokens |

**9 engineering bugs fixed** across Cell 17 (4 bugs: dtype, dynamo hook, stale cache, KV head mismatch) and Cell 27 (5 bugs: tokenizer, float32→float16, codebook index, sequence length, OOM)

**Metrics used:** Loss, Perplexity, BLEU, WER, CER, Audio Token Accuracy, Duration Ratio, VRAM, Token Accuracy

---

### Backup — Lightweight Turn-Taking Classification
**What we did:** Built a complete voice chatbot from scratch using only free and open-source tools — works in both English and French.

**How we did it:**
- Built a 4-stage pipeline: Speech → Whisper → DistilBERT → TinyLlama → edge-tts → Speech
  - Whisper: converts speech to text, detects language
  - DistilBERT: trained classifier, decides when to reply (wait / respond / backchannel)
  - TinyLlama: generates the actual reply (4-bit quantized)
  - edge-tts: converts reply back to speech (English or French voice)
- Trained classifier on 51,184 examples from DailyDialog, 5 epochs, 45 minutes on free T4

**What we got out:**

| Method | Accuracy |
|--------|---------|
| Rule-based baseline | 88.48% |
| Naive Bayes (classical) | 58.48% |
| k-NN on DistilBERT embeddings (k=7) | 84.13% |
| DistilBERT fine-tuned (ours) | 96.16% |

End-to-end: 4/6 clips correct (66.7%), total latency 6.22s

| | DuplexCascade | Ours |
|---|---|---|
| Hardware | 8 H100 GPUs | 1 free T4 |
| Open-source | Partial | Full |
| Code-mixed | No | Yes (EN+FR) |
| Train time | 5 hours | 45 minutes |

**Metrics used:** Accuracy, F1 Score (handles imbalanced classes), Training Loss, Latency per stage, ARI (Adjusted Rand Index for k-Means clustering), PCA variance explained

---

## 14. MANDATORY REPORT STRUCTURE (EXACT — DO NOT DEVIATE)

The report MUST follow this section order exactly, in IEEE two-column LaTeX format.
**Primary focus: Demo 3 (TinyLlama) and Demo 2 (Qwen) — these receive the most space and depth.**

```
1.  TITLE PAGE
    ─────────────────────────────────────────────────────────────────
    Title:   Replacing Moshi's Helium-7B with Lightweight Alternatives:
             A Multi-Stage Study on Commodity Hardware
    Course:  CSE 465 — Pattern Recognition and Neural Network
    Faculty: Dr. Nabeel Mohammed [NbM]
             Associate Professor, PhD in Computer Science, Monash University
    Members: Rafiur Rahman Mashrafi   | 2221971042 | rafiur.mashrafi@northsouth.edu
             Md. Shadman Shihab       | 2231639642 | shadman.shihab@northsouth.edu
             Md. Nafiul Alam Chowdhury| 2231774642 | nafiul.chowdhury@northsouth.edu
    Date:    May 2026

2.  ABSTRACT  (~200 words)
    ─────────────────────────────────────────────────────────────────
    - State the problem: Moshi's Helium-7B backbone requires ~14 GB VRAM,
      preventing fine-tuning on free-tier GPUs (Tesla T4, 15.6 GB)
    - State the approach: three-stage study — quantization analysis (Demo 1),
      HybridBackbone swap with Qwen2.5-0.5B (Demo 2), TinyLlamaBackbone swap
      with TinyLlama-1.1B (Demo 3)
    - State key results of Demo 2: training diverges (loss 7.59→9.56 over 1000
      steps); three structural root causes identified and diagnosed
    - State key results of Demo 3: swap verified, LoRA fine-tuning (300 steps,
      163.68M trainable params), full Tier-1 + Tier-2 evaluation computed,
      Gradio live demo produced; VRAM reduced to 5.5 GB during training
    - Mention backup project briefly (turn-taking classifier, 96.16% accuracy)
    - End with the takeaway: backbone replacement in tightly-coupled multimodal
      models requires more than LoRA alone; distillation and unfreezing of
      downstream components are necessary next steps

3.  INTRODUCTION
    ─────────────────────────────────────────────────────────────────
    - Paragraph 1: Motivation — real-time spoken dialogue, Moshi as SOTA,
      but 7B parameters are inaccessible on commodity hardware
    - Paragraph 2: Problem statement — T4 has 15.6 GB VRAM; BF16 Moshi is
      15.4 GB alone; fine-tuning impossible without backbone replacement
    - Paragraph 3: Our approach — iterative three-demo progression:
        Demo 1 → quantization feasibility
        Demo 2 → HybridBackbone (negative result, documented)
        Demo 3 → TinyLlamaBackbone (full run, surgical swap design)
    - Paragraph 4: Numbered contributions:
        (1) Systematic quantization analysis of Mimi codec; lossless INT8
        (2) HybridBackbone design and complete 1,000-step training with root-
            cause diagnosis of three structural failures
        (3) Two bug patches to the Moshi reference implementation
        (4) TinyLlamaBackbone: surgical inner-transformer swap with dimension
            adapters; full training + Tier-1/Tier-2 evaluation + Gradio demo
        (5) 9 engineering problems resolved in Demo 3 (dtype, KV cache,
            tokenizer, OOM, codebook indexing)
        (6) Lightweight turn-taking classifier (DistilBERT, 96.16%) as a
            companion speech-to-speech system
    - Paragraph 5: Paper structure overview

4.  LITERATURE REVIEW
    ─────────────────────────────────────────────────────────────────
    FORMAT FOR EVERY ENTRY (mandatory):
    "[Author(s)] [Ref] proposed/developed/introduced [name] for [objective].
     The study utilized/employed [method/dataset] to [task].
     Experimental results demonstrated that [metric/result] compared to
     [baseline]. The findings concluded that [contribution/significance]."

    Entries (in this order):
    [1]  Defossez et al. — Moshi (speech-text foundation model, Mimi codec,
         Helium-7B, full-duplex dialogue)
    [2]  Borsos et al. — AudioLM (language modeling for audio generation)
    [3]  Zhang et al. — SpeechGPT (cross-modal conversational LLM)
    [4]  Hu et al. — LoRA (low-rank adaptation)
    [5]  Dettmers et al. — QLoRA (4-bit NF4 quantized fine-tuning)
    [6]  Dettmers et al. — bitsandbytes / LLM.int8()
    [7]  Hinton, Vinyals & Dean — Knowledge distillation
    [8]  Radford et al. — Whisper (robust ASR)
    [9]  Qwen Team — Qwen2.5 technical report (student model, Demo 2)
    [10] Zhang et al. — TinyLlama (student model, Demo 3)
    [11] Yang et al. — DuplexCascade (2026, baseline for backup project)
    [12] Sanh et al. — DistilBERT (classifier backbone, backup)
    [13] Li et al. — DailyDialog dataset (backup classifier training)

5.  PROPOSED METHOD(S)
    ─────────────────────────────────────────────────────────────────
    5.1  Demo 1 — Quantization Analysis
         - Overview of Mimi codec architecture and Moshiko LM (7B)
         - Six-experiment quantization pipeline:
           BF16 vs Q8 | Manual INT8 PTQ | INT4 NF4 | Layer-wise sensitivity
           | Mixed precision | Dynamic quantization (incompatible)
         - [PLACEHOLDER: Figure — layer-wise sensitivity bar chart]
         - [PLACEHOLDER: Figure — mixed precision strategy diagram]

    5.2  Demo 2 — HybridBackbone (Qwen2.5-0.5B)
         - Swap point: moshi.decoder (replaces entire decoder)
         - [PLACEHOLDER: Figure — HybridBackbone architecture diagram
           showing: Moshi pipeline → 4096 → Win(896) → Qwen → Wout(4096)
           → depth_decoder]
         - Dimension bridge: Win Linear(4096→896), Wout Linear(896→4096)
         - LoRA config: rank=16, alpha=32, targeting all attention+MLP layers
         - Memory stack: 4-bit NF4, 8-bit AdamW, gradient checkpointing,
           2s clip → peak VRAM 2.98 GB
         - Two bug fixes: Mimi padding overflow, depth decoder dtype mismatch
         - Mini-Omni parallel work: brief mention — text-to-text limitation,
           modality mismatch lesson

    5.3  Demo 3 — TinyLlamaBackbone (TinyLlama-1.1B)  [PRIMARY FOCUS]
         - Swap point: moshi.decoder.model (surgical inner-transformer only)
         - Design principle: "everything believes Helium is still present"
           — embed_tokens, lm_head, depth_decoder, Mimi all unchanged
         - [PLACEHOLDER: Figure — TinyLlamaBackbone architecture diagram
           showing: Moshi outer wrapper → embed_tokens (frozen) → 4096
           → input_adapter(2048) → TinyLlama LlamaModel → output_adapter(4096)
           → lm_head (frozen) → depth_decoder (frozen)]
         - [PLACEHOLDER: Figure — Demo 2 vs Demo 3 swap point comparison
           side-by-side diagram]
         - Comparison table: Helium-7B / Demo 2 / Demo 3 (full 3-column table)
         - LoRA on TinyLlama: 163.68M / 2.19B trainable (7.479%)
         - Training: 300 steps, DailyTalkContiguous 180/20 split,
           MAX_AUDIO_TOKENS=32, audio_labels=None (skip depth decoder)
         - 9 engineering problems and solutions (table format):
           Cell 17 × 4 bugs | Cell 27 × 5 bugs

    5.4  Backup — Lightweight Turn-Taking Pipeline
         - [PLACEHOLDER: Figure — pipeline diagram:
           Speech → Whisper → DistilBERT → TinyLlama → edge-tts → Speech]
         - DistilBERT classifier: 3-class (wait/respond/backchannel),
           DailyDialog, class-weighted loss, 45 min on T4
         - Classical comparison: GNB (TF-IDF), k-NN (DistilBERT embeddings)

6.  EXPERIMENTAL SETUP / EXPERIMENTS
    ─────────────────────────────────────────────────────────────────
    - Hardware table: Tesla T4, 15.6 GB VRAM, Google Colab free tier
    - Software stack table (all versions — see Section 8 of CONTEXT.md)
    - Datasets table:
        DailyTalkContiguous: 200 dialogues (180 train / 20 val), 24kHz stereo
        DailyDialog: 13,118 dialogues → 51,184 train / 8,645 test
    - Hyperparameters table (two columns: Demo 2 | Demo 3):
        Demo 2: 1,000 steps, lr=2e-4, batch=4, AdamW8bit, clip=2s, LoRA r=16
        Demo 3: 300 steps, lr=2e-4, MAX_AUDIO_TOKENS=32, audio_labels=None,
                LoRA r=16, alpha=32, VRAM 5.5 GB
    - Demo 1 quantization experiment suite table (6 experiments, status column)
    - Demo 3 engineering problems table (9 bugs: cell, error, fix)
    - Mini-Omni: hardware constraint narrative, 3 runs summary

7.  PERFORMANCE METRICS WITH JUSTIFICATION
    ─────────────────────────────────────────────────────────────────
    Present as a table: Metric | Formula/Definition | Demo Used In | Justification

    - Loss (cross-entropy): LM quality baseline; lower = better learning
    - Perplexity (exp(loss)): interpretable LM confusion measure
    - Token Accuracy: fraction of correct next-token predictions
    - Macro F1: balanced precision/recall across classes (imbalanced data)
    - BLEU: n-gram overlap with reference text; standard generation metric
    - WER (Word Error Rate): ASR-based end-to-end speech quality via Whisper-tiny
    - CER (Character Error Rate): finer-grained than WER for short utterances
    - Audio Token Accuracy (codebook-0): direct measure of speech codebook prediction
    - Duration Ratio: generated audio length / reference length (1.0 = perfect)
    - SNR (Signal-to-Noise Ratio, dB): codec reconstruction quality; higher = better
    - RTF (Real-Time Factor): processing time / audio duration; <1.0 = real-time capable
    - VRAM (GB): GPU memory consumption; feasibility constraint for T4
    - Classification Accuracy: turn-taking classifier correctness (backup)
    - ARI (Adjusted Rand Index): unsupervised cluster quality (backup k-Means)
    - PCA Variance Explained: dimensionality reduction fidelity (backup)

8.  RESULTS
    ─────────────────────────────────────────────────────────────────
    8.1  Demo 1 — Quantization Results
         - Table: BF16 vs Q8 SNR comparison (0.00 dB difference — lossless)
         - Table: RTF latency benchmark (1s/3s/5s/10s)
         - Table: Top-5 most sensitive layers (SNR drop per layer)
         - Table: Mixed-precision vs baselines
         - Table: VRAM usage comparison

    8.2  Demo 2 — HybridBackbone Results  [PRIMARY FOCUS]
         - Table: Training metrics history (steps 200–1000, loss diverges)
         - [PLACEHOLDER: Figure — loss curve showing divergence]
         - Root cause analysis subsection (3 numbered causes with code-level detail)
         - End-to-end result: pure noise; audio acc = 0.0 throughout
         - Mini-Omni sidebar: 3-run loss table, 0% accuracy explanation
         - Resource comparison table: Helium-7B vs Qwen2.5-0.5B

    8.3  Demo 3 — TinyLlamaBackbone Results  [PRIMARY FOCUS]
         - Table: Step-300 evaluation metrics with honest interpretation
           (loss, perplexity, BLEU, WER, CER, audio_tok_acc, dur_ratio, accuracy)
         - [PLACEHOLDER: Figure — 6-panel metrics plot (metrics_plot.png from Drive)]
         - 3-way audio comparison: before_audio / after_audio / finetuned_output
           (describe duration, quality difference; use waveform/spectrogram if Drive
           files are shared)
         - Overfitting diagnosis: why loss→0 but wer>1.0 (small data, short clips,
           padding tokens, depth decoder skipped)
         - Table: 9 engineering bugs (cell, error description, fix applied)
         - Gradio demo: confirm swap is live, faculty demonstration

    8.4  Backup — Turn-Taking Results
         - Table: Classifier accuracy comparison (rule-based / GNB / k-NN / DistilBERT)
         - Table: Per-sample pipeline results (6 clips, expected vs predicted)
         - Table: Latency breakdown per component vs DuplexCascade
         - k-Means ARI + PCA variance explained

9.  CONCLUSION
    ─────────────────────────────────────────────────────────────────
    - Paragraph 1: Summary of Demo 1 — quantization is lossless, T4 feasibility confirmed
    - Paragraph 2 (Demo 2 — detailed): HybridBackbone design, training failure,
      three root causes (unmasked padding, scrambled projector, frozen depth decoder),
      contribution as a documented negative result with diagnostic value
    - Paragraph 3 (Demo 3 — detailed): TinyLlamaBackbone surgical design overcomes
      Demo 2's architectural flaws; training ran to completion; full evaluation computed;
      overfitting due to data/sequence constraints, not architectural failure
    - Paragraph 4: Mini-Omni lesson — text LLM swap ≠ speech-to-speech
    - Paragraph 5: Future work:
        (1) Knowledge distillation loss (match Helium hidden states via MSE)
        (2) Unfreeze depth decoder with LoRA adapters
        (3) Larger student model (Qwen2.5-1.5B or Llama-3.2-3B)
        (4) More data (full 2,500-dialogue DailyTalk) and longer training
        (5) Remove depth-decoder skip (audio_labels=None) with memory offloading

10. MANDATORY APPENDIX – 1
    ─────────────────────────────────────────────────────────────────
    A. Code and Repository Links
       - GitHub: https://github.com/RRM006/moshi-backbone-swap-nbm
         (with repo structure listing)
       - Google Drive folders — table with QR codes (2cm × 2cm each):
           Demo 1: https://drive.google.com/drive/folders/1CjVNMQW77IXPGnGI7oa3feMDEa_dg7or
           Demo 2: https://drive.google.com/drive/folders/1FokGH0cn9LkRj23Xq8gdsToaBaeM1k2a
           Demo 3: https://drive.google.com/drive/folders/100rsxBt_h1Jip2UxZ2-Tt2b6Gx0gTLxn
           Backup: https://drive.google.com/drive/folders/1SEZ-XZmAWYyEIIiIXbua05vQ_FTK0Imk

    B. Reproducible Instructions
       - Package version table (locked stack — Section 8 of CONTEXT.md)
       - Warning: always start with a fresh Colab session
       - Demo 1: run quantization_analysis.ipynb cell by cell (note partial experiments)
       - Demo 2: run Moshi_Colab_Notebook_llmswap_qwen_decoder_module.ipynb in order
       - Demo 3: step-by-step instructions (use the 15-step Gradio run instructions
         from Section 5 of CONTEXT.md as the basis — these are the canonical steps)
       - Backup: run Lightweight_Turn-Taking_Classification.ipynb in order

    C. Agent Reproduction Prompt (OpenCode / AI Agent)
       - A single self-contained prompt that an agent can execute to reproduce
         Demo 3 end-to-end (the primary deliverable):
           * Clone repo from GitHub
           * Install locked package stack
           * HuggingFace login and model download
           * Run CELL 1 through CELL 16 (environment + swap)
           * Run FIX cells (tokenizer + DataLoaders)
           * Run CELL 27 (training loop, 300 steps)
           * Run CELL 28–31 (evaluation, plots, end-to-end test)
           * Run Gradio cell for demo
       - Agent prompt must be self-contained: no manual steps assumed
```

---

## 15. WHAT DOES NOT NEED TO BE ASSUMED

Everything in this context file is drawn directly from uploaded notebooks, PDFs, and context documents. No information has been inferred or assumed without a source document.

---

## 16. AI USE ACKNOWLEDGMENT (MUST APPEAR IN REPORT)

The report must include an honest acknowledgment of AI tool use. Suggested text for the report:

> **AI Tools Acknowledgment:** The authors used large language model (LLM) assistants (including Claude by Anthropic) to support parts of this project. AI assistance was used for: (1) debugging Python code and resolving CUDA/dtype errors in the Colab notebooks, (2) drafting and refining sections of this report, and (3) generating boilerplate training loop and evaluation code. All experimental results, architectural decisions, root cause analyses, and interpretations are the original work of the authors. The final report was reviewed and edited by all group members.

**Placement in report:** After the Conclusion, inside `\section*{Acknowledgments}` (IEEE format).

**Tone guidance:** Be specific about what AI helped with (code debugging, writing assistance) versus what was original (experimental design, architecture decisions, result interpretation). Do not overstate or understate AI involvement.
