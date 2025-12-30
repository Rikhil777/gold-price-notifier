import requests
from datetime import datetime
import os

GOLD_API_KEY = os.getenv("goldapi-qsuhmsmjr6mocl-io")
BOT_TOKEN = os.getenv("8237637090:AAFusvBLzNsvKL40b9aKPYY5egJekBoW1TU")
CHAT_ID = os.getenv("1856690962")

def get_gold_price():
    url = "https://www.goldapi.io/api/XAU/INR"
    headers = {
        "x-access-token": GOLD_API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers, timeout=10)
    data = response.json()
    price_per_gram = data["price"] / 31.1035
    return round(price_per_gram, 2)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload, timeout=10)

price = get_gold_price()
today = datetime.now().strftime("%d %b %Y")

message = (
    f"🟡 Gold Price Update\n\n"
    f"📅 Date: {today}\n"
    f"💰 24K Gold Price:\n"
    f"₹{price} per gram\n\n"
    f"(Approx Google Pay Gold rate)"
)

send_telegram_message(message)
