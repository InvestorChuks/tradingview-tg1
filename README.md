# TradingView Alerts to Telegram Bot

This is a lightweight Flask backend that receives TradingView webhook alerts and forwards them to a Telegram group or channel.

## How It Works

1. TradingView sends a POST webhook to this backend.
2. The backend parses the message and relays it to a Telegram chat via bot API.

## Deploying to Render

- Create a new **Web Service** from this GitHub repo
- Use **Python 3.x** runtime
- Add environment variables:
  - `TELEGRAM_TOKEN`: Bot token from @BotFather
  - `TELEGRAM_CHAT_ID`: Chat ID of your target group/channel
- Render will auto-detect the `Procfile` and run `python main.py`

## Webhook URL

Use the following URL in your TradingView alerts:
https://tradingview-tg1.onrender.com

## Webhook Message Format (JSON)

   json
{
  "ticker": "{{ticker}}",
  "timeframe": "15m",
  "signal": "{{strategy.order.comment}}"
} 


## Sample Telegram Output
Signal Alert
Pair: BTCUSDT
Timeframe: 15m
Signal: Buy Signal

## License
MIT