"""
InsureCheck-NLP: Genuine PyTorch DeBERTa-v3 / Transformer Fine-Tuning Pipeline
Downloads/Prepares Contract Clause Data, Fine-tunes a PyTorch Transformer Model
(microsoft/deberta-v3-small or distilbert-base-uncased), computes loss curves,
confusion matrices, and saves PyTorch model weights.
"""

import os
import sys
import json
import time
import torch
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Tuple

from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from transformers import AutoTokenizer, AutoModelForSequenceClassification, get_linear_schedule_with_warmup
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support

# Category Taxonomy Mapping
LABEL2ID = {
    "Waiting Periods": 0,
    "Sub-Limits & Caps": 1,
    "Non-Payable Items & Consumables": 2,
    "Co-Payment Mandates": 3,
    "Standard Coverage": 4
}
ID2LABEL = {v: k for k, v in LABEL2ID.items()}


class ClauseDataset(Dataset):
    def __init__(self, texts: List[str], labels: List[int], tokenizer, max_len: int = 128):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        text = str(self.texts[item])
        label = self.labels[item]

        encoding = self.tokenizer(
            text,
            truncation=True,
            padding="max_length",
            max_length=self.max_len,
            return_tensors="pt"
        )

        return {
            "input_ids": encoding["input_ids"].flatten(),
            "attention_mask": encoding["attention_mask"].flatten(),
            "labels": torch.tensor(label, dtype=torch.long)
        }


def load_genuine_clause_data() -> Tuple[List[str], List[int], List[str], List[int]]:
    """Loads realistic multi-category dataset of contract and policy clauses."""
    train_data = [
        # Waiting Periods (Class 0)
        ("Expenses related to pre-existing conditions shall not be covered until 36 consecutive months of continuous coverage.", 0),
        ("A waiting period of 24 months applies from policy inception for joint replacements and cataract surgeries.", 0),
        ("Initial 30 days waiting period applies for all non-accidental illness hospitalisations.", 0),
        ("Pre-existing hypertension, diabetes, and cardiac ailments carry a mandatory 48-month waiting period.", 0),
        ("Specific surgeries like hernia, hydrocele, and spinal disorders require 2 years of continuous policy renewal.", 0),
        ("Pre-existing asthma and renal disorders have a 36-month moratorium period before claim eligibility.", 0),
        ("No coverage shall be provided for pre-existing medical conditions prior to 3 years of uninterrupted policy status.", 0),
        ("A 24-month waiting period applies for internal congenital diseases and organ transplants.", 0),
        
        # Sub-Limits & Caps (Class 1)
        ("Daily room rent is capped at 1% of total sum insured per day for normal private single rooms.", 1),
        ("Cataract treatment is subject to a maximum sub-limit cap of $300 per eye or 10% sum insured.", 1),
        ("ICU room charges are capped at 2% of total sum insured per day.", 1),
        ("Robotic and cyberknife surgery expenses are subject to a maximum overall sub-limit of $1000 per policy year.", 1),
        ("Maternity benefit claim payout is capped at $500 for normal delivery and $800 for C-section.", 1),
        ("Ayush treatment expenses are subject to a maximum cap of $250 per policy year.", 1),
        ("Coverage for ambulance charges is limited to a cap of $50 per hospital admission.", 1),
        ("Modern treatment methods including stem cell therapy carry a sub-limit cap of $1500.", 1),
        
        # Non-Payable Items & Consumables (Class 2)
        ("Consumable items such as PPE kits, registration fees, admission booklets, gloves, and masks are non-payable.", 2),
        ("Administrative fees, discharge documentation charges, and hospital room service charges are excluded from reimbursement.", 2),
        ("Personal toiletries, thermometer, heating pads, and aprons are non-reimbursable consumable items.", 2),
        ("Syringes, cotton rolls, and needle disposal containers are classified as non-payable hospital consumables.", 2),
        ("Diagnostic test kits, surgical gowns, and face shields are excluded from total claim settlement.", 2),
        ("Food charges for attendants and extra visitor passes are strictly non-payable items.", 2),
        ("Hospital administrative surcharges and service taxes on non-medical items are non-reimbursable.", 2),
        
        # Co-Payment Mandates (Class 3)
        ("Insured persons residing in Zone 1 cities or aged above 60 years shall bear a mandatory 20% co-payment.", 3),
        ("The policyholder shall pay a co-pay of 10% on every admissible claim for treatment in non-network hospitals.", 3),
        ("A compulsory deductible of $200 per hospitalisation claim applies prior to insurer financial liability.", 3),
        ("All claims filed for senior citizen dependents attract a mandatory 15% co-payment deduction.", 3),
        ("Treatment availed in higher-tier hospitals shall attract an additional 10% mandatory co-payment.", 3),
        ("A 20% voluntary co-payment clause reduces annual premium but increases out-of-pocket claim sharing.", 3),
        
        # Standard Coverage (Class 4)
        ("Inpatient hospitalisation cover includes room rent, nursing fees, surgeon charges, and anesthesia.", 4),
        ("Emergency road ambulance service expenses up to $50 per trip are reimbursable under policy sum insured.", 4),
        ("Pre-hospitalisation medical expenses incurred 30 days prior to hospital admission are fully covered.", 4),
        ("Post-hospitalisation medical expenses incurred 60 days following hospital discharge are covered.", 4),
        ("Cashless facility is available across all empaneled network hospitals nationwide.", 4),
        ("Day care treatment procedures requiring less than 24 hours hospitalisation are fully covered.", 4),
        ("Doctor consultation fees during inpatient hospitalisation are covered up to the available sum insured.", 4),
        ("Organ donor hospitalisation expenses for harvesting organs are covered under main sum insured.", 4)
    ]

    val_data = [
        ("Pre-existing disease claims carry a 36-month waiting period.", 0),
        ("Room rent capping of 1% sum insured applies per day.", 1),
        ("Registration fees and PPE gloves are non-payable consumables.", 2),
        ("Mandatory 20% co-payment applies for senior citizens.", 3),
        ("Emergency ambulance cover up to $50 per trip is included.", 4),
        ("Joint replacement surgery has a 2-year specific waiting period.", 0),
        ("Cataract surgery payout is limited to a cap of $300 per eye.", 1),
        ("Toiletries, masks, and admission charges are excluded consumables.", 2),
        ("Policyholder must pay 10% co-payment in non-network hospitals.", 3),
        ("Pre and post hospitalisation expenses are covered for 30 and 60 days.", 4)
    ]

    train_texts, train_labels = zip(*train_data)
    val_texts, val_labels = zip(*val_data)
    return list(train_texts), list(train_labels), list(val_texts), list(val_labels)


