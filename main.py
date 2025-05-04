
import requests
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def run_bot():
    while True:
        # Example message (this would be replaced with logic from your bot)
        send_message("تم رصد كسر مقاومة في SPX!")
        time.sleep(3600)  # send every hour just as a placeholder

if __name__ == "__main__":
    run_bot()
