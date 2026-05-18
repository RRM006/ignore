# =============================================================
# CSE465 | Speech-to-Speech Project
# Day 4: Deep Analysis + Visualization + Error Analysis
# =============================================================
# BEFORE STARTING:
#   1. Runtime > Change runtime type > T4 GPU
#   2. Run Cell 1 first (Drive mount)
#   3. Days 1, 2, 3 must be complete
#   4. Drive must contain:
#      - results/complete_comparison.json
#      - results/training_history.json
#      - results/baseline_pipeline_results.json
#      - results/after_pipeline_results.json
#      - models/best_classifier/
# Expected total runtime: 2-3 hours
# =============================================================


# -------------------------------------------------------------
# CELL 1: Mount Drive + Verify All Files
# -------------------------------------------------------------
from google.colab import drive
drive.mount('/content/drive')

import os

DRIVE_PATH = "/content/drive/MyDrive/CSE465_Project"

required_files = [
    f"{DRIVE_PATH}/results/complete_comparison.json",
    f"{DRIVE_PATH}/results/training_history.json",
    f"{DRIVE_PATH}/results/baseline_pipeline_results.json",
    f"{DRIVE_PATH}/results/after_pipeline_results.json",
    f"{DRIVE_PATH}/results/baseline_accuracy.json",
    f"{DRIVE_PATH}/results/after_accuracy.json",
    f"{DRIVE_PATH}/models/best_classifier/config.json",
    f"{DRIVE_PATH}/dataset/turn_taking_labeled.json",
]

print("Verifying required files from Days 1-3...")
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
        "Complete Days 1-3 before running Day 4."
    )

print("\nAll files verified.")

!pip install -q -r /content/drive/MyDrive/CSE465_Project/requirements.txt
!pip install -q matplotlib seaborn
print("Packages ready.")


# -------------------------------------------------------------
# CELL 2: Load All Results
# -------------------------------------------------------------
import json
import numpy as np

# Load all result files
with open(f"{DRIVE_PATH}/results/complete_comparison.json") as f:
    comparison = json.load(f)

with open(f"{DRIVE_PATH}/results/training_history.json") as f:
    history = json.load(f)

with open(f"{DRIVE_PATH}/results/baseline_pipeline_results.json") as f:
    before_results = json.load(f)

with open(f"{DRIVE_PATH}/results/after_pipeline_results.json") as f:
    after_results = json.load(f)

with open(f"{DRIVE_PATH}/results/baseline_accuracy.json") as f:
    baseline_acc = json.load(f)

with open(f"{DRIVE_PATH}/results/after_accuracy.json") as f:
    after_acc = json.load(f)

with open(f"{DRIVE_PATH}/dataset/turn_taking_labeled.json") as f:
    labeled_data = json.load(f)

LABEL_NAMES = {0: "wait", 1: "respond", 2: "backchannel"}

print("All results loaded successfully.")
print(f"Training epochs recorded : {len(history)}")
print(f"Before pipeline samples  : {len(before_results)}")
print(f"After pipeline samples   : {len(after_results)}")


# -------------------------------------------------------------
# CELL 3: Plot 1 — Training Loss and Accuracy Curve
# Shows the classifier learning over 5 epochs.
# Save to Drive for report.
# -------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.dpi'] = 120

PLOTS_PATH = f"{DRIVE_PATH}/results/plots"
os.makedirs(PLOTS_PATH, exist_ok=True)

