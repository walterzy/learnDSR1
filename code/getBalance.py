import requests
import json
import os

api_key = os.getenv("DS_API_KEY")
url = "https://api.deepseek.com/user/balance"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() 
    balance_data = response.json()
    print (balance_data)
    print("current balance:", balance_data.get("balance_infos")[0]['total_balance'])
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except Exception as e:
    print(f"Request Failure: {e}")
