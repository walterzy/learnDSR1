# Please install OpenAI SDK first: `pip3 install openai`

# key for: LearnDSR120250210
# sk-dc8a218f20ce43328d2b7eab7ef27162

from openai import OpenAI

proxy_servers = {
   'http': 'http://10.158.100.3:8080',
   'https': 'https://10.158.100.3:8080',
}


client = OpenAI(api_key="sk-dc8a218f20ce43328d2b7eab7ef27162", 
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