epochs      = [h["epoch"]      for h in history]
train_loss  = [h["train_loss"] for h in history]
val_loss    = [h["val_loss"]   for h in history]
train_acc   = [h["train_acc"]  * 100 for h in history]
val_acc     = [h["val_acc"]    * 100 for h in history]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Loss curve
axes[0].plot(epochs, train_loss, "b-o", label="Train Loss", linewidth=2)
axes[0].plot(epochs, val_loss,   "r-o", label="Val Loss",   linewidth=2)
axes[0].set_title("Training & Validation Loss", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Loss")
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[0].set_xticks(epochs)

# Accuracy curve
axes[1].plot(epochs, train_acc, "b-o", label="Train Accuracy", linewidth=2)
axes[1].plot(epochs, val_acc,   "r-o", label="Val Accuracy",   linewidth=2)
axes[1].axhline(
    y=baseline_acc["accuracy"] * 100,
    color="gray", linestyle="--", linewidth=1.5,
    label=f"Rule-based baseline ({baseline_acc['accuracy']*100:.1f}%)"
)
axes[1].set_title("Training & Validation Accuracy", fontsize=13, fontweight="bold")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Accuracy (%)")
axes[1].legend()
axes[1].grid(True, alpha=0.3)
axes[1].set_xticks(epochs)
axes[1].set_ylim([0, 100])

plt.tight_layout()
plot_path = f"{PLOTS_PATH}/training_curves.png"
plt.savefig(plot_path, bbox_inches="tight")
plt.show()
print(f"Saved: {plot_path}")


# -------------------------------------------------------------
# CELL 4: Plot 2 — Before vs After Turn-Taking Accuracy
# Simple bar chart. Clear and easy to put in report.
# -------------------------------------------------------------
import seaborn as sns

before_pipeline_acc = comparison["pipeline_comparison"]["before"]["accuracy"] * 100
after_pipeline_acc  = comparison["pipeline_comparison"]["after"]["accuracy"]  * 100
before_clf_acc      = baseline_acc["accuracy"] * 100
after_clf_acc       = after_acc["accuracy"]    * 100

fig, axes = plt.subplots(1, 2, figsize=(11, 5))

# Pipeline accuracy
categories = ["BEFORE\n(Rule-Based)", "AFTER\n(DistilBERT)"]
values     = [before_pipeline_acc, after_pipeline_acc]
colors     = ["#e74c3c", "#2ecc71"]

bars = axes[0].bar(categories, values, color=colors, width=0.45, edgecolor="black")
axes[0].set_title("Pipeline Turn-Taking Accuracy\n(6 Audio Samples)",
                  fontsize=12, fontweight="bold")
axes[0].set_ylabel("Accuracy (%)")
axes[0].set_ylim([0, 110])
axes[0].grid(True, alpha=0.3, axis="y")
for bar, val in zip(bars, values):
    axes[0].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        f"{val:.1f}%", ha="center", fontsize=12, fontweight="bold"
    )

# Classifier accuracy
values2 = [before_clf_acc, after_clf_acc]
bars2   = axes[1].bar(categories, values2, color=colors, width=0.45, edgecolor="black")
axes[1].set_title("Classifier Turn-Taking Accuracy\n(Test Set)",
                  fontsize=12, fontweight="bold")
axes[1].set_ylabel("Accuracy (%)")
axes[1].set_ylim([0, 110])
axes[1].grid(True, alpha=0.3, axis="y")
for bar, val in zip(bars2, values2):
    axes[1].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        f"{val:.1f}%", ha="center", fontsize=12, fontweight="bold"
    )

plt.tight_layout()
plot_path = f"{PLOTS_PATH}/before_after_accuracy.png"
plt.savefig(plot_path, bbox_inches="tight")
plt.show()
print(f"Saved: {plot_path}")


# -------------------------------------------------------------
# CELL 5: Plot 3 — Latency Breakdown (Stacked Bar)
# Shows where time is spent: ASR / CLF / LLM / TTS
# -------------------------------------------------------------
before_s = comparison["pipeline_comparison"]["before"]
after_s  = comparison["pipeline_comparison"]["after"]

labels    = ["BEFORE\n(Rule-Based)", "AFTER\n(DistilBERT)"]
asr_vals  = [before_s["avg_asr"],   after_s["avg_asr"]]
clf_vals  = [before_s["avg_clf"],   after_s["avg_clf"]]
llm_vals  = [before_s["avg_llm"],   after_s["avg_llm"]]
tts_vals  = [before_s["avg_tts"],   after_s["avg_tts"]]

x    = np.arange(len(labels))
w    = 0.45
fig, ax = plt.subplots(figsize=(8, 5))

p1 = ax.bar(x, asr_vals, w, label="ASR (Whisper)",     color="#3498db", edgecolor="black")
p2 = ax.bar(x, clf_vals, w, label="Classifier",         color="#e67e22", edgecolor="black",
            bottom=np.array(asr_vals))
p3 = ax.bar(x, llm_vals, w, label="LLM (Phi-3-mini)",  color="#9b59b6", edgecolor="black",
            bottom=np.array(asr_vals) + np.array(clf_vals))
p4 = ax.bar(x, tts_vals, w, label="TTS (edge-tts)",    color="#2ecc71", edgecolor="black",
            bottom=np.array(asr_vals) + np.array(clf_vals) + np.array(llm_vals))

# Paper latency reference line
ax.axhline(y=1.70, color="red", linestyle="--", linewidth=2,
           label="Paper latency ~1.70s (8x H100)")

ax.set_title("Average Latency Breakdown\nBefore vs After Training",
             fontsize=12, fontweight="bold")
