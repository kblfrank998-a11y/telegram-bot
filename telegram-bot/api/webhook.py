import os
import json
import requests

def handler(request):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    if not BOT_TOKEN:
        return {
            "statusCode": 500,
            "body": "BOT_TOKEN not set"
        }

    update = request.get_json()

    if not update:
        return {"statusCode": 200, "body": "no data"}

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
