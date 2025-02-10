import json, requests

API_KEY = "sk-dc8a218f20ce43328d2b7eab7ef27162" # Replace with your actual DeepSeek API Key
API_URL = "https://api.deepseek.com/v1/chat/completions" # Replace with your DeepSeek API Endpoint

headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
        }

def generate_product_description(product_name, product_features):
    prompt = f"Generate a compelling product description for a product named '{product_name}' with the following features: {product_features}."
    data = {
            "model": "deepseek-chat",
            'prompt': prompt,
            "messages": [
                {"role": "user", "content": "how to resolve 404 error?"}
            ]
            }
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_data = response.json()
        return response_data['text']
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
    except KeyError:
        print("Error: 'text' key not found in the API response.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None

   
# Example Usage
product_name = "Wireless Noise-Canceling Headphones"
product_features = "Active noise cancellation, Bluetooth 5.0, 20-hour battery life, comfortable earcups"
description = generate_product_description(product_name, product_features)

if description:
    print("Product Description:\n", description)
