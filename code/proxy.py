import requests, os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

proxies = {"https": "http://10.158.100.3:8080"}
API_KEY = os.getenv("DS_API_KEY")

url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "User-Agent": "MyApp/1.0"
}
data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello!"}]
}

retry = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=retry)

session = requests.Session()
session.mount("https://", adapter)

try:
    response = session.post(
        url,
        headers=headers,
        json=data,
#        proxies=proxies,
        timeout=20,
        verify=True
    )
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
except requests.exceptions.RequestException as e:
    print(f"Request failure: {e}")
