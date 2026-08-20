import os
import base64
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
# SKIN IMAGE ANALYSIS
# =====================================================

def analyze_skin_image(image_file):

    image_bytes = image_file.read()

    if not image_bytes:
        raise ValueError("The uploaded image is empty.")

    encoded_image = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    content_type = image_file.content_type or "image/jpeg"

    # =================================================
    # PROMPT
    # =================================================

    prompt = """
You are an AI healthcare assistant providing an educational
analysis of a skin image.

Analyze ONLY what can reasonably be observed in the image.

IMPORTANT MEDICAL SAFETY RULES:

- This is NOT a confirmed medical diagnosis.
- Do not claim certainty from an image alone.
- Use phrases such as "possible", "may be consistent with",
  or "appears potentially consistent with".
- If the image is unclear, say that the condition cannot
  be reliably assessed from the image.
- Do NOT prescribe prescription medicines.
- Do NOT provide medication dosages.
- Do NOT tell the user to start, stop, or change prescription
  medication.
- Recommend evaluation by an appropriate healthcare professional
  when necessary.
- Diet information must be general healthy lifestyle information,
  NOT a treatment or cure.
- Do not invent information that cannot reasonably be inferred.

Return ONLY valid JSON.

The JSON MUST have exactly these fields:

{
    "disease": "Possible condition or 'Unable to determine from image'",
    "description": "Short educational explanation of the possible condition.",
    "medicines": [
        "Safe general information about treatment categories or advice to consult a doctor."
    ],
    "precautions": [
        "Safe precaution 1",
        "Safe precaution 2",
        "Safe precaution 3"
    ],
    "diet": [
        "General healthy lifestyle/diet advice 1",
        "General healthy lifestyle/diet advice 2",
        "General healthy lifestyle/diet advice 3"
    ],
    "doctor": "Recommended healthcare professional",
    "confidence": "Low / Moderate / High",
    "disclaimer": "This is an educational AI assessment and not a confirmed medical diagnosis."
}

FIELD REQUIREMENTS:

disease:
Give the most likely visible possibility, but clearly indicate
that it is only a possibility.

description:
Briefly explain the visible condition in simple language.

medicines:
Do NOT prescribe medication.
You may mention that a healthcare professional may consider
appropriate treatment after examination.

precautions:
Give practical, safe precautions relevant to the visible issue.

diet:
Give only general healthy diet and lifestyle suggestions.
Do not claim that a particular food cures the condition.

doctor:
Suggest the appropriate specialist, such as "Dermatologist",
when appropriate.

confidence:
Use only Low, Moderate, or High.

disclaimer:
Always include the medical disclaimer.

If the image does not clearly show a skin condition, return:

{
    "disease": "Unable to determine from image",
    "description": "The uploaded image does not provide enough information for a reliable assessment.",
    "medicines": [
        "Please consult a qualified healthcare professional for an appropriate evaluation."
    ],
    "precautions": [
        "Avoid scratching, squeezing, or irritating the affected area."
    ],
    "diet": [
        "Maintain a balanced diet and adequate hydration."
    ],
    "doctor": "Dermatologist",
    "confidence": "Low",
    "disclaimer": "This is an educational AI assessment and not a confirmed medical diagnosis."
}
"""

    # =================================================
    # SEND IMAGE TO GEMINI
    # =================================================

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[
            {
                "inline_data": {
                    "mime_type": content_type,
                    "data": encoded_image
                }
            },
            prompt
        ]
    )

    # =================================================
    # GET GEMINI RESPONSE
    # =================================================

    result_text = response.text.strip()

    # Gemini sometimes returns JSON inside ```json ... ```
    if result_text.startswith("```"):
        result_text = result_text.replace("```json", "")
        result_text = result_text.replace("```", "")
        result_text = result_text.strip()

    # =================================================
    # CONVERT JSON TEXT TO PYTHON DICTIONARY
    # =================================================

    try:

        result = json.loads(result_text)

    except json.JSONDecodeError:

        # Fallback if Gemini returns unexpected text
        result = {
            "disease": "AI analysis available",
            "description": result_text,
            "medicines": [
                "Please consult a qualified healthcare professional "
                "before using any medication."
            ],
            "precautions": [
                "Avoid scratching, squeezing, or irritating "
                "the affected area."
            ],
            "diet": [
                "Maintain a balanced diet and adequate hydration."
            ],
            "doctor": "Dermatologist",
            "confidence": "Low",
            "disclaimer": (
                "This is an educational AI assessment and not "
                "a confirmed medical diagnosis."
            )
        }

    # =================================================
    # MAKE SURE ALL REQUIRED FIELDS EXIST
    # =================================================

    result.setdefault(
        "disease",
        "Unable to determine from image"
    )

    result.setdefault(
        "description",
        "Please consult a qualified healthcare professional."
    )

    result.setdefault(
        "medicines",
        [
            "Consult a healthcare professional before using medication."
        ]
    )

    result.setdefault(
        "precautions",
        [
            "Avoid scratching, squeezing, or irritating the area."
        ]
    )

    result.setdefault(
        "diet",
        [
            "Maintain a balanced diet and adequate hydration."
        ]
    )

    result.setdefault(
        "doctor",
        "Dermatologist"
    )

    result.setdefault(
        "confidence",
        "Low"
    )

    result.setdefault(
        "disclaimer",
        "This is an educational AI assessment and not a confirmed medical diagnosis."
    )

    return result