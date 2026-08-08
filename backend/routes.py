from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required

from extensions import bcrypt
from models import db, User

print("Loading AI modules...")

from predictor.predictor import predict
from chatbot.chatbot import ask_chatbot
from medicines.medicine_service import get_medicine

print("AI modules loaded.")

api = Blueprint("api", __name__)


# =====================================================
# REGISTER
# =====================================================
@api.route("/register", methods=["POST"])
def register():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "No JSON received"
            }), 400

        name = data.get("name", "").strip()
        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        if not name or not email or not password:
            return jsonify({
                "success": False,
                "message": "All fields are required"
            }), 400

        if User.query.filter_by(email=email).first():
            return jsonify({
                "success": False,
                "message": "Email already exists"
            }), 409

        hashed = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(
            name=name,
            email=email,
            password=hashed
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Registration Successful"
        }), 201

    except Exception as e:
        db.session.rollback()

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# =====================================================
# LOGIN
# =====================================================
@api.route("/login", methods=["POST"])
def login():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "No JSON received"
            }), 400

        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        if not email or not password:
            return jsonify({
                "success": False,
                "message": "Email and Password required"
            }), 400

        user = User.query.filter_by(email=email).first()

        if user is None:
            return jsonify({
                "success": False,
                "message": "Invalid Email"
            }), 401

        if not bcrypt.check_password_hash(user.password, password):
            return jsonify({
                "success": False,
                "message": "Wrong Password"
            }), 401

        token = create_access_token(identity=str(user.id))

        return jsonify({
            "success": True,
            "token": token,
            "name": user.name
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# =====================================================
# DASHBOARD
# =====================================================
@api.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():

    return jsonify({
        "success": True,
        "message": "Welcome to AI Healthcare Assistant"
    })


# =====================================================
# DISEASE PREDICTION
# =====================================================
# =====================================================
# DISEASE PREDICTION
# =====================================================
@api.route("/predict", methods=["GET", "POST"])
def predict_route():

    # Browser request
    if request.method == "GET":
        return jsonify({
            "success": True,
            "message": "Predict API is working.",
            "how_to_use": "Send a POST request with symptoms.",
            "example": {
                "url": "http://127.0.0.1:5000/predict",
                "method": "POST",
                "body": {
                    "symptoms": [
                        "fever",
                        "cough",
                        "fatigue"
                    ]
                }
            }
        })

    # POST request
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "No JSON received"
            }), 400

        symptoms = data.get("symptoms")

        if not symptoms:
            return jsonify({
                "success": False,
                "message": "Symptoms are required"
            }), 400

        result = predict(symptoms)

        return jsonify({
            "success": True,
            "result": result
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

# =====================================================
# AI CHATBOT
# =====================================================
@api.route("/chat", methods=["POST"])
def chatbot():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "reply": "No JSON received"
            }), 400

        message = data.get("message", "")

        reply = ask_chatbot(message)

        return jsonify({
            "success": True,
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "reply": str(e)
        }), 500


# =====================================================
# MEDICINE
# =====================================================
@api.route("/medicine", methods=["POST"])
def medicine():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "No JSON received"
            }), 400

        disease = data.get("disease", "")

        result = get_medicine(disease)

        return jsonify({
            "success": True,
            "result": result
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# =====================================================
# HEALTH CHECK
# =====================================================
@api.route("/health", methods=["GET"])
def health():

    return jsonify({
        "success": True,
        "message": "Backend Running"
    })


print("All routes successfully registered.")