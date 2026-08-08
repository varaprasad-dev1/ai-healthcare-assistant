from flask import Flask, jsonify
from flask_cors import CORS


import config

from extensions import db, bcrypt, jwt

app = Flask(__name__)

# ==========================================
# Configuration
# ==========================================
app.config.from_object(config)

# ==========================================
# Enable CORS
# ==========================================
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True
)

# ==========================================
# Initialize Extensions
# ==========================================
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# ==========================================
# Register Blueprint
# ==========================================
from routes import api

app.register_blueprint(api)

# ==========================================
# Create Database Tables
# ==========================================
with app.app_context():
    db.create_all()

# ==========================================
# Home Route
# ==========================================
@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "success": True,
        "message": "AI Healthcare Assistant Backend Running"
    })

# ==========================================
# Run Flask
# ==========================================
if __name__ == "__main__":

    print("\n========== REGISTERED ROUTES ==========\n")

    for rule in sorted(app.url_map.iter_rules(), key=lambda r: r.rule):
        print(f"{rule.rule:25} -> {rule.endpoint}")

    print("\n=======================================\n")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )