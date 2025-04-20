
import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.post("/webhook")
async def webhook(request: request):
    try:
        data = await request.json()

        # Extract the fields from the TradingView alert JSON
        pair = data.get("pair", "Unknown Pair")
        timeframe = data.get("timeframe", "Unknown Timeframe")
        signal = data.get("signal", "Unknown Signal")

        # Format the message
        message = f"**TradingView Alert**\nPair: `{pair}`\nTimeframe: `{timeframe}`\nSignal: *{signal}*"

        # Send to Telegram
        send_telegram_message(message)
        return {"message": "Alert sent to Telegram"}

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}


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
