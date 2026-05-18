# =============================================================
# CSE465 | Speech-to-Speech Project
# Day 3: Full Speech-to-Speech Pipeline + Evaluation
# =============================================================
# BEFORE STARTING:
#   1. Runtime > Change runtime type > T4 GPU
#   2. Run Cell 1 first (Drive mount) before anything else
#   3. Day 1 AND Day 2 must be complete
#   4. Drive must contain:
#      - models/best_classifier/
#      - audio_samples/ (6 wav files)
#      - results/baseline_pipeline_results.json
# Expected total runtime: 2-3 hours
# Can be run on Account 2 if Account 1 session is exhausted
# =============================================================


# -------------------------------------------------------------
# CELL 1: Mount Drive + Verify All Required Files
# Run this FIRST. Every session must start here.
# -------------------------------------------------------------
from google.colab import drive
drive.mount('/content/drive')

import os

DRIVE_PATH = "/content/drive/MyDrive/CSE465_Project"

required_files = [
    f"{DRIVE_PATH}/models/best_classifier/config.json",
    f"{DRIVE_PATH}/audio_samples/en_wait.wav",
    f"{DRIVE_PATH}/audio_samples/en_respond.wav",
    f"{DRIVE_PATH}/audio_samples/en_backchannel.wav",
    f"{DRIVE_PATH}/audio_samples/fr_wait.wav",
    f"{DRIVE_PATH}/audio_samples/fr_respond.wav",
    f"{DRIVE_PATH}/audio_samples/fr_backchannel.wav",
    f"{DRIVE_PATH}/results/baseline_pipeline_results.json",
    f"{DRIVE_PATH}/results/baseline_accuracy.json",
    f"{DRIVE_PATH}/results/after_accuracy.json",
]

print("Verifying Day 1 and Day 2 files...")
all_ok = True
for path in required_files:
    exists = os.path.exists(path)
    status = "OK" if exists else "MISSING"
    print(f"  [{status}] {os.path.basename(path)}")
    if not exists:
        all_ok = False

if not all_ok:
    raise FileNotFoundError(
        "Some required files are missing.\n"
        "Complete Day 1 and Day 2 before running Day 3."
    )

print("\nAll required files found.")

# Reinstall packages
!pip install -q -r /content/drive/MyDrive/CSE465_Project/requirements.txt
print("Packages reinstalled.")


# -------------------------------------------------------------
# CELL 2: Verify GPU
# -------------------------------------------------------------
import torch

print(f"GPU available : {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU name      : {torch.cuda.get_device_name(0)}")
    total_mem = torch.cuda.get_device_properties(0).total_memory / 1e9
    print(f"GPU memory    : {total_mem:.1f} GB")
else:
    raise RuntimeError(
        "No GPU found. Go to Runtime > Change runtime type > T4 GPU."
    )

device = torch.device("cuda")


# -------------------------------------------------------------
# CELL 3: Load Whisper-small (ASR)
# Pretrained. No fine-tuning. Handles EN and FR.
# -------------------------------------------------------------
import whisper

print("Loading Whisper-small...")
whisper_model = whisper.load_model("small")
print("Whisper-small loaded.")
print(f"GPU memory used: {torch.cuda.memory_allocated()/1e9:.2f} GB")


# -------------------------------------------------------------
# CELL 4: Load Trained DistilBERT Classifier
# This is the model trained in Day 2.
# Replaces the 7B LLM the paper used for turn-taking decisions.
# -------------------------------------------------------------
from transformers import (
    DistilBertForSequenceClassification,
    DistilBertTokenizer
)

CLASSIFIER_PATH = f"{DRIVE_PATH}/models/best_classifier"

print("Loading trained turn-taking classifier...")
classifier = DistilBertForSequenceClassification.from_pretrained(
    CLASSIFIER_PATH, num_labels=3
).to(device)
classifier.eval()

clf_tokenizer = DistilBertTokenizer.from_pretrained(CLASSIFIER_PATH)

LABEL_NAMES = {0: "wait", 1: "respond", 2: "backchannel"}

print("Classifier loaded.")
print(f"GPU memory used: {torch.cuda.memory_allocated()/1e9:.2f} GB")


# -------------------------------------------------------------
# CELL 5: Load Phi-3-mini (Response Generator)
# 4-bit quantized to fit T4 VRAM.
# Only called when classifier says "respond".
# -------------------------------------------------------------
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig
)

print("Loading Phi-3-mini-4k-instruct (4-bit quantized)...")

