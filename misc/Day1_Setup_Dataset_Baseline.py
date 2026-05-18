# =============================================================
# CSE465 | Speech-to-Speech Project
# Day 1: Setup + Dataset Preparation + Baseline Pipeline Test
# =============================================================
# Run each cell IN ORDER. Do not skip any cell.
# Expected total runtime: 2-3 hours
# =============================================================


# -------------------------------------------------------------
# CELL 1: Mount Google Drive
# Run this FIRST. Every session must start here.
# -------------------------------------------------------------
from google.colab import drive
drive.mount('/content/drive')

import os

DRIVE_PATH = "/content/drive/MyDrive/CSE465_Project"

# Create all folders we will need across all 5 days
os.makedirs(f"{DRIVE_PATH}/dataset",        exist_ok=True)
os.makedirs(f"{DRIVE_PATH}/checkpoints",    exist_ok=True)
os.makedirs(f"{DRIVE_PATH}/models",         exist_ok=True)
os.makedirs(f"{DRIVE_PATH}/audio_samples",  exist_ok=True)
os.makedirs(f"{DRIVE_PATH}/results",        exist_ok=True)

print("Drive mounted successfully.")
print(f"Project folder: {DRIVE_PATH}")
print("All subfolders ready.")


# -------------------------------------------------------------
# CELL 2: Install Dependencies
# This takes ~5 minutes. Run once.
# -------------------------------------------------------------
!pip install -q openai-whisper \
               datasets \
               transformers \
               accelerate \
               soundfile \
               librosa \
               edge-tts \
               jiwer \
               torch \
               torchaudio \
               pydub \
               scikit-learn \
               numpy \
               pandas

# Save to Drive so future sessions can reinstall quickly
!pip freeze > /content/drive/MyDrive/CSE465_Project/requirements.txt
print("All packages installed.")
print("requirements.txt saved to Drive.")


# -------------------------------------------------------------
# CELL 3: Verify GPU
# You need a T4. If you see CPU here, restart runtime.
# -------------------------------------------------------------
import torch

print(f"GPU available : {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU name      : {torch.cuda.get_device_name(0)}")
    total_mem = torch.cuda.get_device_properties(0).total_memory / 1e9
    print(f"GPU memory    : {total_mem:.1f} GB")
else:
    print("WARNING: No GPU found. Go to Runtime > Change runtime type > T4 GPU.")


# -------------------------------------------------------------
# CELL 4: Download and Save DailyDialog Dataset
# DailyDialog is text-only dialogue. We use it to train
# the turn-taking classifier (wait / respond / backchannel).
# Download once → saved to Drive → reuse every session.
# -------------------------------------------------------------
from datasets import load_dataset, load_from_disk

DATASET_PATH = f"{DRIVE_PATH}/dataset/dailydialog"

if os.path.exists(DATASET_PATH):
    print("DailyDialog already on Drive. Loading...")
    dataset = load_from_disk(DATASET_PATH)
else:
    print("Downloading DailyDialog from HuggingFace...")
    dataset = load_dataset("daily_dialog")
    dataset.save_to_disk(DATASET_PATH)
    print(f"Saved to Drive: {DATASET_PATH}")

print(f"\nTrain samples : {len(dataset['train'])}")
print(f"Test samples  : {len(dataset['test'])}")
print(f"\nSample dialog (first 3 turns):")
for i, turn in enumerate(dataset['train'][0]['dialog'][:3]):
    print(f"  Turn {i+1}: {turn}")


# -------------------------------------------------------------
# CELL 5: Create Turn-Taking Labels from DailyDialog
# 
# The paper used a 7B LLM to decide:
#   - wait         (user still speaking)
#   - respond      (user finished, system should reply)
#   - backchannel  (short acknowledgment: uh-huh, go on)
#
# We create labeled training examples by simulating these
# three situations from the text dialogues.
#
# Label mapping:
#   0 = wait
#   1 = respond
#   2 = backchannel
# -------------------------------------------------------------
import pandas as pd
import numpy as np

BACKCHANNEL_WORDS = {
    "yes", "yeah", "okay", "ok", "sure", "right",
    "i see", "go on", "uh huh", "mhm", "alright",
    "indeed", "of course", "exactly", "understood"
}

