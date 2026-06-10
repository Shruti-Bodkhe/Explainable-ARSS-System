import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# STEP 1: Load files FIRST
df = pd.read_csv("results/arss_results.csv")
gt_df = pd.read_csv("ground_truth.csv")

print("\n--- SAMPLE FROM RESULTS FILE ---")
print(df["resume_file"].head(10))

print("\n--- SAMPLE FROM GROUND TRUTH ---")
print(gt_df["resume_file"].head(10))

# STEP 2: Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip().str.lower()
gt_df.columns = gt_df.columns.str.strip().str.lower()

# STEP 3: NOW print columns (after loading)
print("Output columns:", df.columns)
print("Ground truth columns:", gt_df.columns)

# STEP 4: Convert prediction to numeric
df["predicted_label"] = df["recommendation"].apply(
    lambda x: 1 if x == "selected" else 0
)

# Normalize names
df["resume_file"] = df["resume_file"].str.strip().str.lower()
gt_df["resume_file"] = gt_df["resume_file"].str.strip().str.lower()

# Remove .pdf if mismatch exists
df["resume_file"] = df["resume_file"].str.replace(".pdf", "", regex=False)
gt_df["resume_file"] = gt_df["resume_file"].str.replace(".pdf", "", regex=False)

# STEP 5: Merge
merged = df.merge(gt_df, on="resume_file")

print("Total matched resumes:", len(merged))

# STEP 6: Extract values
y_true = merged["actual_label"]
y_pred = merged["predicted_label"]

# STEP 7: Metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, zero_division=0)
recall = recall_score(y_true, y_pred, zero_division=0)
f1 = f1_score(y_true, y_pred, zero_division=0)

# STEP 8: Print results
print("\n--- Evaluation Results ---")
print("Accuracy:", round(accuracy, 2))
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))
print("F1 Score:", round(f1, 2))

# STEP 9: Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
print("\nConfusion Matrix:\n", cm)