# SESSION_CONTEXT.md

## Project Title
EHR-Based Pre-Consultation Medical Documentation System (CSE499 Capstone)

## Project Summary
A Bangla multi-dialect medical speech-to-EHR pipeline that listens to patients describe symptoms in Bangla (any regional dialect), converts speech to text via ASR, extracts medical entities via NER, and generates a structured Electronic Health Record (EHR) in JSON format for doctors to review before consultation. The system handles 5 regional dialects (Puran Dhaka, Barishal, Sylheti, Normal Bangla, Indian Bangla) and Bangla-English code-mixed speech. Built entirely on zero budget using Google Colab (free tier) and Google Drive for storage.

## Current Status
**Phase 1 — ASR, Notebook 1 of 4**: The first notebook (`01_data_download.ipynb`) has been fully generated and delivered. The user needs to test it in Colab before proceeding to Notebook 2.

## What Has Been Completed
- ✅ Master plan document (`CSE499_Master_Plan.docx`) read and fully understood
- ✅ Project requirements clarified and confirmed with user
- ✅ Delivery approach decided: one notebook at a time for safe testing
- ✅ Whisper model size confirmed: `whisper-small` (244M params)
- ✅ Starting point confirmed: zero existing data — full download pipeline needed
- ✅ Full Google Drive folder structure defined (exact paths from DOCX)
- ✅ `01_data_download.ipynb` — complete 11-cell notebook delivered with:
  - Dependency installation (yt-dlp, gdown, pandas)
  - Google Drive mounting
  - Complete folder structure creation
  - YouTube URL configuration with metadata template
  - Download function with skip-existing logic (idempotent)
  - dataset_log.csv generation
  - Download verification
  - Full debugging tips for every cell
  - Session-resume instructions

## What Is Pending (Next Steps)
1. 🔲 **User tests `01_data_download.ipynb`** in Colab — replace placeholder URLs, run, verify downloads
2. 🔲 **`02_audio_preprocessing.ipynb`** — noise removal, silence trimming, 16kHz mono WAV conversion
3. 🔲 **`03_model_comparison.ipynb`** — run 10+ ASR models (Wav2Vec2, HuBERT, Data2Vec, WavLM, XLSR-53, Whisper, Canary, MMS, SeamlessM4T, Conformer-CTC), calculate WER scores
4. 🔲 **`04_whisper_finetune.ipynb`** — fine-tune Whisper-small on custom dialect dataset with checkpoint auto-save to Drive
5. 🔲 **`01_ner_dataset_prep.ipynb`** — create BIO-labeled NER dataset from Phase 1 transcripts
6. 🔲 **`02_ner_model_comparison.ipynb`** — run 6+ NER models (BanglaBERT, mBERT, XLM-RoBERTa, bangla-bert-base, Bio-ClinicalBERT, SpanBERT), calculate F1 scores
7. 🔲 **`03_banglabert_finetune.ipynb`** — fine-tune BanglaBERT for medical NER with checkpoint auto-save to Drive

## Key Decisions Already Made
| Decision | Value |
|----------|-------|
| Root Drive folder | `CSE499_EHR_Project` |
| Delivery method | One notebook at a time (user tests each before next) |
| Starting data | Zero — full YouTube download pipeline included |
| Whisper model size | `whisper-small` |
| Audio format | 16kHz mono WAV (after preprocessing) |
| Download tool | `yt-dlp` |
| Target dataset size | 40-60 clips per dialect (200-300 total) |
| Audio clip length | 30 seconds to 5 minutes |
| Dialect codes | `pd`=Puran Dhaka, `br`=Barishal, `sy`=Sylheti, `nb`=Normal Bangla, `ib`=Indian Bangla |
| File naming | `[dialect_code]_[3-digit]_[gender]_[age].[ext]` (e.g., `br_001_female_30s.mp3`) |
| Session safety | All artifacts saved to Drive; checkpoints every 200-500 steps; idempotent code |
| Colab runtime | T4 GPU for training, CPU for data prep |
| NER entity types | SYMPTOM, DISEASE, MEDICATION, DURATION, BODY_PART, ALLERGY, SEVERITY |
| NER labeling format | BIO (Beginning, Inside, Outside) |
| Train/test split | 80/20 for NER |
| EHR output format | JSON |

## Folder & File Structure
```
CSE499_EHR_Project/                          ← Root (shared Google Drive folder)
│
├── 00_Admin/
│   ├── team_contacts.txt
│   ├── weekly_progress_log.docx
│   └── project_plan.docx
│
├── 01_Dataset/
│   ├── raw_audio/
│   │   ├── puran_dhaka/                     ← pd_*.mp3
│   │   ├── barishal/                        ← br_*.mp3
│   │   ├── sylheti/                         ← sy_*.mp3
│   │   ├── normal_bangla/                   ← nb_*.mp3
│   │   └── indian_bangla/                   ← ib_*.mp3
│   ├── cleaned_audio/                       ← 16kHz mono WAV
│   ├── transcripts/
│   │   ├── manual/
│   │   └── auto/
│   ├── metadata/
│   │   └── dataset_log.csv
│   └── ner_labeled/                         ← .jsonl files
│
├── 02_Phase1_ASR/
│   ├── notebooks/
│   │   ├── 01_data_download.ipynb           ← ✅ DELIVERED
│   │   ├── 02_audio_preprocessing.ipynb     ← 🔲 PENDING
│   │   ├── 03_model_comparison.ipynb        ← 🔲 PENDING
│   │   └── 04_whisper_finetune.ipynb        ← 🔲 PENDING
│   ├── model_outputs/
│   │   ├── wav2vec2_transcripts/
│   │   ├── hubert_transcripts/
│   │   ├── whisper_transcripts/
│   │   ├── xlsr53_transcripts/
│   │   └── mms_transcripts/
│   ├── evaluation/
│   │   └── wer_scores.csv
│   └── saved_models/
│       └── whisper_finetuned/
│
├── 03_Phase2_NER/
│   ├── notebooks/
│   │   ├── 01_ner_dataset_prep.ipynb        ← 🔲 PENDING
│   │   ├── 02_ner_model_comparison.ipynb    ← 🔲 PENDING
│   │   └── 03_banglabert_finetune.ipynb     ← 🔲 PENDING
│   ├── model_outputs/
│   ├── evaluation/
│   │   └── f1_scores.csv
│   └── saved_models/
│       └── banglabert_ner_finetuned/
│
├── 04_Phase3_EHR/
│   ├── notebooks/
│   ├── ehr_outputs/
│   └── templates/
│       └── ehr_template.json
│
├── 05_Pipeline/
│   ├── full_pipeline_demo.ipynb
│   └── sample_outputs/
│
└── 06_Presentation/
    ├── slides.pptx
    ├── demo_video.mp4
    └── results_summary.pdf
```

## How To Resume In A New Session
Paste this file content at the start of a new chat and say:
> "Read this SESSION_CONTEXT.md. This is our project context. Continue from the PENDING section. Ask me if anything is unclear before starting."

---

## ⚠️ Notes & Flags
- No contradictions found in chat history
- All decisions explicitly confirmed by user
- Notebook 1 (`01_data_download.ipynb`) is fully delivered but **not yet tested** by user
- Placeholder URLs in Cell 6 must be replaced with real YouTube URLs before running
- User must have Editor access to the shared Google Drive folder before running any notebook
