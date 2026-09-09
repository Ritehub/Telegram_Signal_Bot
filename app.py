from flask import Flask, request
import requests
import os

app = Flask(__name__)

# REPLACE THESE WITH YOUR ACTUAL VALUES
TELEGRAM_BOT_TOKEN = "8935439324:AAFrBNEZIEjMboD8RYxU1rSpCgJoYp8dc5U"
TELEGRAM_CHAT_ID = "8935439324"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{8935439324:AAFrBNEZIEjMboD8RYxU1rSpCgJoYp8dc5U}/sendMessage"
    payload = {"chat_id": 8935439324, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    if not data:
        return "No data received", 400

    if data.get('stage') == 1:
        msg = (
            f"🟡 *STAGE 1: SETUP FORMED [{data.get('symbol')}]*\n\n"
            f"• *Bias:* {data.get('bias')}\n"
            f"• *1H FVG Zone:* `{data.get('fvg_bottom')} - {data.get('fvg_top')}`\n"
            f"• *Key Entry Level (50% CE):* `{data.get('key_level')}`\n"
            f"• *Stop Loss (SL):* `{data.get('sl')}`\n"
            f"• *Target TP1 (1:{data.get('rrr1')} RRR):* `{data.get('tp1')}`\n"
            f"• *Target TP2 (1:{data.get('rrr2')} RRR):* `{data.get('tp2')}`\n\n"
            f"⏳ _Awaiting price retest into ${data.get('key_level')}..._"
        )
        send_telegram(msg)
        
    elif data.get('stage') == 2:
        msg = (
            f"🟢 *STAGE 2: DIRECT ENTRY TRIGGERED [{data.get('symbol')}]*\n\n"
            f"• *Action:* {data.get('action')} LIMIT RETEST\n"
            f"• *Entry Price:* `{data.get('entry')}`\n"
            f"• *Stop Loss:* `{data.get('sl')}`\n"
            f"• *Take Profit 1:* `{data.get('tp1')}` (1:{data.get('rrr1')} RRR)\n"
            f"• *Take Profit 2:* `{data.get('tp2')}` (1:{data.get('rrr2')} RRR)\n\n"
            f"🚀 _Price hit the 50% FVG Key Level. Trade active!_"
        )
        send_telegram(msg)
        
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
