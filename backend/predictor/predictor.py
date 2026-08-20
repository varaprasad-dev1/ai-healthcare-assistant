import os
import json

from dotenv import load_dotenv
from google import genai


# =====================================================
# LOAD ENVIRONMENT VARIABLES
# =====================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing from backend/.env"
    )


# =====================================================
# GEMINI CLIENT
# =====================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# =====================================================
# AI SYMPTOM ANALYSIS
# =====================================================

def predict(symptoms):

    # -------------------------------------------------
    # Validate input
    # -------------------------------------------------

    if isinstance(symptoms, list):

        symptom_text = ", ".join(
            str(item).strip()
            for item in symptoms
            if str(item).strip()
        )

    elif isinstance(symptoms, str):

        symptom_text = symptoms.strip()

    else:

        raise ValueError(
            "Symptoms must be provided as text or a list."
        )

    if not symptom_text:

        raise ValueError(
            "Please enter at least one symptom."
        )

    # -------------------------------------------------
    # Gemini prompt
    # -------------------------------------------------

    prompt = f"""
You are an AI healthcare assistant.

The user has provided the following symptoms:

{symptom_text}

Analyze these symptoms carefully and provide an
EDUCATIONAL health assessment.

IMPORTANT MEDICAL SAFETY RULES:

- This is NOT a confirmed medical diagnosis.
- Do not claim certainty.
- Consider multiple possible conditions when appropriate.
- Do not invent symptoms that the user did not provide.
- Do not prescribe prescription medicines.
- Do not provide medication dosages.
- Do not tell the user to start, stop, or change medication.
- If symptoms could indicate something serious, recommend
  appropriate professional medical evaluation.
- Diet information must be general healthy lifestyle advice,
  not a treatment or cure.
- If there is not enough information to make a reasonable
  assessment, clearly say so.

Return ONLY valid JSON.

The JSON MUST have exactly these fields:

{{
    "disease": "Most likely possible condition or conditions",
    "description": "Simple explanation of the possible condition",
    "medicines": [
        "Safe general treatment information or recommendation to consult a doctor"
    ],
    "precautions": [
        "Safe precaution 1",
        "Safe precaution 2",
        "Safe precaution 3"
    ],
    "diet": [
        "General healthy diet/lifestyle advice 1",
        "General healthy diet/lifestyle advice 2",
        "General healthy diet/lifestyle advice 3"
    ],
    "doctor": "Recommended healthcare professional",
    "confidence": "Low / Moderate / High",
    "matched_symptoms": [
        "Symptoms from the user's input that support the assessment"
    ],
    "message": "This is an educational AI assessment and not a confirmed medical diagnosis."
}}

FIELD REQUIREMENTS:

disease:
Give a possible condition based on the symptoms.
If multiple conditions are reasonably possible, mention the
main possibilities rather than pretending there is one certain
diagnosis.

description:
Explain the possibility in simple language.

medicines:
Do not prescribe.
Instead, describe general treatment categories or recommend
professional evaluation.

precautions:
Give practical and safe precautions relevant to the symptoms.

diet:
Give general healthy diet and lifestyle information only.

doctor:
Recommend an appropriate healthcare professional.

confidence:
Use ONLY:
"Low"
"Moderate"
or
"High"

matched_symptoms:
Include only symptoms that were actually supplied by the user.

message:
Always include the medical disclaimer.
"""

    # -------------------------------------------------
    # Send request to Gemini
    # -------------------------------------------------

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    result_text = response.text.strip()

    # -------------------------------------------------
    # Remove markdown JSON formatting if Gemini adds it
    # -------------------------------------------------

    if result_text.startswith("```"):

        result_text = result_text.replace(
            "```json",
            ""
        )

        result_text = result_text.replace(
            "```",
            ""
        )

        result_text = result_text.strip()

    # -------------------------------------------------
    # Convert JSON to Python dictionary
    # -------------------------------------------------

    try:

        result = json.loads(
            result_text
        )

    except json.JSONDecodeError:

        result = {
            "disease": "Unable to determine",

            "description":
                result_text,

            "medicines": [
                "Please consult a qualified healthcare professional "
                "for appropriate evaluation and treatment."
            ],

            "precautions": [
                "Monitor your symptoms.",
                "Avoid self-medicating.",
                "Seek professional medical advice if symptoms persist "
                "or worsen."
            ],

            "diet": [
                "Maintain a balanced diet.",
                "Stay adequately hydrated.",
                "Get adequate rest."
            ],

            "doctor":
                "General Physician",

            "confidence":
                "Low",

            "matched_symptoms":
                symptom_text.split(","),

            "message":
                "This is an educational AI assessment and not "
                "a confirmed medical diagnosis."
        }

    # -------------------------------------------------
    # Ensure required fields exist
    # -------------------------------------------------

    result.setdefault(
        "disease",
        "Unable to determine"
    )

    result.setdefault(
        "description",
        "Please consult a qualified healthcare professional."
    )

    result.setdefault(
        "medicines",
        [
            "Consult a qualified healthcare professional "
            "before using medication."
        ]
    )

    result.setdefault(
        "precautions",
        [
            "Monitor your symptoms.",
            "Avoid self-medication.",
            "Seek professional medical advice if symptoms worsen."
        ]
    )

    result.setdefault(
        "diet",
        [
            "Maintain a balanced diet.",
            "Stay adequately hydrated.",
            "Get adequate rest."
        ]
    )

    result.setdefault(
        "doctor",
        "General Physician"
    )

    result.setdefault(
        "confidence",
        "Low"
    )

    result.setdefault(
        "matched_symptoms",
        []
    )

    result.setdefault(
        "message",
        "This is an educational AI assessment and not "
        "a confirmed medical diagnosis."
    )

    return result