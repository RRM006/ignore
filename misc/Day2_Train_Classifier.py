# =============================================================
# CSE465 | Speech-to-Speech Project
# Day 2: Train DistilBERT Turn-Taking Classifier
# =============================================================
# BEFORE STARTING:
#   1. Runtime > Change runtime type > T4 GPU
#   2. Run Cell 1 first (Drive mount) before anything else
#   3. Day 1 must be complete (dataset must be on Drive)
# Expected total runtime: 2-3 hours
# =============================================================


# -------------------------------------------------------------
# CELL 1: Mount Drive + Reinstall Packages
# Run this FIRST. Every session must start here.
# -------------------------------------------------------------
from google.colab import drive
drive.mount('/content/drive')

import os

DRIVE_PATH = "/content/drive/MyDrive/CSE465_Project"

# Verify Day 1 files exist before proceeding
required = [
    f"{DRIVE_PATH}/dataset/turn_taking_labeled.json",
    f"{DRIVE_PATH}/results/baseline_accuracy.json",
]
for path in required:
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Missing: {path}\n"
            "Day 1 must be completed before Day 2."
        )

print("Drive mounted.")
print("Day 1 files verified.")

# Reinstall packages from saved requirements
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


# -------------------------------------------------------------
# CELL 3: Load Labeled Dataset from Drive
# Created in Day 1 Cell 6. No re-downloading needed.
# -------------------------------------------------------------
import json
import numpy as np

LABELED_PATH = f"{DRIVE_PATH}/dataset/turn_taking_labeled.json"

with open(LABELED_PATH, "r") as f:
    labeled_data = json.load(f)

train_texts  = labeled_data["train"]["texts"]
train_labels = labeled_data["train"]["labels"]
test_texts   = labeled_data["test"]["texts"]
test_labels  = labeled_data["test"]["labels"]

LABEL_NAMES = {0: "wait", 1: "respond", 2: "backchannel"}
NUM_LABELS  = 3

from collections import Counter
print(f"Train samples : {len(train_texts)}")
print(f"Test samples  : {len(test_texts)}")
print("\nLabel distribution (train):")
for k, v in sorted(Counter(train_labels).items()):
    print(f"  {LABEL_NAMES[k]:12s}: {v}")


# -------------------------------------------------------------
# CELL 4: Tokenize Dataset
# DistilBERT needs tokenized input, not raw text.
# We tokenize everything here and cache to Drive.
# -------------------------------------------------------------
from transformers import DistilBertTokenizer
from torch.utils.data import Dataset, DataLoader

TOKENIZER_NAME = "distilbert-base-uncased"
tokenizer = DistilBertTokenizer.from_pretrained(TOKENIZER_NAME)

MAX_LENGTH = 64  # Turn-taking inputs are short; 64 is enough

class TurnTakingDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.encodings = tokenizer(
            texts,
            truncation=True,
            padding=True,
            max_length=max_length,
            return_tensors="pt"
        )
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return {
            "input_ids":      self.encodings["input_ids"][idx],
            "attention_mask": self.encodings["attention_mask"][idx],
            "labels":         self.labels[idx]
        }

print("Tokenizing training set...")
train_dataset = TurnTakingDataset(
    train_texts, train_labels, tokenizer, MAX_LENGTH
)

print("Tokenizing test set...")
test_dataset = TurnTakingDataset(
    test_texts, test_labels, tokenizer, MAX_LENGTH
)

print(f"Train dataset : {len(train_dataset)} samples")
print(f"Test dataset  : {len(test_dataset)} samples")
print(f"Input shape   : {train_dataset[0]['input_ids'].shape}")


# -------------------------------------------------------------
# CELL 5: Build DataLoaders
# -------------------------------------------------------------
BATCH_SIZE = 32

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)

print(f"Batch size         : {BATCH_SIZE}")
print(f"Training batches   : {len(train_loader)}")
print(f"Test batches       : {len(test_loader)}")


# -------------------------------------------------------------
# CELL 6: Load DistilBERT for Sequence Classification
#
# DistilBERT is a smaller, faster version of BERT.
# ~66M parameters — trains easily on T4 in 30-45 minutes.
# We add a classification head on top for 3 classes:
#   0 = wait  |  1 = respond  |  2 = backchannel
# -------------------------------------------------------------
from transformers import DistilBertForSequenceClassification

