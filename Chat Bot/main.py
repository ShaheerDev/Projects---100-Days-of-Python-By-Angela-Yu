import requests
import json
import tkinter as tk

if True:
    while True:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
        api_key = "AIzaSyD8TPaXNHhSRVIZebH06pOFtV2aBebMurA"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": input("What do you Want me to ask? \nUser: ")
                        }
                    ]
                }
            ]

        }

        response = requests.post(f"{url}?key={api_key}", headers=headers, json=data)
        print("Chat-Bot: ", response.json()["candidates"][0]["content"]["parts"][0]["text"])


