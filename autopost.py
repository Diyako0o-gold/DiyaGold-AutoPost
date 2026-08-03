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
"""

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "mistralai/mistral-7b-instruct:free",
    "messages": [
        {
            "role": "user",
            "content": PROMPT
        }
    ]
}

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=data
)

print("Status:", response.status_code)
print("Response:", response.text)

if response.status_code != 200:
    raise Exception(response.text)

result = response.json()
text = result["choices"][0]["message"]["content"]

telegram = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": text
    }
)

print("Telegram:", telegram.status_code)
print("Done!")
