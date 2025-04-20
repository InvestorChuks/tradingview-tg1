
# TradingView Telegram Scanner

This app receives alerts from TradingView and sends them to a Telegram bot.

## Setup

1. Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
```

2. Set environment variables:

- `TELEGRAM_TOKEN`: Your Telegram bot token
- `TELEGRAM_CHAT_ID`: Your Telegram chat ID

3. Run the app:

```bash
python app.py
```

## Deployment

Deploy on Railway, Render, or Replit. Use `/webhook` as the endpoint for TradingView alerts.

## TradingView Alert Format

Set the webhook URL in your alert like:

```
https://your-deployment-url/webhook
```

Then use this in the alert message:

```json
{
  "message": "🔔 Alert: {{ticker}} {{interval}} - Buy Signal!"
}
```
