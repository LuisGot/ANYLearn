import os
import requests
from dotenv import load_dotenv
load_dotenv()

def send_discord_message(content):
    webhook_url = os.environ["DISCORD_WEBHOOK"]
    headers = {
        "Content-Type": "application/json"
    }

    # Split the message into multiple messages if it exceeds 2000 characters
    max_chars = 2000
    messages = [content[i:i + max_chars] for i in range(0, len(content), max_chars)]

    for message in messages:
        data = {
            "content": message
        }
        try:
            response = requests.post(webhook_url, json=data, headers=headers)
            print("successfully sent to discord")
        except requests.exceptions.RequestException as e:
            print(f"Error sending to Discord: {e}")
        else:
            if response.status_code != 204:
                print(f"Error sending to Discord: {response.text}")