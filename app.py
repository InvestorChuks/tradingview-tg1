
import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    message = data.get("message", "TradingView Alert")
    send_telegram_alert(message)
    return jsonify({"status": "success"}), 200

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
