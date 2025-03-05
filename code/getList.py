import requests
import os

api_key = os.getenv("DS_API_KEY")
url = "https://api.deepseek.com/models"

payload={}
headers = {
  'Accept': 'application/json',
  "Authorization": f"Bearer {api_key}",
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

