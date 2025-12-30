import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def get_gold_price_per_mg():
    url = "https://www.goodreturns.in/gold-rates/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # 24K gold price per gram
    price_text = soup.find("td", class_="gold-rate-24k").text
    price_per_gram = float(price_text.replace("₹", "").replace(",", "").strip())

    # Convert gram → mg
    price_per_mg = price_per_gram / 1000

    return round(price_per_mg, 2)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload, timeout=10)

price_mg = get_gold_price_per_mg()
today = datetime.now().strftime("%d %b %Y")

message = (
    f"🟡 Gold Locker Update\n\n"
    f"📅 Date: {today}\n"
    f"💰 24K Gold Price\n"
    f"₹{price_mg} per mg\n\n"
    f"(Like Google Pay Gold Locker)"
)

send_telegram_message(message)
