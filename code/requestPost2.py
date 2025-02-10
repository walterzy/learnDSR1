import requests

DEEPSEEK_API_KEY = "sk-dc8a218f20ce43328d2b7eab7ef27162" 

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

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    print(response.json())
else:
    print(f"error code: {response.status_code}, response: {response.text}")