CHECKPOINT_PATH = f"{DRIVE_PATH}/checkpoints"

# Check if a checkpoint already exists (resuming from yesterday)
existing_checkpoints = sorted([
    d for d in os.listdir(CHECKPOINT_PATH)
    if d.startswith("classifier_epoch")
]) if os.path.exists(CHECKPOINT_PATH) else []

if existing_checkpoints:
    latest_ckpt = f"{CHECKPOINT_PATH}/{existing_checkpoints[-1]}"
    print(f"Resuming from checkpoint: {latest_ckpt}")
    model = DistilBertForSequenceClassification.from_pretrained(
        latest_ckpt,
        num_labels=NUM_LABELS
    )
    start_epoch = int(existing_checkpoints[-1].split("epoch")[-1]) + 1
else:
    print("No checkpoint found. Starting from pretrained DistilBERT.")
    model = DistilBertForSequenceClassification.from_pretrained(
        TOKENIZER_NAME,
        num_labels=NUM_LABELS
    )
    start_epoch = 0

device = torch.device("cuda")
model = model.to(device)

total_params = sum(p.numel() for p in model.parameters())
trainable   = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"\nTotal parameters    : {total_params:,}")
print(f"Trainable parameters: {trainable:,}")
print(f"Starting from epoch : {start_epoch}")
print(f"GPU memory used     : {torch.cuda.memory_allocated()/1e9:.2f} GB")


# -------------------------------------------------------------
# CELL 7: Define Optimizer, Scheduler, Loss
# -------------------------------------------------------------
from torch.optim import AdamW
from transformers import get_linear_schedule_with_warmup

EPOCHS       = 5
LEARNING_RATE = 2e-5
WARMUP_STEPS  = 100

optimizer = AdamW(model.parameters(), lr=LEARNING_RATE, weight_decay=0.01)

total_steps = len(train_loader) * EPOCHS
scheduler = get_linear_schedule_with_warmup(
    optimizer,
    num_warmup_steps=WARMUP_STEPS,
    num_training_steps=total_steps
)

# Class weights to handle label imbalance
label_counts  = Counter(train_labels)
total_samples = len(train_labels)
class_weights = torch.tensor(
    [total_samples / (NUM_LABELS * label_counts[i]) for i in range(NUM_LABELS)],
    dtype=torch.float
).to(device)

loss_fn = torch.nn.CrossEntropyLoss(weight=class_weights)

print(f"Epochs          : {EPOCHS}")
print(f"Learning rate   : {LEARNING_RATE}")
print(f"Total steps     : {total_steps}")
print(f"Warmup steps    : {WARMUP_STEPS}")
print(f"Class weights   : {class_weights.cpu().numpy().round(3)}")


# -------------------------------------------------------------
# CELL 8: Training Loop
#
# Saves checkpoint to Drive after EVERY epoch.
# If session crashes, Day 3 (Account 2) resumes from last epoch.
# Watch the loss go down — that confirms training is working.
# -------------------------------------------------------------
from sklearn.metrics import accuracy_score
import time

def train_epoch(model, loader, optimizer, scheduler, loss_fn, device):
    model.train()
    total_loss = 0
    all_preds  = []
    all_labels = []

    for batch in loader:
        input_ids      = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels         = batch["labels"].to(device)

        optimizer.zero_grad()
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits  = outputs.logits

        loss = loss_fn(logits, labels)
        loss.backward()

        # Gradient clipping prevents exploding gradients
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        optimizer.step()
        scheduler.step()

        total_loss += loss.item()
        preds = torch.argmax(logits, dim=1).cpu().numpy()
        all_preds.extend(preds)
        all_labels.extend(labels.cpu().numpy())

    avg_loss = total_loss / len(loader)
    accuracy = accuracy_score(all_labels, all_preds)
    return avg_loss, accuracy


def evaluate(model, loader, loss_fn, device):
    model.eval()
    total_loss = 0
    all_preds  = []
    all_labels = []

    with torch.no_grad():
        for batch in loader:
            input_ids      = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels         = batch["labels"].to(device)

            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            logits  = outputs.logits

            loss = loss_fn(logits, labels)
            total_loss += loss.item()

            preds = torch.argmax(logits, dim=1).cpu().numpy()
            all_preds.extend(preds)
            all_labels.extend(labels.cpu().numpy())

    avg_loss = total_loss / len(loader)
    accuracy = accuracy_score(all_labels, all_preds)
    return avg_loss, accuracy, all_preds, all_labels


