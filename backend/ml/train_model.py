
import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "disease_dataset.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "disease_model.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "label_encoder.pkl"
)


# ============================================================
# LOAD DATASET
# ============================================================

print("\nDataset path:")
print(
    os.path.abspath(DATASET_PATH)
)

print("\nLoading dataset...")

if not os.path.exists(DATASET_PATH):

    raise FileNotFoundError(
        f"Dataset not found:\n{DATASET_PATH}"
    )

df = pd.read_csv(
    DATASET_PATH
)

print(
    f"Dataset loaded successfully."
)

print(
    f"Rows: {len(df)}"
)

print(
    f"Columns: {len(df.columns)}"
)


# ============================================================
# CHECK DATASET
# ============================================================

if "disease" not in df.columns:

    raise ValueError(
        "Dataset must contain a 'disease' column."
    )


X = df.drop(
    "disease",
    axis=1
)

y = df["disease"]


print(
    f"\nNumber of features: {X.shape[1]}"
)

print(
    "\nFeatures:"
)

print(
    list(X.columns)
)


# ============================================================
# ENCODE LABELS
# ============================================================

print(
    "\nEncoding disease names..."
)

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(
    y
)

print(
    f"Total diseases: "
    f"{len(encoder.classes_)}"
)


# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

print(
    "\nSplitting dataset..."
)

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y_encoded,

    test_size=0.20,

    random_state=42,

    stratify=y_encoded
)


print(
    f"Training records: "
    f"{len(X_train)}"
)

print(
    f"Testing records: "
    f"{len(X_test)}"
)


# ============================================================
# MEMORY-EFFICIENT RANDOM FOREST
# ============================================================

print(
    "\nTraining memory-efficient Random Forest..."
)

model = RandomForestClassifier(

    n_estimators=120,

    max_depth=16,

    min_samples_split=4,

    min_samples_leaf=2,

    max_features="sqrt",

    class_weight="balanced",

    random_state=42,

    n_jobs=1
)


model.fit(
    X_train,
    y_train
)


print(
    "Training completed."
)


# ============================================================
# TEST MODEL
# ============================================================

print(
    "\nTesting model..."
)

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    f"Model accuracy: "
    f"{accuracy * 100:.2f}%"
)


# ============================================================
# SAVE MODEL
# ============================================================

print(
    "\nSaving model..."
)

joblib.dump(
    model,
    MODEL_PATH,
    compress=3
)

joblib.dump(
    encoder,
    ENCODER_PATH,
    compress=3
)


# ============================================================
# FILE SIZE
# ============================================================

model_size = (
    os.path.getsize(
        MODEL_PATH
    ) / (1024 * 1024)
)

encoder_size = (
    os.path.getsize(
        ENCODER_PATH
    ) / 1024
)


# ============================================================
# SUMMARY
# ============================================================

print("\n======================================")
print("MODEL TRAINING COMPLETE")
print("======================================")

print(
    f"Model:\n{os.path.abspath(MODEL_PATH)}"
)

print(
    f"\nEncoder:\n{os.path.abspath(ENCODER_PATH)}"
)

print(
    f"\nModel size: "
    f"{model_size:.2f} MB"
)

print(
    f"Encoder size: "
    f"{encoder_size:.2f} KB"
)

print(
    f"\nTotal diseases: "
    f"{len(encoder.classes_)}"
)

print("\nDiseases:")

for index, disease in enumerate(
    encoder.classes_,
    start=1
):

    print(
        f"{index}. {disease}"
    )

print(
    "\n======================================"
)

