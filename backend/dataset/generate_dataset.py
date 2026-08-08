
import os
import random
import pandas as pd


# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "disease_dataset.csv"
)

RECORDS_PER_DISEASE = 1000

RANDOM_SEED = 42

random.seed(RANDOM_SEED)


# ============================================================
# EXACT 29 FEATURES USED BY THE MODEL
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
# DISEASE -> REALISTIC SYMPTOM PROFILE
#
# Only symptoms from FEATURES are allowed.
#
# "core" = strongly characteristic
# "support" = commonly associated
# ============================================================

DISEASE_PROFILES = {

    "Acute Kidney Injury": {
        "core": [
            "fatigue",
            "nausea",
            "vomiting",
            "dizziness",
            "abdominal_pain"
        ],
        "support": [
            "fever"
            
        ]
    },

    "Addison Disease": {
        "core": [
            "fatigue",
            "weight_loss",
            "abdominal_pain",
            "nausea",
            "dizziness"
        ],
        "support": [
            "vomiting",
            "sweating"
        ]
    },

    "Allergic Rhinitis": {
        "core": [
            "runny_nose",
            "itching"
        ],
        "support": [
            "headache",
            "fatigue"
        ]
    },

    "Alzheimer Disease": {
        "core": [
            "dizziness",
            "fatigue"
        ],
        "support": [
            "headache"
        ]
    },

    "Angina": {
        "core": [
            "chest_pain",
            "shortness_of_breath",
            "fatigue"
        ],
        "support": [
            "dizziness",
            "sweating"
        ]
    },

    "Anxiety Disorder": {
        "core": [
            "chest_pain",
            "shortness_of_breath",
            "dizziness",
            "sweating"
        ],
        "support": [
            "fatigue",
            "headache"
        ]
    },

    "Appendicitis": {
        "core": [
            "abdominal_pain",
            "fever",
            "nausea",
            "vomiting"
        ],
        "support": [
            "fatigue"
            
        ]
    },

    "Arrhythmia": {
        "core": [
            "chest_pain",
            "dizziness",
            "shortness_of_breath"
        ],
        "support": [
            "fatigue",
            "sweating"
        ]
    },

    "Asthma": {
        "core": [
            "shortness_of_breath",
            "cough"
        ],
        "support": [
            "chest_pain",
            "fatigue"
        ]
    },

    "Atherosclerosis": {
        "core": [
            "chest_pain",
            "fatigue"
        ],
        "support": [
            "shortness_of_breath",
            "dizziness"
        ]
    },

    "Bell Palsy": {
        "core": [
            "headache",
            "dizziness"
        ],
        "support": [
            "fatigue"
        ]
    },

    "Bladder Infection": {
        "core": [
            "frequent_urination",
            "abdominal_pain",
            "fever"
        ],
        "support": [
            "nausea",
            "fatigue"
        ]
    },

    "Bronchitis": {
        "core": [
            "cough",
            "fever",
            "fatigue"
        ],
        "support": [
            "chest_pain",
            "shortness_of_breath",
            "body_pain"
        ]
    },

    "COPD": {
        "core": [
            "cough",
            "shortness_of_breath",
            "fatigue"
        ],
        "support": [
            "chest_pain"
        ]
    },

    "COVID-19": {
        "core": [
            "fever",
            "cough",
            "fatigue",
            "body_pain"
        ],
        "support": [
            "headache",
            "sore_throat",
            "loss_of_taste",
            "loss_of_smell",
            "shortness_of_breath"
        ]
    },

    "Cardiomyopathy": {
        "core": [
            "shortness_of_breath",
            "fatigue",
            "chest_pain"
        ],
        "support": [
            "dizziness"
        ]
    },

    "Cataract": {
        "core": [
            "blurred_vision"
        ],
        "support": [
            "dizziness",
            "headache"
        ]
    },

    "Chickenpox": {
        "core": [
            "rash",
            "itching",
            "fever"
        ],
        "support": [
            "fatigue",
            "headache"
        ]
    },

    "Cholera": {
        "core": [
            "diarrhea",
            "vomiting",
            "nausea"
        ],
        "support": [
            "abdominal_pain",
            "dizziness",
            "fatigue"
        ]
    },

    "Chronic Kidney Disease": {
        "core": [
            "fatigue",
            "nausea",
            "dizziness"
        ],
        "support": [
            "vomiting",
            "itching",
            "weight_loss"
        ]
    },

    "Common Cold": {
        "core": [
            "runny_nose",
            "sore_throat",
            "cough"
        ],
        "support": [
            "headache",
            "fatigue",
            "fever"
        ]
    },

    "Conjunctivitis": {
        "core": [
            "itching"
        ],
        "support": [
            "fever",
            "headache"
        ]
    },

    "Coronary Artery Disease": {
        "core": [
            "chest_pain",
            "shortness_of_breath",
            "fatigue"
        ],
        "support": [
            "dizziness",
            "sweating"
        ]
    },

    "Crohn's Disease": {
        "core": [
            "abdominal_pain",
            "diarrhea",
            "weight_loss"
        ],
        "support": [
            "fatigue",
            "fever",
            "nausea"
        ]
    },

    "Cushing Syndrome": {
        "core": [
            "weight_loss",
            "fatigue"
        ],
        "support": [
            "headache",
            "dizziness"
        ]
    },

    "Dengue": {
        "core": [
            "high_fever",
            "headache",
            "body_pain",
            "joint_pain"
        ],
        "support": [
            "nausea",
            "vomiting",
            "rash",
            "fatigue"
        ]
    },

    "Depression": {
        "core": [
            "fatigue",
            "headache"
        ],
        "support": [
            "dizziness",
            "body_pain"
        ]
    },

    "Diabetes Type 1": {
        "core": [
            "frequent_urination",
            "increased_thirst",
            "weight_loss",
            "fatigue"
        ],
        "support": [
            "blurred_vision",
            "nausea",
            "abdominal_pain"
        ]
    },

    "Diabetes Type 2": {
        "core": [
            "frequent_urination",
            "increased_thirst",
            "fatigue",
            "blurred_vision"
        ],
        "support": [
            "weight_loss"
        ]
    },

    "Epilepsy": {
        "core": [
            "dizziness",
            "headache",
            "fatigue"
        ],
        "support": [
            "vomiting"
        ]
    },

    "Food Poisoning": {
        "core": [
            "nausea",
            "vomiting",
            "diarrhea",
            "abdominal_pain"
        ],
        "support": [
            "fever",
            "fatigue",
            "dizziness"
        ]
    },

    "GERD": {
        "core": [
            "chest_pain",
            "nausea",
            "abdominal_pain"
        ],
        "support": [
            "cough",
            "sore_throat"
        ]
    },

    "Gallstones": {
        "core": [
            "abdominal_pain",
            "nausea",
            "vomiting"
        ],
        "support": [
            "fever",
            "yellow_skin"
        ]
    },

    "Gastritis": {
        "core": [
            "abdominal_pain",
            "nausea"
        ],
        "support": [
            "vomiting",
            "fatigue"
        ]
    },

    "Glaucoma": {
        "core": [
            "blurred_vision",
            "headache"
        ],
        "support": [
            "nausea",
            "vomiting",
            "dizziness"
        ]
    },

    "Goiter": {
        "core": [
            "fatigue"
        ],
        "support": [
            "shortness_of_breath",
            "dizziness"
        ]
    },

    "HIV/AIDS": {
        "core": [
            "fatigue",
            "weight_loss",
            "fever"
        ],
        "support": [
            "sore_throat",
            "rash",
            "swollen_lymph_nodes",
            "diarrhea"
        ]
    },

    "Hearing Loss": {
        "core": [
            "dizziness"
        ],
        "support": [
            "headache",
            "fatigue"
        ]
    },

    "Heart Failure": {
        "core": [
            "shortness_of_breath",
            "fatigue",
            "chest_pain"
        ],
        "support": [
            "dizziness",
            "cough"
        ]
    },

    "Hepatitis A": {
        "core": [
            "yellow_skin",
            "dark_urine",
            "fatigue",
            "nausea"
        ],
        "support": [
            "abdominal_pain",
            "fever",
            "vomiting"
        ]
    },

    "Hepatitis B": {
        "core": [
            "yellow_skin",
            "dark_urine",
            "fatigue"
        ],
        "support": [
            "nausea",
            "abdominal_pain",
            "fever"
        ]
    },

    "Hepatitis C": {
        "core": [
            "fatigue",
            "yellow_skin",
            "dark_urine"
        ],
        "support": [
            "nausea",
            "abdominal_pain"
        ]
    },

    "Hypertension": {
        "core": [
            "headache",
            "dizziness"
        ],
        "support": [
            "chest_pain",
            "shortness_of_breath",
            "fatigue"
        ]
    },

    "Hyperthyroidism": {
        "core": [
            "weight_loss",
            "sweating",
            "fatigue"
        ],
        "support": [
            "dizziness",
            "shortness_of_breath"
        ]
    },

    "Hypothyroidism": {
        "core": [
            "fatigue",
            "weight_loss"
        ],
        "support": [
            "dizziness",
            "headache"
        ]
    },

    "Influenza": {
        "core": [
            "high_fever",
            "cough",
            "body_pain",
            "fatigue"
        ],
        "support": [
            "headache",
            "sore_throat",
            "chills"
        ]
    },

    "Insomnia": {
        "core": [
            "fatigue",
            "headache"
        ],
        "support": [
            "dizziness"
        ]
    },

    "Irritable Bowel Syndrome": {
        "core": [
            "abdominal_pain",
            "diarrhea",
            "nausea"
        ],
        "support": [
            "fatigue"
        ]
    },

    "Kidney Stone": {
        "core": [
            "abdominal_pain",
            "nausea",
            "vomiting"
        ],
        "support": [
            "fever",
            "dizziness",
            "sweating"
        ]
    },

    "Laryngitis": {
        "core": [
            "sore_throat",
            "cough"
        ],
        "support": [
            "fever",
            "fatigue"
        ]
    },

    "Leptospirosis": {
        "core": [
            "fever",
            "headache",
            "body_pain",
            "chills"
        ],
        "support": [
            "vomiting",
            "yellow_skin",
            "fatigue"
        ]
    },

    "Malaria": {
        "core": [
            "high_fever",
            "chills",
            "sweating",
            "headache"
        ],
        "support": [
            "body_pain",
            "vomiting",
            "nausea",
            "fatigue"
        ]
    },

    "Measles": {
        "core": [
            "fever",
            "rash",
            "cough"
        ],
        "support": [
            "sore_throat",
            "runny_nose",
            "headache",
            "fatigue"
        ]
    },

    "Metabolic Syndrome": {
        "core": [
            "fatigue",
            "frequent_urination",
            "increased_thirst"
        ],
        "support": [
            "blurred_vision"
        ]
    },

    "Migraine": {
        "core": [
            "headache",
            "dizziness",
            "nausea"
        ],
        "support": [
            "vomiting",
            "fatigue"
        ]
    },

    "Mumps": {
        "core": [
            "fever",
            "headache",
            "fatigue"
        ],
        "support": [
            "swollen_lymph_nodes",
            "body_pain"
        ]
    },

    "Myocardial Infarction": {
        "core": [
            "chest_pain",
            "shortness_of_breath",
            "sweating"
        ],
        "support": [
            "nausea",
            "vomiting",
            "dizziness",
            "fatigue"
        ]
    },

    "Obesity": {
        "core": [
            "fatigue",
            "shortness_of_breath"
        ],
        "support": [
            "joint_pain",
            "frequent_urination"
        ]
    },

    "Otitis Media": {
        "core": [
            "fever",
            "headache"
        ],
        "support": [
            "dizziness",
            "fatigue"
        ]
    },

    "PCOS": {
        "core": [
            "weight_loss",
            "fatigue"
        ],
        "support": [
            "abdominal_pain",
            "headache",
            "dizziness"
        ]
    },

    "Pancreatitis": {
        "core": [
            "abdominal_pain",
            "nausea",
            "vomiting"
        ],
        "support": [
            "fever",
            "fatigue"
        ]
    },

    "Parkinson Disease": {
        "core": [
            "dizziness",
            "fatigue"
        ],
        "support": [
            "headache"
        ]
    },

    "Peptic Ulcer": {
        "core": [
            "abdominal_pain",
            "nausea"
        ],
        "support": [
            "vomiting",
            "fatigue"
        ]
    },

    "Pericarditis": {
        "core": [
            "chest_pain",
            "shortness_of_breath",
            "fever"
        ],
        "support": [
            "fatigue"
        ]
    },

    "Pharyngitis": {
        "core": [
            "sore_throat",
            "fever"
        ],
        "support": [
            "headache",
            "fatigue"
        ]
    },

    "Pneumonia": {
        "core": [
            "fever",
            "cough",
            "shortness_of_breath",
            "chest_pain"
        ],
        "support": [
            "fatigue",
            "body_pain",
            "chills"
        ]
    },

    "Pulmonary Fibrosis": {
        "core": [
            "shortness_of_breath",
            "cough",
            "fatigue"
        ],
        "support": [
            "chest_pain"
        ]
    },

    "Rabies": {
        "core": [
            "fever",
            "headache",
            "fatigue"
        ],
        "support": [
            "vomiting",
            "dizziness"
        ]
    },

    "Sinusitis": {
        "core": [
            "headache",
            "runny_nose"
        ],
        "support": [
            "fever",
            "cough",
            "fatigue"
        ]
    },

    "Sleep Apnea": {
        "core": [
            "fatigue",
            "headache"
        ],
        "support": [
            "dizziness",
            "shortness_of_breath"
        ]
    },

    "Stroke": {
        "core": [
            "headache",
            "dizziness"
        ],
        "support": [
            "fatigue",
            "vomiting"
        ]
    },

    "Tetanus": {
        "core": [
            "fever",
            "body_pain"
        ],
        "support": [
            "headache",
            "fatigue",
            "sweating"
        ]
    },

    "Tonsillitis": {
        "core": [
            "sore_throat",
            "fever"
        ],
        "support": [
            "headache",
            "fatigue"
        ]
    },

    "Tuberculosis": {
        "core": [
            "cough",
            "fever",
            "weight_loss",
            "fatigue"
        ],
        "support": [
            "chills",
            "sweating",
            "chest_pain"
        ]
    },

    "Typhoid": {
        "core": [
            "high_fever",
            "headache",
            "abdominal_pain",
            "fatigue"
        ],
        "support": [
            "diarrhea",
            "vomiting",
            "body_pain"
        ]
    },

    "Ulcerative Colitis": {
        "core": [
            "diarrhea",
            "abdominal_pain",
            "fatigue"
        ],
        "support": [
            "weight_loss",
            "fever"
        ]
    },

    "Urinary Tract Infection": {
        "core": [
            "frequent_urination",
            "abdominal_pain",
            "fever"
        ],
        "support": [
            "nausea",
            "fatigue"
        ]
    },

    "Valve Disease": {
        "core": [
            "chest_pain",
            "shortness_of_breath",
            "fatigue"
        ],
        "support": [
            "dizziness"
        ]
    },

    "Vertigo": {
        "core": [
            "dizziness",
            "nausea"
        ],
        "support": [
            "vomiting",
            "headache",
            "fatigue"
        ]
    },

    "Whooping Cough": {
        "core": [
            "cough",
            "shortness_of_breath"
        ],
        "support": [
            "vomiting",
            "fatigue",
            "fever"
        ]
    }
}