ax.set_ylabel("Latency (seconds)")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc="upper right", fontsize=9)
ax.grid(True, alpha=0.3, axis="y")

# Total latency labels
for i, (b, a) in enumerate(zip(
    [before_s["avg_total"]], [after_s["avg_total"]]
)):
    pass

totals = [before_s["avg_total"], after_s["avg_total"]]
for xi, total in zip(x, totals):
    ax.text(xi, total + 0.05, f"{total:.2f}s",
            ha="center", fontsize=11, fontweight="bold")

plt.tight_layout()
plot_path = f"{PLOTS_PATH}/latency_breakdown.png"
plt.savefig(plot_path, bbox_inches="tight")
plt.show()
print(f"Saved: {plot_path}")


# -------------------------------------------------------------
# CELL 6: Plot 4 — Confusion Matrix (After Training)
# Shows which labels the classifier confuses most.
# -------------------------------------------------------------
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
from sklearn.metrics import confusion_matrix
import seaborn as sns

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load classifier
classifier = DistilBertForSequenceClassification.from_pretrained(
    f"{DRIVE_PATH}/models/best_classifier", num_labels=3
).to(device)
classifier.eval()

clf_tokenizer = DistilBertTokenizer.from_pretrained(
    f"{DRIVE_PATH}/models/best_classifier"
)

# Run on test set
test_texts  = labeled_data["test"]["texts"]
test_labels = labeled_data["test"]["labels"]

print(f"Running classifier on {len(test_texts)} test samples...")

all_preds = []
BATCH = 64
for i in range(0, len(test_texts), BATCH):
    batch_texts = test_texts[i:i+BATCH]
    enc = clf_tokenizer(
        batch_texts, truncation=True, padding=True,
        max_length=64, return_tensors="pt"
    )
    enc = {k: v.to(device) for k, v in enc.items()}
    with torch.no_grad():
        logits = classifier(**enc).logits
    preds = torch.argmax(logits, dim=1).cpu().numpy()
    all_preds.extend(preds)
    if i % 500 == 0:
        print(f"  Processed {i}/{len(test_texts)}")

cm = confusion_matrix(test_labels, all_preds)
class_names = ["wait", "respond", "backchannel"]

fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(
    cm, annot=True, fmt="d", cmap="Blues",
    xticklabels=class_names,
    yticklabels=class_names,
    ax=ax, linewidths=0.5
)
ax.set_title("Confusion Matrix — After Training\n(rows=actual, cols=predicted)",
             fontsize=12, fontweight="bold")
ax.set_xlabel("Predicted Label", fontsize=11)
ax.set_ylabel("Actual Label",    fontsize=11)

plt.tight_layout()
plot_path = f"{PLOTS_PATH}/confusion_matrix.png"
plt.savefig(plot_path, bbox_inches="tight")
plt.show()
print(f"Saved: {plot_path}")


# -------------------------------------------------------------
# CELL 7: Plot 5 — Label Distribution in Dataset
# Shows balance of wait/respond/backchannel in training data.
# Justifies use of class-weighted loss in Day 2.
# -------------------------------------------------------------
from collections import Counter

train_labels = labeled_data["train"]["labels"]
label_counts = Counter(train_labels)

fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(
    [class_names[i] for i in sorted(label_counts)],
    [label_counts[i] for i in sorted(label_counts)],
    color=["#3498db", "#e74c3c", "#2ecc71"],
    edgecolor="black", width=0.5
)
ax.set_title("Training Data Label Distribution",
             fontsize=12, fontweight="bold")
ax.set_ylabel("Number of Samples")
ax.grid(True, alpha=0.3, axis="y")
for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 30,
        f"{int(bar.get_height()):,}",
        ha="center", fontsize=11
    )
plt.tight_layout()
plot_path = f"{PLOTS_PATH}/label_distribution.png"
plt.savefig(plot_path, bbox_inches="tight")
plt.show()
print(f"Saved: {plot_path}")


# -------------------------------------------------------------
# CELL 8: Plot 6 — System Architecture Diagram
# Visual overview of your pipeline vs the paper's pipeline.
# -------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 4))

# --- Paper Pipeline ---
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")
ax.set_title("DuplexCascade (Paper)", fontsize=12, fontweight="bold")