def assign_label(text):
    """
    Assign a turn-taking label to a piece of text.
    Rules are derived from the paper's special token descriptions.
    """
    text = text.strip().lower()
    words = text.split()
    word_count = len(words)

    # Rule 1: Very short utterance → likely a backchannel
    if word_count <= 3:
        if text in BACKCHANNEL_WORDS or any(b in text for b in BACKCHANNEL_WORDS):
            return 2  # backchannel

    # Rule 2: Ends with question mark or is clearly complete → respond
    if text.endswith("?") or text.endswith(".") or text.endswith("!"):
        return 1  # respond

    # Rule 3: Incomplete sentence (no terminal punctuation, > 3 words) → wait
    if word_count > 3 and not text.endswith((".", "?", "!")):
        return 0  # wait

    # Default → respond
    return 1


def build_dataset_from_dailydialog(split, max_dialogs=3000):
    """
    Build turn-taking examples from DailyDialog.
    For each dialog:
      - Full utterances → respond or backchannel
      - First half of long utterances → wait
    """
    texts  = []
    labels = []

    dialogs = dataset[split].select(range(min(max_dialogs, len(dataset[split]))))

    for dialog in dialogs:
        turns = dialog['dialog']

        for turn in turns:
            turn = turn.strip()
            if len(turn) == 0:
                continue

            words = turn.split()

            # --- Generate a WAIT example ---
            # Take only the first half of longer utterances
            if len(words) >= 6:
                partial = " ".join(words[:len(words)//2])
                texts.append(partial)
                labels.append(0)  # wait

            # --- Generate a RESPOND or BACKCHANNEL example ---
            label = assign_label(turn)
            texts.append(turn)
            labels.append(label)

    return texts, labels


print("Building training examples...")
train_texts, train_labels = build_dataset_from_dailydialog("train", max_dialogs=3000)

print("Building test examples...")
test_texts,  test_labels  = build_dataset_from_dailydialog("test",  max_dialogs=500)

# Show label distribution
from collections import Counter
label_names = {0: "wait", 1: "respond", 2: "backchannel"}

train_counts = Counter(train_labels)
print(f"\nTraining set size : {len(train_texts)}")
print("Label distribution (train):")
for k, v in sorted(train_counts.items()):
    print(f"  {label_names[k]:12s} ({k}): {v:5d} samples")

test_counts = Counter(test_labels)
print(f"\nTest set size : {len(test_texts)}")
print("Label distribution (test):")
for k, v in sorted(test_counts.items()):
    print(f"  {label_names[k]:12s} ({k}): {v:5d} samples")


# -------------------------------------------------------------
# CELL 6: Save Labeled Dataset to Drive
# This persists across sessions. Never download again.
# -------------------------------------------------------------
import json

labeled_data = {
    "train": {"texts": train_texts, "labels": train_labels},
    "test":  {"texts": test_texts,  "labels": test_labels}
}

LABELED_PATH = f"{DRIVE_PATH}/dataset/turn_taking_labeled.json"

with open(LABELED_PATH, "w") as f:
    json.dump(labeled_data, f)

print(f"Labeled dataset saved to Drive: {LABELED_PATH}")
print(f"Train: {len(train_texts)} examples")
print(f"Test:  {len(test_texts)} examples")


# -------------------------------------------------------------
# CELL 7: Baseline Turn-Taking Accuracy (BEFORE Training)
#
# Before we train the classifier, we measure how well
# a simple rule-based system performs on the test set.
# This is our BEFORE number in the before/after comparison.
# -------------------------------------------------------------
from sklearn.metrics import classification_report, accuracy_score

def rule_based_classifier(text):
    """
    Simple rule-based turn-taking. No training. No model.
    This is what any basic system would do without learning.
    """
    return assign_label(text)

rule_predictions = [rule_based_classifier(t) for t in test_texts]

baseline_accuracy = accuracy_score(test_labels, rule_predictions)

print("=" * 50)
print("BASELINE Turn-Taking (Rule-Based, BEFORE Training)")
print("=" * 50)
print(f"Accuracy: {baseline_accuracy:.4f} ({baseline_accuracy*100:.2f}%)")
print()
print(classification_report(
    test_labels,
    rule_predictions,
    target_names=["wait", "respond", "backchannel"]
))

# Save baseline result to Drive
baseline_result = {
    "method":   "rule_based",
    "accuracy": baseline_accuracy,
    "note":     "BEFORE classifier training"
}
with open(f"{DRIVE_PATH}/results/baseline_accuracy.json", "w") as f:
    json.dump(baseline_result, f, indent=2)

print("Baseline accuracy saved to Drive.")


# -------------------------------------------------------------
# CELL 8: Generate Test Audio Samples
#
# We create 6 test audio clips using edge-tts (free, no GPU).
# 3 English + 3 code-mixed English-French.
# These will be used for the full pipeline demo.
# Saved to Drive for use in all future sessions.
# -------------------------------------------------------------
import edge_tts
import asyncio

AUDIO_PATH = f"{DRIVE_PATH}/audio_samples"

# Test sentences: 3 English, 3 code-mixed English-French
test_sentences = [
    # (filename, text, voice, expected_label)
    ("en_wait.wav",        "I was thinking that maybe we could",          "en-US-JennyNeural", "wait"),
    ("en_respond.wav",     "What time does the meeting start tomorrow?",  "en-US-JennyNeural", "respond"),
    ("en_backchannel.wav", "I see.",                                      "en-US-JennyNeural", "backchannel"),
    ("fr_wait.wav",        "Je voudrais to order something but",          "fr-FR-DeniseNeural","wait"),
    ("fr_respond.wav",     "Can you tell me où est la station?",          "en-US-JennyNeural", "respond"),
    ("fr_backchannel.wav", "Oui, okay.",                                  "fr-FR-DeniseNeural","backchannel"),
]

async def generate_audio(text, voice, filepath):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filepath)

print("Generating test audio samples...")
for filename, text, voice, label in test_sentences:
    filepath = f"{AUDIO_PATH}/{filename}"
    if os.path.exists(filepath):
        print(f"  Already exists: {filename}")
    else:
        asyncio.run(generate_audio(text, voice, filepath))
        print(f"  Generated ({label}): {filename}")

print(f"\nAll audio saved to Drive: {AUDIO_PATH}")

# Save metadata
audio_meta = [
    {"file": f, "text": t, "voice": v, "expected_label": l}
    for f, t, v, l in test_sentences
]
with open(f"{DRIVE_PATH}/audio_samples/metadata.json", "w") as f:
    json.dump(audio_meta, f, indent=2)
print("Audio metadata saved.")


# -------------------------------------------------------------
# CELL 9: Load Whisper-small
# Pretrained. No fine-tuning today. Used for transcription.
# -------------------------------------------------------------
import whisper

print("Loading Whisper-small...")
whisper_model = whisper.load_model("small")
print("Whisper-small loaded.")
print(f"GPU memory used: {torch.cuda.memory_allocated()/1e9:.2f} GB")


# -------------------------------------------------------------
# CELL 10: Run Baseline Speech-to-Speech Pipeline
#
# Full pipeline:
#   Audio → Whisper (ASR) → Rule-based classifier → edge-tts
#
# This is the BEFORE pipeline (rule-based turn-taking).
# Day 2 replaces rule-based with trained DistilBERT classifier.
# -------------------------------------------------------------
import time
import numpy as np

LABEL_NAMES = {0: "wait", 1: "respond", 2: "backchannel"}

RESPONSE_TEMPLATES = {
    0: None,  # wait → system says nothing
    1: "Thank you for your message. Let me respond to that.",
    2: "Uh-huh, please go on."
}

async def tts_speak(text, voice, out_path):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(out_path)

def run_baseline_pipeline(audio_file, expected_label):
    """
    Full speech-to-speech pipeline using rule-based turn-taking.
    Returns timing info and predicted label.
    """
    print(f"\n{'='*50}")
    print(f"Input audio : {os.path.basename(audio_file)}")
    print(f"Expected    : {expected_label}")

    total_start = time.time()

    # --- Step 1: ASR (Whisper) ---
    asr_start = time.time()
    result = whisper_model.transcribe(audio_file)
    transcription = result["text"].strip()
    detected_lang = result["language"]
    asr_time = time.time() - asr_start

    print(f"Transcription : \"{transcription}\"")
    print(f"Language      : {detected_lang}")
    print(f"ASR latency   : {asr_time:.2f}s")

    # --- Step 2: Turn-taking decision (rule-based) ---
    clf_start = time.time()
    predicted_label = rule_based_classifier(transcription)
    decision = LABEL_NAMES[predicted_label]
    clf_time = time.time() - clf_start

    print(f"Decision      : {decision} (label={predicted_label})")
    print(f"Classifier    : {clf_time:.3f}s")

    # --- Step 3: TTS response ---
    tts_start = time.time()
    response_text = RESPONSE_TEMPLATES[predicted_label]

    if response_text is None:
        print("Action        : System waits (no audio output)")
        tts_time = 0.0
        output_path = None
    else:
        voice = "fr-FR-DeniseNeural" if detected_lang == "fr" else "en-US-JennyNeural"
        output_path = f"/content/output_{os.path.basename(audio_file)}"
        asyncio.run(tts_speak(response_text, voice, output_path))
        tts_time = time.time() - tts_start
        print(f"Response      : \"{response_text}\"")
        print(f"TTS latency   : {tts_time:.2f}s")

    total_time = time.time() - total_start
    print(f"Total latency : {total_time:.2f}s")
    print(f"Correct?      : {'YES' if decision == expected_label else 'NO'}")

    return {
        "file":           os.path.basename(audio_file),
        "transcription":  transcription,
        "detected_lang":  detected_lang,
        "expected":       expected_label,
        "predicted":      decision,
        "correct":        decision == expected_label,
        "asr_latency":    round(asr_time, 3),
        "clf_latency":    round(clf_time, 3),
        "tts_latency":    round(tts_time, 3),
        "total_latency":  round(total_time, 3),
    }


# --- Run pipeline on all 6 test audio files ---
print("Running baseline speech-to-speech pipeline on all test samples...")
print("(This is BEFORE classifier training)")

pipeline_results = []
for filename, text, voice, expected_label in test_sentences:
    filepath = f"{AUDIO_PATH}/{filename}"
    result = run_baseline_pipeline(filepath, expected_label)
    pipeline_results.append(result)


# -------------------------------------------------------------
# CELL 11: Save Baseline Pipeline Results
# -------------------------------------------------------------
import json

RESULTS_PATH = f"{DRIVE_PATH}/results/baseline_pipeline_results.json"
with open(RESULTS_PATH, "w") as f:
    json.dump(pipeline_results, f, indent=2)

# Summary
correct = sum(1 for r in pipeline_results if r["correct"])
total   = len(pipeline_results)
avg_lat = sum(r["total_latency"] for r in pipeline_results) / total

print("\n" + "="*50)
print("BASELINE PIPELINE SUMMARY (BEFORE Training)")
print("="*50)
print(f"Turn-taking accuracy : {correct}/{total} = {correct/total*100:.1f}%")
print(f"Avg total latency    : {avg_lat:.2f}s")
print(f"\nPer-sample results:")
print(f"{'File':<25} {'Expected':<12} {'Predicted':<12} {'Correct':<8} {'Latency'}")
print("-"*70)
for r in pipeline_results:
    print(f"{r['file']:<25} {r['expected']:<12} {r['predicted']:<12} "
          f"{'YES' if r['correct'] else 'NO':<8} {r['total_latency']:.2f}s")

print(f"\nResults saved to Drive: {RESULTS_PATH}")


# -------------------------------------------------------------
# CELL 12: Day 1 Summary — What Is Saved to Drive
# -------------------------------------------------------------
print("\n" + "="*50)
print("DAY 1 COMPLETE — Files Saved to Drive")
print("="*50)
print(f"""
{DRIVE_PATH}/
├── requirements.txt                    ← reinstall packages next session
├── dataset/
│   ├── dailydialog/                    ← raw DailyDialog dataset
│   └── turn_taking_labeled.json        ← labeled train/test examples
├── audio_samples/
│   ├── metadata.json                   ← audio file info
│   ├── en_wait.wav
│   ├── en_respond.wav
│   ├── en_backchannel.wav
│   ├── fr_wait.wav
│   ├── fr_respond.wav
│   └── fr_backchannel.wav
└── results/
    ├── baseline_accuracy.json          ← rule-based WER (BEFORE)
    └── baseline_pipeline_results.json  ← full pipeline test (BEFORE)
""")
print("Next session (Day 2): Train DistilBERT turn-taking classifier.")
print("Open a NEW notebook. Mount Drive. Load from paths above.")