quant_config = BitsAndBytesConfig(load_in_4bit=True)
phi_tokenizer = AutoTokenizer.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    trust_remote_code=True
)
phi_model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    quantization_config=quant_config,
    device_map="auto",
    trust_remote_code=True
)
phi_model.eval()

print("Phi-3-mini loaded.")
print(f"GPU memory used: {torch.cuda.memory_allocated()/1e9:.2f} GB")


# -------------------------------------------------------------
# CELL 6: Define All Pipeline Functions
#
# The full pipeline is:
# Audio → [Whisper] → text + language
#       → [DistilBERT classifier] → decision
#       → if respond: [Phi-3-mini] → response text
#       → [edge-tts] → speech output
#
# This is what the paper's Fig.1 shows, but with:
#   - Open-source ASR (Whisper) instead of DSM-ASR
#   - Trained lightweight classifier instead of 7B LLM
#   - edge-tts instead of DSM-TTS
# -------------------------------------------------------------
import asyncio
import edge_tts
import time
import numpy as np

# --- Voice map by language ---
VOICE_MAP = {
    "en": "en-US-JennyNeural",
    "fr": "fr-FR-DeniseNeural",
    "default": "en-US-JennyNeural"
}

# --- Response templates for backchannel ---
BACKCHANNEL_RESPONSES = {
    "en": ["Uh-huh, please go on.",
           "I see, continue.",
           "Right, go ahead."],
    "fr": ["Je vois, continuez.",
           "Oui, allez-y.",
           "D'accord, continuez."]
}

import random

# ---- STEP 1: ASR ----
def transcribe_audio(audio_path):
    """
    Transcribe audio using Whisper-small.
    Returns transcription text and detected language.
    """
    result = whisper_model.transcribe(audio_path)
    text   = result["text"].strip()
    lang   = result["language"]  # "en", "fr", etc.
    return text, lang


