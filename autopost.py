import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
API_KEY = os.getenv("OPENROUTER_API_KEY")

PROMPT = """
تو یک تحلیلگر حرفه‌ای بازارهای مالی هستی.

برای کانال تلگرام DiyaGold یک پست فارسی تولید کن.

شرایط:
- حدود 200 تا 300 کلمه
- شامل تحلیل کوتاه طلا (XAUUSD)
- تحلیل کوتاه بیت کوین
- یک نکته آموزشی ترید
- پایان با هشتگ‌های مرتبط
- متن جذاب و قابل انتشار
"""

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "meta-llama/llama-3.1-8b-instruct:free",
    "messages": [
        {
            "role": "user",
            "content": PROMPT
        }
    ]response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=data
)

print("Status:", response.status_code)
print("Response:", response.text)

response.raise_for_status()

text = response.json()["choices"][0]["message"]["content"]

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": text
    }
)

print("Message Sent Successfully")
