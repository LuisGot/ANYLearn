import os
import requests
from dotenv import load_dotenv
load_dotenv()

def send_discord_message(content: str) -> None:
    """
    Send a message to a Discord webhook
    """
    webhook_url = os.environ["DISCORD_WEBHOOK"]
    headers = {"Content-Type": "application/json"}

    # Split the message into multiple messages if it exceeds 2000 characters
    max_chars = 2000
    messages = [content[i:i + max_chars] for i in range(0, len(content), max_chars)]

    for message in messages:
        data = {"content": message}
        try:
            response = requests.post(webhook_url, json=data, headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
            print("Successfully sent to Discord")
        except requests.exceptions.RequestException as e:
            print(f"Error sending to Discord: {e}")

