import json, requests, os

API_KEY = os.getenv("DS_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
        }

def generate_product_description(product_name, product_features):
    messages = [{
        "role": "user",
        "content": f"Generate a compelling product description for a product named '{product_name}' with the following features: {product_features}."
    }]

    data = {
            "model": "deepseek-chat",
            'messages': messages,
            'max_tokens': 150, # Adjust the maximum length based on your preference
            'temperature': 0.7 # Adjust temperature for creativity
            }
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        print("complete response:", response.text)
        return None
    except KeyError:
        print("Error: 'text' key not found in the API response.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        print("raw response:", response_data)
        return None

   
# Example Usage
product_name = "Wireless Noise-Canceling Headphones"
product_features = "Active noise cancellation, Bluetooth 5.0, 20-hour battery life, comfortable earcups"
description = generate_product_description(product_name, product_features)

if description:
    print("Product Description:\n", description)