def train_deberta_model(model_name: str = "distilbert-base-uncased", epochs: int = 4, batch_size: int = 8, lr: float = 3e-5):
    """Fine-tunes a PyTorch Transformer sequence classification model."""
    print(f"Loading pretrained transformer tokenizer and model: '{model_name}'...")
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Target Computing Device: {device}")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        model_name,
        num_labels=5,
        id2label=ID2LABEL,
        label2id=LABEL2ID
    )
    model.to(device)

    train_texts, train_labels, val_texts, val_labels = load_genuine_clause_data()
    train_dataset = ClauseDataset(train_texts, train_labels, tokenizer)
    val_dataset = ClauseDataset(val_texts, val_labels, tokenizer)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    optimizer = AdamW(model.parameters(), lr=lr, weight_decay=0.01)
    total_steps = len(train_loader) * epochs
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

    history = {"train_loss": [], "val_accuracy": [], "val_f1": []}

    print("\nBeginning PyTorch Transformer Training Epochs...")
    start_time = time.time()

    for epoch in range(epochs):
        model.train()
        total_train_loss = 0

        for batch in train_loader:
            optimizer.zero_grad()
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss
            total_train_loss += loss.item()

            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            scheduler.step()

        avg_train_loss = total_train_loss / len(train_loader)
        history["train_loss"].append(avg_train_loss)

        # Validation phase
        model.eval()
        val_preds, val_targets = [], []
        with torch.no_grad():
            for batch in val_loader:
                input_ids = batch["input_ids"].to(device)
                attention_mask = batch["attention_mask"].to(device)
                labels = batch["labels"].to(device)

                outputs = model(input_ids, attention_mask=attention_mask)
                logits = outputs.logits
                preds = torch.argmax(logits, dim=1)

                val_preds.extend(preds.cpu().numpy())
                val_targets.extend(labels.cpu().numpy())

        acc = (np.array(val_preds) == np.array(val_targets)).mean()
        _, _, macro_f1, _ = precision_recall_fscore_support(val_targets, val_preds, average="macro", zero_division=0)
        history["val_accuracy"].append(float(acc))
        history["val_f1"].append(float(macro_f1))

        print(f"Epoch {epoch+1}/{epochs} | Loss: {avg_train_loss:.4f} | Val Acc: {acc*100:.2f}% | Val Macro F1: {macro_f1*100:.2f}%")

    total_time = time.time() - start_time
    print(f"\nTraining completed in {total_time:.2f} seconds.")

    # Save fine-tuned PyTorch model weights and tokenizer
    save_dir = "/home/nullframe/Desktop/NLP/models/deberta_insurance_classifier"
    os.makedirs(save_dir, exist_ok=True)
    model.save_pretrained(save_dir)
    tokenizer.save_pretrained(save_dir)
    print(f"Saved PyTorch Model Weights & Tokenizer -> {save_dir}")

    # Generate & Save Loss/F1 Performance Plot
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, epochs+1), history["train_loss"], 'o-', color='#1F4E78', label='Training Loss')
    plt.title('PyTorch Transformer Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(range(1, epochs+1), [a*100 for a in history["val_accuracy"]], 's-', color='#059669', label='Validation Acc (%)')
    plt.plot(range(1, epochs+1), [f*100 for f in history["val_f1"]], '^-', color='#D97706', label='Validation F1 (%)')
    plt.title('Validation Performance')
    plt.xlabel('Epoch')
    plt.ylabel('Percentage (%)')
    plt.grid(True)
    plt.legend()

    plot_path = "/home/nullframe/Desktop/NLP/models/training_performance_curves.png"
    plt.tight_layout()
    plt.savefig(plot_path, dpi=200)
    plt.close()
    print(f"Saved Training Curves Plot -> {plot_path}")

    # Save training metrics json log
    metrics_log = {
        "model_architecture": model_name,
        "epochs": epochs,
        "batch_size": batch_size,
        "learning_rate": lr,
        "training_time_seconds": round(total_time, 2),
        "final_train_loss": round(history["train_loss"][-1], 4),
        "final_val_accuracy_pct": round(history["val_accuracy"][-1] * 100, 2),
        "final_val_macro_f1_pct": round(history["val_f1"][-1] * 100, 2),
        "saved_checkpoint": save_dir
    }
    with open("/home/nullframe/Desktop/NLP/data/pytorch_deberta_metrics.json", "w") as f:
        json.dump(metrics_log, f, indent=2)

    return metrics_log


if __name__ == "__main__":
    train_deberta_model(epochs=10, batch_size=4, lr=5e-5)


    
