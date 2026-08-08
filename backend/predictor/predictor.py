
import os
import json
import joblib
import pandas as pd


# ============================================================
# PATHS
# ============================================================

CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

BACKEND_DIR = os.path.dirname(
    CURRENT_DIR
)

MODEL_PATH = os.path.join(
    BACKEND_DIR,
    "ml",
    "disease_model.pkl"
)

ENCODER_PATH = os.path.join(
    BACKEND_DIR,
    "ml",
    "label_encoder.pkl"
)

DATASET_PATH = os.path.join(
    BACKEND_DIR,
    "dataset",
    "disease_dataset.csv"
)

DISEASE_FILE = os.path.join(
    BACKEND_DIR,
    "data",
    "diseases.json"
)


# ============================================================
# FEATURES
# ============================================================

FEATURES = [
    "fever",
    "cough",
    "headache",
    "vomiting",
    "chest_pain",
    "fatigue",
    "body_pain",
    "sore_throat",
    "runny_nose",
    "shortness_of_breath",
    "loss_of_taste",
    "loss_of_smell",
    "diarrhea",
    "nausea",
    "abdominal_pain",
    "dizziness",
    "rash",
    "itching",
    "joint_pain",
    "high_fever",
    "chills",
    "sweating",
    "weight_loss",
    "frequent_urination",
    "increased_thirst",
    "blurred_vision",
    "yellow_skin",
    "dark_urine",
    "swollen_lymph_nodes"
]


# ============================================================
# SYMPTOM ALIASES
# ============================================================

SYMPTOM_ALIASES = {

    "high fever": "high_fever",
    "high-fever": "high_fever",

    "chest pain": "chest_pain",

    "body pain": "body_pain",

    "sore throat": "sore_throat",

    "runny nose": "runny_nose",

    "shortness of breath":
        "shortness_of_breath",

    "difficulty breathing":
        "shortness_of_breath",

    "breathing difficulty":
        "shortness_of_breath",

    "loss of taste":
        "loss_of_taste",

    "loss of smell":
        "loss_of_smell",

    "abdominal pain":
        "abdominal_pain",

    "stomach pain":
        "abdominal_pain",

    "joint pain":
        "joint_pain",

    "weight loss":
        "weight_loss",

    "frequent urination":
        "frequent_urination",

    "increased thirst":
        "increased_thirst",

    "blurred vision":
        "blurred_vision",

    "yellow skin":
        "yellow_skin",

    "dark urine":
        "dark_urine",

    "swollen lymph nodes":
        "swollen_lymph_nodes"
}


# ============================================================
# LOAD MODEL
# ============================================================

print(
    "Loading disease prediction model..."
)

if not os.path.exists(MODEL_PATH):

    raise FileNotFoundError(
        f"Model not found:\n{MODEL_PATH}"
    )

if not os.path.exists(ENCODER_PATH):

    raise FileNotFoundError(
        f"Encoder not found:\n{ENCODER_PATH}"
    )

model = joblib.load(
    MODEL_PATH
)

encoder = joblib.load(
    ENCODER_PATH
)

print(
    "Disease prediction model loaded."
)


# ============================================================
# LOAD DATASET
#
# Used only to calculate disease symptom profiles.
# ============================================================

if not os.path.exists(DATASET_PATH):

    raise FileNotFoundError(
        f"Dataset not found:\n{DATASET_PATH}"
    )

dataset = pd.read_csv(
    DATASET_PATH
)


# Make sure all features exist.

missing_features = [
    feature
    for feature in FEATURES
    if feature not in dataset.columns
]

if missing_features:

    raise ValueError(
        "Dataset is missing features: "
        + str(missing_features)
    )


# ============================================================
# CREATE DISEASE PROFILES
# ============================================================

profile_columns = FEATURES

disease_profiles = (
    dataset
    .groupby("disease")[profile_columns]
    .mean()
)


# ============================================================
# LOAD DISEASE INFORMATION
# ============================================================