boxes_paper = [
    (0.3, 1.0, "User\nSpeech",    "#aed6f1"),
    (2.0, 1.0, "DSM-ASR\n(Proprietary)", "#f1948a"),
    (4.1, 1.0, "Qwen2-7B\n+LoRA\n8xH100", "#f9e79f"),
    (6.5, 1.0, "DSM-TTS\n(Proprietary)", "#f1948a"),
    (8.5, 1.0, "System\nSpeech",  "#a9dfbf"),
]
for x, y, label, color in boxes_paper:
    ax.add_patch(plt.Rectangle((x, y), 1.5, 0.9,
                 facecolor=color, edgecolor="black", linewidth=1.2))
    ax.text(x + 0.75, y + 0.45, label,
            ha="center", va="center", fontsize=7.5, fontweight="bold")

for i in range(len(boxes_paper) - 1):
    x1 = boxes_paper[i][0]   + 1.5
    x2 = boxes_paper[i+1][0]
    ax.annotate("", xy=(x2, 1.45), xytext=(x1, 1.45),
                arrowprops=dict(arrowstyle="->", lw=1.5))

# --- Our Pipeline ---
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")
ax.set_title("Our System (CSE465)", fontsize=12, fontweight="bold")

boxes_ours = [
    (0.3, 1.0, "User\nSpeech",      "#aed6f1"),
    (2.0, 1.0, "Whisper-small\n(Open-source)", "#a9dfbf"),
    (4.0, 1.0, "DistilBERT\nClassifier\n(Trained)", "#a9dfbf"),
    (6.2, 1.0, "Phi-3-mini\n4-bit\n(Open-source)", "#a9dfbf"),
    (8.3, 1.0, "edge-tts\n(Free)",  "#a9dfbf"),
]
for x, y, label, color in boxes_ours:
    ax.add_patch(plt.Rectangle((x, y), 1.7, 0.9,
                 facecolor=color, edgecolor="black", linewidth=1.2))
    ax.text(x + 0.85, y + 0.45, label,
            ha="center", va="center", fontsize=7.5, fontweight="bold")

for i in range(len(boxes_ours) - 1):
    x1 = boxes_ours[i][0]   + 1.7
    x2 = boxes_ours[i+1][0]
    ax.annotate("", xy=(x2, 1.45), xytext=(x1, 1.45),
                arrowprops=dict(arrowstyle="->", lw=1.5))

# System speech label
ax.text(9.15 + 0.5, 1.45, "System\nSpeech",
        ha="center", va="center", fontsize=7.5, fontweight="bold",
        bbox=dict(facecolor="#aed6f1", edgecolor="black", boxstyle="round,pad=0.3"))

ax.annotate("", xy=(9.5, 1.45), xytext=(9.15 + 1.7/2 + 0.35, 1.45),
            arrowprops=dict(arrowstyle="->", lw=1.5))

plt.tight_layout()
plot_path = f"{PLOTS_PATH}/architecture_comparison.png"
plt.savefig(plot_path, bbox_inches="tight")
plt.show()
print(f"Saved: {plot_path}")


# -------------------------------------------------------------
# CELL 9: Error Analysis
# Which samples did the pipeline get wrong?
# What caused the error?
# -------------------------------------------------------------
print("=" * 60)
print("ERROR ANALYSIS — After Pipeline")
print("=" * 60)

errors = [r for r in after_results if not r["correct"]]
correct = [r for r in after_results if r["correct"]]

print(f"Correct predictions : {len(correct)}/{len(after_results)}")
print(f"Wrong  predictions  : {len(errors)}/{len(after_results)}")

if errors:
    print("\nMisclassified samples:")
    print(f"{'File':<25} {'Expected':<14} {'Predicted':<14} {'Confidence'}")
    print("-" * 75)
    for e in errors:
        conf_str = " | ".join(
            f"{k}:{v}" for k, v in e.get("confidence", {}).items()
        )
        print(f"{e['input_file']:<25} "
              f"{e['expected_label']:<14} "
              f"{e['decision']:<14} "
              f"{conf_str}")
    print()
    print("Possible reasons for errors:")
    print("  1. Code-mixed audio may confuse language detection")
    print("  2. Short audio clips may not give enough context")
    print("  3. Training data (DailyDialog) is text-only;")
    print("     acoustic features are not captured")
else:
    print("\nAll samples correctly classified.")

# Language detection analysis
print("\nLanguage Detection Results:")
print(f"{'File':<25} {'Expected Lang':<15} {'Detected Lang':<15} {'Correct?'}")
print("-" * 60)
lang_map = {"en_": "en", "fr_": "fr"}
for r in after_results:
    expected_lang = "fr" if r["input_file"].startswith("fr") else "en"
    detected_lang = r.get("detected_lang", "?")
    correct_lang  = expected_lang == detected_lang
    print(f"{r['input_file']:<25} {expected_lang:<15} {detected_lang:<15} "
          f"{'YES' if correct_lang else 'NO'}")


