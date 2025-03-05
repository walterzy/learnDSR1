import requests
import json
import os

api_key = os.getenv("DS_API_KEY")
url = "https://api.deepseek.com/beta/completions"

payload = json.dumps({
  "model": "deepseek-chat",
  "prompt": "Once upon a time, ",
  "echo": False,
  "frequency_penalty": 0,
  "logprobs": 0,
  "max_tokens": 1024,
  "presence_penalty": 0,
  "stop": None,
  "stream": False,
  "stream_options": None,
  "suffix": None,
  "temperature": 1,
  "top_p": 1
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  "Authorization": f"Bearer {api_key}",
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