if os.path.exists(
    DISEASE_FILE
):

    with open(
        DISEASE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        disease_db = json.load(
            file
        )

    print(
        f"Disease information loaded: "
        f"{len(disease_db)} diseases"
    )

else:

    print(
        "WARNING: diseases.json not found."
    )

    disease_db = {}


# ============================================================
# NORMALIZE SYMPTOM
# ============================================================

def normalize_symptom(symptom):

    symptom = str(
        symptom
    ).strip().lower()

    symptom = symptom.replace(
        "-",
        " "
    )

    symptom = " ".join(
        symptom.split()
    )

    if symptom in SYMPTOM_ALIASES:

        return SYMPTOM_ALIASES[
            symptom
        ]

    return symptom.replace(
        " ",
        "_"
    )


# ============================================================
# PARSE SYMPTOMS
# ============================================================

def parse_symptoms(symptoms):

    if isinstance(
        symptoms,
        str
    ):

        raw = symptoms.split(",")

    elif isinstance(
        symptoms,
        list
    ):

        raw = symptoms

    else:

        return []

    result = []

    for symptom in raw:

        normalized = normalize_symptom(
            symptom
        )

        if normalized in FEATURES:

            result.append(
                normalized
            )

    return list(
        dict.fromkeys(result)
    )


# ============================================================
# CREATE MODEL INPUT
# ============================================================

def create_input(symptoms):

    row = {}

    for feature in FEATURES:

        row[feature] = (
            1
            if feature in symptoms
            else 0
        )

    return pd.DataFrame(
        [row],
        columns=FEATURES
    )


# ============================================================
# SYMPTOM MATCH SCORE
# ============================================================

def calculate_match_scores(symptoms):

    scores = {}

    for disease in disease_profiles.index:

        profile = disease_profiles.loc[
            disease
        ]

        matched_values = []

        for symptom in symptoms:

            matched_values.append(
                float(
                    profile.get(
                        symptom,
                        0
                    )
                )
            )

        if not matched_values:

            scores[disease] = 0.0

        else:

            # Average presence of the
            # entered symptoms for this disease.
            scores[disease] = (
                sum(matched_values)
                / len(matched_values)
            )

    return scores


# ============================================================
# DISEASE INFORMATION
# ============================================================

def get_disease_info(disease):

    info = disease_db.get(
        disease
    )

    if info is None:

        for name, value in disease_db.items():

            if str(name).lower() == str(
                disease
            ).lower():

                info = value
                break

    if info is None:

        info = {}

    return {

        "description":
            info.get(
                "description",
                "No description available."
            ),

        "medicines":
            info.get(
                "medicines",
                []
            ),

        "precautions":
            info.get(
                "precautions",
                []
            ),

        "diet":
            info.get(
                "diet",
                []
            ),

        "doctor":
            info.get(
                "doctor",
                "General Physician"
            )
    }


# ============================================================
# MAIN PREDICTION FUNCTION
# ============================================================

def predict(symptoms):

    print(
        "\n=============================="
    )

    print(
        "Prediction request received"
    )

    parsed = parse_symptoms(
        symptoms
    )

    print(
        "Symptoms:",
        parsed
    )

    if not parsed:

        raise ValueError(
            "No valid symptoms detected. "
            "Please enter symptoms separated "
            "by commas."
        )

    # --------------------------------------------------------
    # Create input
    # --------------------------------------------------------

    df = create_input(
        parsed
    )

    # --------------------------------------------------------
    # ML prediction probabilities
    # --------------------------------------------------------

    probabilities = model.predict_proba(
        df
    )[0]

    classes = encoder.classes_

    ml_scores = {}

    for index, disease in enumerate(
        classes
    ):

        ml_scores[
            disease
        ] = float(
            probabilities[index]
        )

    # --------------------------------------------------------
    # Direct symptom matching
    # --------------------------------------------------------

    match_scores = calculate_match_scores(
        parsed
    )

    # --------------------------------------------------------
    # Combine both signals
    #
    # ML = 55%
    # Symptom profile = 45%
    # --------------------------------------------------------

    final_scores = {}

    for disease in classes:

        ml_score = ml_scores.get(
            disease,
            0.0
        )

        symptom_score = match_scores.get(
            disease,
            0.0
        )

        final_scores[disease] = (
            0.55 * ml_score
            +
            0.45 * symptom_score
        )

    # --------------------------------------------------------
    # Sort diseases by combined score
    # --------------------------------------------------------

    ranked = sorted(
        final_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    best_disease = ranked[0][0]

    best_score = ranked[0][1]

    # --------------------------------------------------------
    # Information
    # --------------------------------------------------------

    info = get_disease_info(
        best_disease
    )

    # --------------------------------------------------------
    # Matched symptoms
    # --------------------------------------------------------

    matched = []

    if best_disease in disease_profiles.index:

        profile = disease_profiles.loc[
            best_disease
        ]

        for symptom in parsed:

            if profile.get(
                symptom,
                0
            ) >= 0.25:

                matched.append(
                    symptom
                )

    # --------------------------------------------------------
    # Convert score to percentage
    # --------------------------------------------------------

    confidence = round(
        best_score * 100,
        2
    )

    result = {

        "disease":
            best_disease,

        "description":
            info["description"],

        "medicines":
            info["medicines"],

        "precautions":
            info["precautions"],

        "diet":
            info["diet"],

        "doctor":
            info["doctor"],

        "symptoms":
            parsed,

        "matched_symptoms":
            matched,

        "confidence":
            confidence,

        "message":
            "This is an AI-generated health indication, "
            "not a medical diagnosis. Consult a qualified "
            "healthcare professional for proper evaluation."
    }

    print(
        "Predicted disease:",
        best_disease
    )

    print(
        "Confidence:",
        confidence,
        "%"
    )

    print(
        "Matched symptoms:",
        matched
    )

    print(
        "==============================\n"
    )

    return result

