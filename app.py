import os
from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# List of pairs you're monitoring (ensure this list matches your alert format)
pairs_to_scan = [
    "BTC/USDT”, “ETH/USDT”, “XRP/USDT”, “SOL/USDT”, “S/USDT”, “SUI/USDT”, “PENGU/USDT”,  “DOGE/USDT”, “TRX/USDT”, “RENDER/USDT”, “REI/USDT”, “ENS/USDT”, “SAND/USDT”, “GALA/USDT”, “ROSE/USDT”, “MANA/USDT”, “ALICE/USDT”, “LRC/USDT”, "TRUMP/USDT”, “XVG/USDT”, “UXLINK/USDT”, “VIRTUAL/USDT”, “AIXBT/USDT”, “SHIB/USDT”, “BEAMX/USDT”, “ACT/USDT”, “OP/USDT”, “CHR/USDT”, “ACE/USDT”, “RIF/USDT”, “LDO/USDT”, “PNUT/USDT”, “MAV/USDT”, “ARKM/USDT”, “ENA/USDT”, “BCH/USDT”, “LTC/USDT”, "BNB/USDT”, “XTZ/USDT”, “ATOM/USDT”, “VET/USDT”, “COMP/USDT”, “KAVA/USDT”, “RLC/USDT”, “MKR/USDT”, “DOT/USDT”, “YFI/USDT”, “CRV/USDT”, “UNI/USDT”, “ENJ/USDT”, “NEAR/USDT”, “AAVE/USDT”, “AXS/USDT”, “CHZ/USDT”, “RVN/USDT”, “COTI/USDT”, “EURUSD”, "XAUUSD”, “USOIL”, “GBPCHF”, “CADJPY”, “SPX”, “SFP/USDT”, “SPX/USDT”, “CYBER/USDT”, “DYM/USDT”, “BANANA/USDT”, “FLUX/USDT”, “NEO/USDT”, “ZIL/USDT”, “HBAR/USDT”,  # Add up to 100 pairs
    # ...
]

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        if not data:
            return "No JSON data received", 400

        # Extract alert message
        message = data.get("message", "")
        if not message:
            return "No message found in the alert", 400

        # Loop through pairs and find the one that matches in the alert
        for pair in pairs_to_scan:
            if pair in message:
                # Send the alert message to Telegram with the correct pair information
                send_telegram_message(f"Alert for {pair}: {message}")
                break

        return "Alert received and sent", 200

    except Exception as e:
        return f"Error: {str(e)}", 500

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)