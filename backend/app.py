from flask import Flask
from flask_cors import CORS
import os

# Routes
from routes_public import public_bp
from routes_i18n import i18n_bp
from routes_wallet import wallet_bp
from routes_admin import admin_bp

app = Flask(__name__)
CORS(app)

# -----------------------------
# CONFIG ENVIRONMENT VARIABLES
# -----------------------------
app.config['PAYMENT_ADDRESS'] = os.getenv(
    "PAYMENT_ADDRESS",
    "0xfee37e7e64d70f37f96c42375131abb57c1481c2"
)

app.config['POLYGON_RPC_URL'] = os.getenv(
    "POLYGON_RPC_URL",
    "https://polygon-rpc.com"
)

app.config['ADMIN_SECRET'] = os.getenv(
    "ADMIN_SECRET",
    "CHANGE_ME_ADMIN_SECRET"
)

app.config['USDT_CONTRACT_ADDRESS'] = os.getenv(
    "USDT_CONTRACT_ADDRESS",
    "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"   # USDT (Polygon)
)

# -----------------------------
# REGISTER BLUEPRINTS
# -----------------------------
app.register_blueprint(public_bp, url_prefix="/api/public")
app.register_blueprint(i18n_bp, url_prefix="/api/i18n")
app.register_blueprint(wallet_bp, url_prefix="/api/payment")
app.register_blueprint(admin_bp, url_prefix="/api/admin")


# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.route("/")
def home():
    return {"status": "AUREA TRADE backend running"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