# -------------------------------------------------------------
# CELL 10: Confidence Score Analysis
# Shows how confident the classifier is per label.
# Low confidence = uncertain decision → worth noting in report.
# -------------------------------------------------------------
print("\n" + "=" * 60)
print("CONFIDENCE SCORE ANALYSIS")
print("=" * 60)

print(f"\n{'File':<25} {'Decision':<14} {'Wait':>8} {'Respond':>10} {'Backchannel':>13}")
print("-" * 70)

for r in after_results:
    conf = r.get("confidence", {})
    w    = conf.get("wait",        0)
    res  = conf.get("respond",     0)
    bc   = conf.get("backchannel", 0)
    print(f"{r['input_file']:<25} {r['decision']:<14} "
          f"{w:>8.3f} {res:>10.3f} {bc:>13.3f}")

# Average confidence per decision type
decisions = list(set(r["decision"] for r in after_results))
print("\nAverage confidence by decision type:")
for dec in decisions:
    dec_results = [r for r in after_results if r["decision"] == dec]
    avg_conf = sum(r["confidence"].get(dec, 0) for r in dec_results) / len(dec_results)
    print(f"  {dec:<14}: {avg_conf:.3f}")


# -------------------------------------------------------------
# CELL 11: Latency Analysis Per Sample
# Shows which component causes the most delay.
# -------------------------------------------------------------
print("\n" + "=" * 65)
print("LATENCY ANALYSIS PER SAMPLE (AFTER Training)")
print("=" * 65)
print(f"{'File':<25} {'ASR':>8} {'CLF':>8} {'LLM':>8} {'TTS':>8} {'Total':>8}")
print("-" * 65)

for r in after_results:
    print(f"{r['input_file']:<25} "
          f"{r['asr_latency']:>8.3f} "
          f"{r['clf_latency']:>8.3f} "
          f"{r.get('llm_latency', 0):>8.3f} "
          f"{r['tts_latency']:>8.3f} "
          f"{r['total_latency']:>8.3f}")

avgs = {
    "ASR":   sum(r["asr_latency"]             for r in after_results) / len(after_results),
    "CLF":   sum(r["clf_latency"]             for r in after_results) / len(after_results),
    "LLM":   sum(r.get("llm_latency", 0)      for r in after_results) / len(after_results),
    "TTS":   sum(r["tts_latency"]             for r in after_results) / len(after_results),
    "Total": sum(r["total_latency"]           for r in after_results) / len(after_results),
}
print("-" * 65)
print(f"{'AVERAGE':<25} "
      f"{avgs['ASR']:>8.3f} "
      f"{avgs['CLF']:>8.3f} "
      f"{avgs['LLM']:>8.3f} "
      f"{avgs['TTS']:>8.3f} "
      f"{avgs['Total']:>8.3f}")

dominant = max(avgs, key=lambda k: avgs[k] if k != "Total" else 0)
print(f"\nDominant latency component: {dominant} ({avgs[dominant]:.3f}s)")
print("Note: Paper reported ~1.70s on 8x H100.")
print(f"      Your system achieved {avgs['Total']:.2f}s on 1x T4 (free Colab).")


# -------------------------------------------------------------
# CELL 12: Save All Plots List to Drive
# -------------------------------------------------------------
plots = [f for f in os.listdir(PLOTS_PATH) if f.endswith(".png")]
plots_manifest = {
    "plots_path": PLOTS_PATH,
    "files":      sorted(plots),
    "descriptions": {
        "training_curves.png":        "Training loss and accuracy per epoch",
        "before_after_accuracy.png":  "Before vs After turn-taking accuracy",
        "latency_breakdown.png":      "Latency breakdown by component",
        "confusion_matrix.png":       "Confusion matrix after training",
        "label_distribution.png":     "Training data label distribution",
        "architecture_comparison.png":"Pipeline architecture comparison"
    }
}

with open(f"{DRIVE_PATH}/results/plots_manifest.json", "w") as f:
    json.dump(plots_manifest, f, indent=2)

print("\n" + "=" * 50)
print("DAY 4 COMPLETE — Plots Saved to Drive")
print("=" * 50)
print(f"\n{PLOTS_PATH}/")
for p in sorted(plots):
    desc = plots_manifest["descriptions"].get(p, "")
    print(f"  {p:<40} ← {desc}")

print(f"\nTotal plots generated: {len(plots)}")
print("\nDay 5: Generate final report document.")
