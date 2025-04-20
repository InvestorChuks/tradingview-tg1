import json
import logging
from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Load your configuration (e.g., list of coins)
with open("config.json", "r") as f:
    coin_config = json.load(f)["coins"]

# Telegram Config
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

logging.basicConfig(level=logging.INFO)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            logging.error("Telegram send failed: %s", response.text)
    except Exception as e:
        logging.exception("Exception sending Telegram message: %s", str(e))

@app.route("/alert", methods=["POST"])
def handle_alert():
    try:
        data = request.get_json(force=True)
        signal = data.get("signal", "No Signal")
        ticker = data.get("ticker", "Unknown")
        timeframe = data.get("timeframe", "Unknown")
        
        message = f"*Signal Alert*\nPair: `{ticker}`\nTimeframe: `{timeframe}`\nSignal: `{signal}`"
        send_telegram_message(message)
        return {"status": "ok"}, 200
    except Exception as e:
        logging.exception("Error handling alert")
        return {"error": str(e)}, 500

@app.route("/", methods=["GET"])
def home():
    return "Backend is Live!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
