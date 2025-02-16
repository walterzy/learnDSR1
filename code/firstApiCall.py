import json, requests, os

API_KEY = os.getenv("DS_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
    }

messages = [{
    "role": "user",
    "content": f"Write a short story about a robot that learns to love."
}]

data = {
    "model": "deepseek-chat",
    'messages': messages,
    'max_tokens': 150, # Adjust the maximum length based on your preference
    'temperature': 0.7 # Adjust temperature for creativity
}

try:
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
    response_data = response.json()
    if 'text' in response_data:
        generated_text = response_data['text']
        print("Generated Story:\n", generated_text)
    else:
        print("Error: 'text' key not found in the API response.")
except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
