from fastapi import FastAPI, Request
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    async with httpx.AsyncClient() as client:
        await client.post(url, json=payload)

@app.get("/")
async def root():
    return {"message": "Bot is alive."}

@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()

        pair = data.get("pair", "Unknown Pair")
        timeframe = data.get("timeframe", "Unknown Timeframe")
        signal = data.get("signal", "Unknown Signal")

        message = f"**TradingView Alert**\nPair: `{pair}`\nTimeframe: `{timeframe}`\nSignal: *{signal}*"
        await send_telegram_message(message)

        return {"message": "Alert sent to Telegram"}

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}
