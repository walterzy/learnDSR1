# Please install OpenAI SDK first: `pip3 install openai`

import os
from openai import OpenAI

API_KEY = os.getenv("DS_API_KEY")

client = OpenAI(api_key=f'{API_KEY}', 
                base_url="https://api.deepseek.com")

response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                        {"role": "system", "content": "You are a helpful assistant"},
                        {"role": "user", "content": "Hello"},
                    ],
            stream=False,
            )

print(response.choices[0].message.content)