# --- Training History (for saving results) ---
history = []
best_val_accuracy = 0.0

print("=" * 60)
print("TRAINING STARTED")
print("=" * 60)
print(f"{'Epoch':<8} {'Train Loss':<12} {'Train Acc':<12} {'Val Loss':<12} {'Val Acc':<12} {'Time'}")
print("-" * 60)

for epoch in range(start_epoch, EPOCHS):
    epoch_start = time.time()

    # --- Train ---
    train_loss, train_acc = train_epoch(
        model, train_loader, optimizer, scheduler, loss_fn, device
    )

    # --- Evaluate ---
    val_loss, val_acc, val_preds, val_labels_list = evaluate(
        model, test_loader, loss_fn, device
    )

    epoch_time = time.time() - epoch_start

    print(f"Epoch {epoch+1:<3} "
          f"{train_loss:<12.4f} "
          f"{train_acc*100:<11.2f}% "
          f"{val_loss:<12.4f} "
          f"{val_acc*100:<11.2f}% "
          f"{epoch_time:.1f}s")

    # --- Save checkpoint to Drive after every epoch ---
    ckpt_dir = f"{CHECKPOINT_PATH}/classifier_epoch{epoch+1}"
    model.save_pretrained(ckpt_dir)
    tokenizer.save_pretrained(ckpt_dir)
    print(f"  Checkpoint saved: {ckpt_dir}")

    # --- Track best model ---
    if val_acc > best_val_accuracy:
        best_val_accuracy = val_acc
        best_model_dir = f"{DRIVE_PATH}/models/best_classifier"
        model.save_pretrained(best_model_dir)
        tokenizer.save_pretrained(best_model_dir)
        print(f"  Best model updated: {best_val_accuracy*100:.2f}%")

    # --- Save history entry ---
    history.append({
        "epoch":      epoch + 1,
        "train_loss": round(train_loss, 4),
        "train_acc":  round(train_acc, 4),
        "val_loss":   round(val_loss, 4),
        "val_acc":    round(val_acc, 4),
        "time_sec":   round(epoch_time, 1)
    })

    # Save history after every epoch (crash protection)
    with open(f"{DRIVE_PATH}/results/training_history.json", "w") as f:
        json.dump(history, f, indent=2)

print("\n" + "=" * 60)
print(f"TRAINING COMPLETE")
print(f"Best validation accuracy: {best_val_accuracy*100:.2f}%")
print("=" * 60)


# -------------------------------------------------------------
# CELL 9: Detailed Evaluation — AFTER Training
#
# This is your AFTER number for the before/after comparison.
# Compare this directly against Day 1 Cell 7 baseline.
# -------------------------------------------------------------
from sklearn.metrics import classification_report, confusion_matrix

# Load best model for final evaluation
best_model = DistilBertForSequenceClassification.from_pretrained(
    f"{DRIVE_PATH}/models/best_classifier",
    num_labels=NUM_LABELS
).to(device)

_, after_accuracy, after_preds, after_labels = evaluate(
    best_model, test_loader, loss_fn, device
)

# Load baseline result from Day 1
with open(f"{DRIVE_PATH}/results/baseline_accuracy.json") as f:
    baseline_result = json.load(f)

baseline_accuracy = baseline_result["accuracy"]

print("=" * 60)
print("BEFORE vs AFTER Training — Turn-Taking Classifier")
print("=" * 60)
print(f"BEFORE (rule-based) accuracy : {baseline_accuracy*100:.2f}%")
print(f"AFTER  (DistilBERT) accuracy : {after_accuracy*100:.2f}%")
improvement = (after_accuracy - baseline_accuracy) * 100
print(f"Improvement                  : +{improvement:.2f}%")

print("\nDetailed report AFTER training:")
print(classification_report(
    after_labels,
    after_preds,
    target_names=["wait", "respond", "backchannel"]
))

print("Confusion matrix (rows=actual, cols=predicted):")
cm = confusion_matrix(after_labels, after_preds)
print(f"{'':12}", end="")
for name in LABEL_NAMES.values():
    print(f"{name:>12}", end="")
print()
for i, row in enumerate(cm):
    print(f"{LABEL_NAMES[i]:12}", end="")
    for val in row:
        print(f"{val:>12}", end="")
    print()


