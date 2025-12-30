import os
import json
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]

def handler(request):
    update = request.json

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "Hello! Your bot is working 🎉"
            }
        )

    return {
        "statusCode": 200,
        "body": json.dumps({"ok": True})
    }