# ============================================================
# VALIDATE PROFILES
# ============================================================

print("Validating disease profiles...")

unknown_symptoms = []

for disease, profile in DISEASE_PROFILES.items():

    all_symptoms = (
        profile["core"] +
        profile["support"]
    )

    for symptom in all_symptoms:

        if symptom not in FEATURES:

            unknown_symptoms.append(
                (disease, symptom)
            )


if unknown_symptoms:

    print("\nInvalid symptoms found:")

    for disease, symptom in unknown_symptoms:
        print(
            f"  {disease} -> {symptom}"
        )

    raise ValueError(
        "Some disease profiles contain "
        "symptoms that are not in FEATURES."
    )


if len(DISEASE_PROFILES) != 80:

    raise ValueError(
        f"Expected 80 diseases, "
        f"found {len(DISEASE_PROFILES)}."
    )


print(
    f"Validated {len(DISEASE_PROFILES)} diseases."
)


# ============================================================
# GENERATE ONE RECORD
# ============================================================

def generate_record(disease, profile):

    row = {
        feature: 0
        for feature in FEATURES
    }

    core = profile["core"]
    support = profile["support"]

    # --------------------------------------------------------
    # Core symptoms
    # Most core symptoms should appear.
    # --------------------------------------------------------

    for symptom in core:

        probability = random.uniform(
            0.70,
            0.95
        )

        if random.random() < probability:
            row[symptom] = 1

    # --------------------------------------------------------
    # Support symptoms
    # Appear less frequently.
    # --------------------------------------------------------

    for symptom in support:

        probability = random.uniform(
            0.30,
            0.65
        )

        if random.random() < probability:
            row[symptom] = 1

    # --------------------------------------------------------
    # Make sure every record has at least
    # one characteristic symptom.
    # --------------------------------------------------------

    if sum(
        row[symptom]
        for symptom in core
    ) == 0:

        symptom = random.choice(core)

        row[symptom] = 1

    row["disease"] = disease

    return row


# ============================================================
# GENERATE DATASET
# ============================================================

print("\nGenerating dataset...")

records = []

for index, (disease, profile) in enumerate(
    DISEASE_PROFILES.items(),
    start=1
):

    print(
        f"[{index:02d}/80] {disease}"
    )

    for _ in range(
        RECORDS_PER_DISEASE
    ):

        records.append(
            generate_record(
                disease,
                profile
            )
        )


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(records)

columns = FEATURES + ["disease"]

df = df[columns]


# ============================================================
# SHUFFLE
# ============================================================

df = df.sample(
    frac=1,
    random_state=RANDOM_SEED
).reset_index(drop=True)


# ============================================================
# SAVE
# ============================================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ============================================================
# SUMMARY
# ============================================================

print("\n======================================")
print("DATASET GENERATED SUCCESSFULLY")
print("======================================")

print(
    f"File: {OUTPUT_FILE}"
)

print(
    f"Rows: {len(df)}"
)

print(
    f"Columns: {len(df.columns)}"
)

print(
    f"Diseases: {df['disease'].nunique()}"
)

print("\nDisease distribution:")

print(
    df["disease"]
    .value_counts()
    .sort_index()
)

print("\nFeatures:")

print(FEATURES)

print("\n======================================")

