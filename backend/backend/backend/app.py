from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSLATIONS_DIR = os.path.join(BASE_DIR, "translations")

# ==========================================
#   LOAD TRANSLATIONS
# ==========================================
def load_translation(lang):
    file_path = os.path.join(TRANSLATIONS_DIR, f"{lang}.json")
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ==========================================
#   API: GET TRANSLATION
# ==========================================
@app.route("/api/translation/<lang>", methods=["GET"])
def get_translation(lang):
    data = load_translation(lang)
    if data is None:
        return jsonify({"error": "Language file not found"}), 404
    return jsonify(data)


# ==========================================
#   API: UPDATE TRANSLATION (ADMIN)
# ==========================================
@app.route("/api/admin/update", methods=["POST"])
def admin_update():
    body = request.json

    lang = body.get("lang")
    updated = body.get("data")

    if not lang or not updated:
        return jsonify({"error": "Missing data"}), 400

    file_path = os.path.join(TRANSLATIONS_DIR, f"{lang}.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(updated, f, ensure_ascii=False, indent=4)

    return jsonify({"status": "updated"})


# ==========================================
#   API: WALLET CONNECT – Register Session
# ==========================================
@app.route("/api/wc/session", methods=["POST"])
def wc_session():
    """
    Фронтендът изпраща WalletConnect session info.
    Backend просто го логва / приема.
    """
    data = request.json
    return jsonify({"received": True, "session": data})


# ==========================================
#   API: WALLET CONNECT – Verify Signature
# ==========================================
@app.route("/api/wc/verify", methods=["POST"])
def wc_verify():
    """
    Фронтендът изпраща: address, message, signature
    Backend може да валидира ако е нужно (по избор).
    Тук просто връщаме потвърждение.
    """
    data = request.json
    return jsonify({"verified": True, "data": data})


# ==========================================
#   RUN
# ==========================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
  