# -------------------------------------------------------------
# CELL 10: Save After-Training Results to Drive
# -------------------------------------------------------------
after_result = {
    "method":             "distilbert_classifier",
    "accuracy":           after_accuracy,
    "baseline_accuracy":  baseline_accuracy,
    "improvement":        improvement,
    "note":               "AFTER classifier training"
}

with open(f"{DRIVE_PATH}/results/after_accuracy.json", "w") as f:
    json.dump(after_result, f, indent=2)

print(f"\nAfter-training results saved to Drive.")


# -------------------------------------------------------------
# CELL 11: Print Training History Table
# Shows loss and accuracy per epoch — include this in report.
# -------------------------------------------------------------
print("\n" + "=" * 60)
print("Training History")
print("=" * 60)
print(f"{'Epoch':<8} {'Train Loss':<12} {'Train Acc':<12} {'Val Loss':<12} {'Val Acc'}")
print("-" * 55)
for h in history:
    print(f"{h['epoch']:<8} "
          f"{h['train_loss']:<12} "
          f"{h['train_acc']*100:<11.2f}% "
          f"{h['val_loss']:<12} "
          f"{h['val_acc']*100:.2f}%")


# -------------------------------------------------------------
# CELL 12: Quick Inference Test
# Test the trained classifier on 6 manual sentences.
# Confirms the model works before Day 3 pipeline integration.
# -------------------------------------------------------------
def predict_turn_taking(text, model, tokenizer, device):
    model.eval()
    encoding = tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=64,
        return_tensors="pt"
    )
    input_ids      = encoding["input_ids"].to(device)
    attention_mask = encoding["attention_mask"].to(device)

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits  = outputs.logits
        probs   = torch.softmax(logits, dim=1).cpu().numpy()[0]
        pred    = torch.argmax(logits, dim=1).item()

    return LABEL_NAMES[pred], probs


test_cases = [
    # (text, expected_label)
    ("I was thinking that maybe we could",          "wait"),
    ("What time does the meeting start tomorrow?",  "respond"),
    ("I see.",                                      "backchannel"),
    ("Je voudrais to order something but",          "wait"),
    ("Can you tell me où est la station?",          "respond"),
    ("Oui, okay.",                                  "backchannel"),
]

print("\n" + "=" * 60)
print("Inference Test — Trained Classifier")
print("=" * 60)
print(f"{'Text':<45} {'Expected':<14} {'Predicted':<14} {'Correct'}")
print("-" * 80)

correct_count = 0
for text, expected in test_cases:
    predicted, probs = predict_turn_taking(text, best_model, tokenizer, device)
    correct = predicted == expected
    if correct:
        correct_count += 1
    short_text = text[:43] + ".." if len(text) > 43 else text
    print(f"{short_text:<45} {expected:<14} {predicted:<14} {'YES' if correct else 'NO'}")

print(f"\nInference accuracy: {correct_count}/{len(test_cases)}")


# -------------------------------------------------------------
# CELL 13: Day 2 Summary — What Is Saved to Drive
# -------------------------------------------------------------
print("\n" + "=" * 60)
print("DAY 2 COMPLETE — Files Saved to Drive")
print("=" * 60)
print(f"""
{DRIVE_PATH}/
├── checkpoints/
│   ├── classifier_epoch1/     ← checkpoint after epoch 1
│   ├── classifier_epoch2/     ← checkpoint after epoch 2
│   ├── classifier_epoch3/     ← checkpoint after epoch 3
│   ├── classifier_epoch4/     ← checkpoint after epoch 4
│   └── classifier_epoch5/     ← checkpoint after epoch 5
├── models/
│   └── best_classifier/       ← best model (use this in Day 3)
└── results/
    ├── training_history.json  ← loss + accuracy per epoch
    └── after_accuracy.json    ← AFTER number for comparison
""")

print("KEY RESULTS FOR YOUR REPORT:")
print(f"  BEFORE accuracy (rule-based) : {baseline_accuracy*100:.2f}%")
print(f"  AFTER  accuracy (DistilBERT) : {after_accuracy*100:.2f}%")
print(f"  Improvement                  : +{improvement:.2f}%")
print()
print("Next (Day 3): Plug trained classifier into full S2S pipeline.")
print("Resume in same account OR Account 2 using checkpoint files.")
