import os
import requests
import argparse

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_http_session(retries=3, backoff_factor=0.5):
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["POST"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    
    session = requests.Session()
    session.mount("https://", adapter)
    return session

def call_deepseek_api(prompt, use_proxy=False, timeout=20):
    PROXY = os.getenv("DS_PROXY")
    proxies = {
        "https": {PROXY}
    } if use_proxy else None

    api_key = os.getenv("DS_API_KEY")
    if not api_key:
        raise ValueError("Not found DS_API_KEY")

    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "DeepSeekClient/1.0"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    session = create_http_session()
    try:
        response = session.post(
            url,
            headers=headers,
            json=payload,
            proxies=proxies,
            timeout=timeout,
            verify=True
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
        
    except requests.exceptions.HTTPError as e:
        print(f"API Request Failed [HTTP {e.response.status_code}]: {e.response.text}")
    except KeyError as e:
        print(f"Reponse resolving Failed: missing key fileds {e}")
    except requests.exceptions.RequestException as e:
        print(f"Network Reqeust Error: {str(e)}")
    finally:
        session.close()
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="To use proxy or not")
    parser.add_argument("-p", "--proxy", type=bool, help="use proxy or not", default=False)
    args = parser.parse_args()
    print(args.proxy)

    response = call_deepseek_api("Hello, how are you?", use_proxy=args.proxy)
    
    # response = call_deepseek_api("Please intro quant computing", use_proxy=True)
    
    if response:
        print("API Reponse Content:")
        print(response)
