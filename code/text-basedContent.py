import json, requests, os

API_KEY = os.getenv("DS_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
    }

def generate_content(prompt, max_tokens=200, temperature=0.8):
    """
    Generates text content using DeepSeek R1 based on the provided prompt.
    Parameters:
    prompt (str): The prompt to send to DeepSeek R1.
    max_tokens (int): The maximum length of the generated text.
    temperature (float): Controls the randomness of the output.
    Returns:
    str: The generated text or an error message.
    """

    messages = [{
        "role": "user",
        "content": f"{prompt}",
    }]

    data = {
        "model": "deepseek-chat",
        'messages': messages,
        'max_tokens': max_tokens, # Adjust the maximum length based on your preference
        'temperature': temperature, # Adjust temperature for creativity
    }

    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_data = response.json()

        if response.status_code == 200:
            # print(response.json())
            content = response_data['choices'][0]['message']['content']
            # print(content)
            return content
        else:
            print(f"error code: {response.status_code}, response: {response.text}")
    except requests.exceptions.RequestException as e:
        return f"Error making API request: {e}"
    except json.JSONDecodeError as e:
        return f"Error decoding JSON response: {e}"

def main():
    """
    Main function to run the text-based content generator.
    """
    while True:
        user_prompt = input("Enter your prompt (or 'exit' to quit): ")
        if user_prompt.lower() == 'exit':
            break
        max_tokens_input = input("Enter max tokens (default is 200): ")
        temperature_input = input("Enter temperature (default is 0.8): ")

        try:
            max_tokens = int(max_tokens_input) if max_tokens_input else 200
            temperature = float(temperature_input) if temperature_input else 0.8
        except ValueError:
            print("Invalid input. Using default values.")
            max_tokens = 200
            temperature = 0.8

        generated_text = generate_content(user_prompt, max_tokens, temperature)
        print("Generated Text:\n", generated_text)

if __name__ == "__main__":
    main()
