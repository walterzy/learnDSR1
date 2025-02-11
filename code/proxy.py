import requests, os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 代理配置
proxies = {"https": "http://10.158.100.3:8080"}

# API配置
API_KEY = os.getenv("DS_API_KEY")

url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "User-Agent": "MyApp/1.0"  # 明确声明User-Agent
}
data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello!"}]
}

# 配置重试和会话
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
        proxies=proxies,
        timeout=20,
        verify=True  # 生产环境必须启用SSL验证
    )
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as e:
    print(f"HTTP错误: {e.response.status_code} - {e.response.text}")
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