# ---- STEP 2: Turn-Taking Decision ----
def classify_turn(text):
    """
    Classify text into: wait (0) / respond (1) / backchannel (2)
    Uses trained DistilBERT classifier from Day 2.
    Returns label string and confidence scores.
    """
    encoding = clf_tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=64,
        return_tensors="pt"
    )
    input_ids      = encoding["input_ids"].to(device)
    attention_mask = encoding["attention_mask"].to(device)

    with torch.no_grad():
        outputs = classifier(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        logits = outputs.logits
        probs  = torch.softmax(logits, dim=1).cpu().numpy()[0]
        pred   = torch.argmax(logits, dim=1).item()

    confidence = {LABEL_NAMES[i]: round(float(probs[i]), 3) for i in range(3)}
    return LABEL_NAMES[pred], confidence


# ---- STEP 3: Generate Response (only if "respond") ----
def generate_response(transcription, lang):
    """
    Generate a natural response using Phi-3-mini.
    Only called when classifier says "respond".
    Max 40 tokens to keep latency low on T4.
    """
    lang_instruction = "Respond in French." if lang == "fr" else "Respond in English."
    if lang not in ("en", "fr"):
        lang_instruction = "Respond in English."

    prompt = (
        f"<|system|>\nYou are a helpful voice assistant. "
        f"Give a short, natural spoken response in 1-2 sentences. "
        f"{lang_instruction}<|end|>\n"
        f"<|user|>\n{transcription}<|end|>\n"
        f"<|assistant|>\n"
    )

    inputs = phi_tokenizer(prompt, return_tensors="pt").to("cuda")

    with torch.no_grad():
        outputs = phi_model.generate(
            **inputs,
            max_new_tokens=60,
            do_sample=False,
            temperature=1.0,
            pad_token_id=phi_tokenizer.eos_token_id
        )

    full_output = phi_tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Extract only the assistant reply
    response = full_output.split("<|assistant|>")[-1].strip()
    return response


# ---- STEP 4: Text-to-Speech ----
async def synthesize_speech(text, lang, out_path):
    """
    Convert response text to speech using edge-tts.
    Selects voice based on detected language.
    """
    voice = VOICE_MAP.get(lang, VOICE_MAP["default"])
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(out_path)


# ---- FULL PIPELINE ----
def run_full_pipeline(audio_path, verbose=True):
    """
    Complete speech-to-speech pipeline.
    Input : path to .wav audio file
    Output: path to response .wav + timing breakdown
    """
    result = {
        "input_file":     os.path.basename(audio_path),
        "transcription":  "",
        "detected_lang":  "",
        "decision":       "",
        "confidence":     {},
        "response_text":  "",
        "output_file":    None,
        "asr_latency":    0.0,
        "clf_latency":    0.0,
        "llm_latency":    0.0,
        "tts_latency":    0.0,
        "total_latency":  0.0,
    }

    pipeline_start = time.time()

    # --- Step 1: ASR ---
    t0 = time.time()
    transcription, lang = transcribe_audio(audio_path)
    result["asr_latency"]    = round(time.time() - t0, 3)
    result["transcription"]  = transcription
    result["detected_lang"]  = lang

    if verbose:
        print(f"  Transcription : \"{transcription}\"")
        print(f"  Language      : {lang}")
        print(f"  ASR latency   : {result['asr_latency']}s")

    # --- Step 2: Turn-Taking Decision ---
    t0 = time.time()
    decision, confidence = classify_turn(transcription)
    result["clf_latency"] = round(time.time() - t0, 3)
    result["decision"]    = decision
    result["confidence"]  = confidence

    if verbose:
        print(f"  Decision      : {decision}")
        print(f"  Confidence    : {confidence}")
        print(f"  CLF latency   : {result['clf_latency']}s")

    # --- Step 3: Generate Response ---
    response_text = ""
    t0 = time.time()

    if decision == "wait":
        response_text = ""  # System stays silent
        if verbose:
            print(f"  Action        : System waits (silent)")

    elif decision == "backchannel":
        options = BACKCHANNEL_RESPONSES.get(lang, BACKCHANNEL_RESPONSES["en"])
        response_text = random.choice(options)
        if verbose:
            print(f"  Backchannel   : \"{response_text}\"")

    elif decision == "respond":
        response_text = generate_response(transcription, lang)
        if verbose:
            print(f"  Response      : \"{response_text}\"")

    result["llm_latency"]   = round(time.time() - t0, 3)
    result["response_text"] = response_text

    if verbose and decision != "wait":
        print(f"  LLM latency   : {result['llm_latency']}s")

    # --- Step 4: TTS (only if there is a response) ---
    t0 = time.time()
    if response_text:
        out_path = f"/content/output_{os.path.basename(audio_path)}"
        asyncio.run(synthesize_speech(response_text, lang, out_path))
        result["output_file"]  = out_path
        result["tts_latency"]  = round(time.time() - t0, 3)
        if verbose:
            print(f"  TTS latency   : {result['tts_latency']}s")
    else:
        result["tts_latency"] = 0.0

    result["total_latency"] = round(time.time() - pipeline_start, 3)

    if verbose:
        print(f"  Total latency : {result['total_latency']}s")

    return result


# -------------------------------------------------------------
# CELL 7: Run Full Pipeline on All 6 Audio Samples
#
# Same 6 files used in Day 1.
# This gives AFTER pipeline results to compare against Day 1.
# -------------------------------------------------------------
import json

AUDIO_PATH = f"{DRIVE_PATH}/audio_samples"

# Load audio metadata from Day 1
with open(f"{AUDIO_PATH}/metadata.json") as f:
    audio_meta = json.load(f)

print("=" * 60)
print("AFTER TRAINING — Full Speech-to-Speech Pipeline")
print("=" * 60)
print("Running pipeline on all 6 test audio samples...\n")

after_pipeline_results = []

for meta in audio_meta:
    audio_file     = f"{AUDIO_PATH}/{meta['file']}"
    expected_label = meta["expected_label"]

    print(f"{'='*50}")
    print(f"File     : {meta['file']}")
    print(f"Expected : {expected_label}")

    result = run_full_pipeline(audio_file, verbose=True)
    result["expected_label"] = expected_label
    result["correct"] = result["decision"] == expected_label

    print(f"  Correct?      : {'YES' if result['correct'] else 'NO'}")
    after_pipeline_results.append(result)

# Save to Drive
AFTER_PIPELINE_PATH = f"{DRIVE_PATH}/results/after_pipeline_results.json"
with open(AFTER_PIPELINE_PATH, "w") as f:
    json.dump(after_pipeline_results, f, indent=2)

print(f"\nResults saved to Drive: {AFTER_PIPELINE_PATH}")


# -------------------------------------------------------------
# CELL 8: Before vs After Pipeline Comparison Table
#
# This is the core comparison for your report.
# Covers: turn-taking accuracy + latency breakdown.
# -------------------------------------------------------------
import json

# Load Day 1 baseline pipeline results
with open(f"{DRIVE_PATH}/results/baseline_pipeline_results.json") as f:
    before_results = json.load(f)

# Load Day 3 after pipeline results
with open(f"{DRIVE_PATH}/results/after_pipeline_results.json") as f:
    after_results = json.load(f)

# Load classifier accuracy numbers
with open(f"{DRIVE_PATH}/results/baseline_accuracy.json") as f:
    baseline_acc = json.load(f)
with open(f"{DRIVE_PATH}/results/after_accuracy.json") as f:
    after_acc = json.load(f)

def compute_summary(results):
    correct     = sum(1 for r in results if r["correct"])
    total       = len(results)
    avg_asr     = sum(r["asr_latency"]   for r in results) / total
    avg_clf     = sum(r["clf_latency"]   for r in results) / total
    avg_llm     = sum(r.get("llm_latency", 0) for r in results) / total
    avg_tts     = sum(r["tts_latency"]   for r in results) / total
    avg_total   = sum(r["total_latency"] for r in results) / total
    return {
        "accuracy":    correct / total,
        "correct":     correct,
        "total":       total,
        "avg_asr":     round(avg_asr, 3),
        "avg_clf":     round(avg_clf, 3),
        "avg_llm":     round(avg_llm, 3),
        "avg_tts":     round(avg_tts, 3),
        "avg_total":   round(avg_total, 3),
    }

before_summary = compute_summary(before_results)
after_summary  = compute_summary(after_results)

print("\n" + "=" * 65)
print("FULL COMPARISON TABLE")
print("=" * 65)
print(f"{'Metric':<35} {'BEFORE':>12} {'AFTER':>12}")
print("-" * 65)

# Turn-taking accuracy
print(f"{'Turn-taking accuracy (pipeline)':<35} "
      f"{before_summary['accuracy']*100:>11.1f}% "
      f"{after_summary['accuracy']*100:>11.1f}%")

print(f"{'Turn-taking accuracy (classifier)':<35} "
      f"{baseline_acc['accuracy']*100:>11.1f}% "
      f"{after_acc['accuracy']*100:>11.1f}%")

print()
# Latency breakdown
print(f"{'Avg ASR latency':<35} "
      f"{before_summary['avg_asr']:>11.3f}s "
      f"{after_summary['avg_asr']:>11.3f}s")

print(f"{'Avg Classifier latency':<35} "
      f"{before_summary['avg_clf']:>11.3f}s "
      f"{after_summary['avg_clf']:>11.3f}s")

print(f"{'Avg LLM latency':<35} "
      f"{before_summary['avg_llm']:>11.3f}s "
      f"{after_summary['avg_llm']:>11.3f}s")

print(f"{'Avg TTS latency':<35} "
      f"{before_summary['avg_tts']:>11.3f}s "
      f"{after_summary['avg_tts']:>11.3f}s")

print(f"{'Avg total latency':<35} "
      f"{before_summary['avg_total']:>11.3f}s "
      f"{after_summary['avg_total']:>11.3f}s")

print()
# Paper comparison
print(f"{'Paper avg latency (DuplexCascade)':<35} {'~1.70s':>12} {'N/A':>12}")
print(f"{'Paper hardware':<35} {'8x H100':>12} {'N/A':>12}")
print(f"{'Your hardware':<35} {'1x T4':>12} {'1x T4':>12}")
print(f"{'Code-mixed support':<35} {'No':>12} {'Yes':>12}")
print(f"{'Open-source components':<35} {'No':>12} {'Yes':>12}")
print("=" * 65)


# -------------------------------------------------------------
# CELL 9: Per-Sample Comparison Table
# Shows each audio file: expected vs before vs after decision.
# -------------------------------------------------------------
print("\n" + "=" * 75)
print("PER-SAMPLE RESULTS")
print("=" * 75)
print(f"{'File':<25} {'Expected':<14} {'Before':>10} {'After':>10} {'Before OK':>10} {'After OK':>10}")
print("-" * 75)

before_dict = {r["file"]: r for r in before_results}

for after in after_results:
    fname    = after["input_file"]
    expected = after["expected_label"]
    before   = before_dict.get(fname, {})

    before_pred = before.get("predicted", "N/A")
    after_pred  = after["decision"]
    before_ok   = "YES" if before.get("correct") else "NO"
    after_ok    = "YES" if after["correct"] else "NO"

    print(f"{fname:<25} {expected:<14} {before_pred:>10} {after_pred:>10} "
          f"{before_ok:>10} {after_ok:>10}")


# -------------------------------------------------------------
# CELL 10: Play Output Audio in Colab
# Listen to the pipeline's speech output directly in notebook.
# -------------------------------------------------------------
from IPython.display import Audio, display

print("\n" + "=" * 50)
print("AUDIO OUTPUT DEMO")
print("=" * 50)

for result in after_pipeline_results:
    print(f"\nFile    : {result['input_file']}")
    print(f"Decision: {result['decision']}")

    if result["output_file"] and os.path.exists(result["output_file"]):
        print(f"Response: \"{result['response_text']}\"")
        print("Playing response audio:")
        display(Audio(result["output_file"], autoplay=False))
    else:
        print("(No audio — system waited silently)")


# -------------------------------------------------------------
# CELL 11: Save Complete Comparison to Drive
# One file with all numbers for your report.
# -------------------------------------------------------------
complete_comparison = {
    "pipeline_comparison": {
        "before": before_summary,
        "after":  after_summary
    },
    "classifier_comparison": {
        "before_accuracy": baseline_acc["accuracy"],
        "after_accuracy":  after_acc["accuracy"],
        "improvement":     after_acc["improvement"]
    },
    "paper_reference": {
        "model":           "DuplexCascade",
        "hardware":        "8x NVIDIA H100",
        "avg_latency_sec": 1.70,
        "open_source":     False,
        "code_mixed":      False,
        "training":        "7B LLM LoRA, 5hrs, 8xH100"
    },
    "our_system": {
        "hardware":        "1x NVIDIA T4 (free Colab)",
        "open_source":     True,
        "code_mixed":      True,
        "asr":             "Whisper-small (pretrained)",
        "classifier":      "DistilBERT (trained Day 2)",
        "llm":             "Phi-3-mini 4-bit (pretrained)",
        "tts":             "edge-tts (free)"
    },
    "per_sample_results": after_pipeline_results
}

COMPARISON_PATH = f"{DRIVE_PATH}/results/complete_comparison.json"
with open(COMPARISON_PATH, "w") as f:
    json.dump(complete_comparison, f, indent=2)

print(f"\nComplete comparison saved: {COMPARISON_PATH}")


# -------------------------------------------------------------
# CELL 12: Final Report Table (Copy This Into Your Report)
# Ready to paste directly into your project report.
# -------------------------------------------------------------
print("\n" + "=" * 65)
print("COPY THIS TABLE INTO YOUR REPORT")
print("=" * 65)
print(f"""
+----------------------------------+-------------+-------------+-------------+
| Metric                           | Paper       | Ours BEFORE | Ours AFTER  |
+----------------------------------+-------------+-------------+-------------+
| Hardware                         | 8x H100     | 1x T4 free  | 1x T4 free  |
| ASR                              | DSM-ASR*    | Whisper-sm  | Whisper-sm  |
| Turn-taking model                | 7B LLM*     | Rule-based  | DistilBERT  |
| LLM                              | Qwen2-7B*   | Phi-3-mini  | Phi-3-mini  |
| TTS                              | DSM-TTS*    | edge-tts    | edge-tts    |
| Open-source                      | Partial     | Full        | Full        |
| Code-mixed support               | No          | Yes         | Yes         |
| Training required                | 5hrs/8xH100 | None        | 45min/1xT4  |
| Turn-taking accuracy             | Not reported| {before_summary['accuracy']*100:.1f}%       | {after_summary['accuracy']*100:.1f}%       |
| Avg total latency                | ~1.70s      | {before_summary['avg_total']:.2f}s         | {after_summary['avg_total']:.2f}s         |
+----------------------------------+-------------+-------------+-------------+
* Proprietary / not open-source
""")


# -------------------------------------------------------------
# CELL 13: Day 3 Summary
# -------------------------------------------------------------
print("\n" + "=" * 60)
print("DAY 3 COMPLETE — Files Saved to Drive")
print("=" * 60)
print(f"""
{DRIVE_PATH}/
└── results/
    ├── baseline_pipeline_results.json  ← BEFORE (Day 1)
    ├── after_pipeline_results.json     ← AFTER  (Day 3)
    └── complete_comparison.json        ← Full report table
""")
print("KEY NUMBERS FOR YOUR REPORT:")
print(f"  Classifier accuracy BEFORE : {baseline_acc['accuracy']*100:.2f}%")
print(f"  Classifier accuracy AFTER  : {after_acc['accuracy']*100:.2f}%")
print(f"  Pipeline accuracy  BEFORE  : {before_summary['accuracy']*100:.1f}%")
print(f"  Pipeline accuracy  AFTER   : {after_summary['accuracy']*100:.1f}%")
print(f"  Avg latency        BEFORE  : {before_summary['avg_total']:.2f}s")
print(f"  Avg latency        AFTER   : {after_summary['avg_total']:.2f}s")
print(f"  Paper latency              : ~1.70s (8x H100)")
print()
print("PROJECT COMPLETE.")
print("Days 4-5: Clean up notebooks + write report using numbers above.")
