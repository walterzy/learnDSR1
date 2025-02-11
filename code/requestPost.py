import requests, os

DEEPSEEK_API_KEY = os.getenv("DS_API_KEY")

url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
}
data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "how to resolve 404 error?"}
    ]
}

try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    response_data = response.json()

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"error code: {response.status_code}, response: {response.text}")

except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
except KeyError:
        print("Error: 'text' key not found in the API response.")
except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")

