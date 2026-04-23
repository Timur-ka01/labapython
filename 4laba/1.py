import requests
import time
from functools import wraps

def limit_calls(delay=2):
    def decorator(func):
        last_call = 0
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.time()
            
            if now - last_call < delay:
                print(f'погоди {delay} сек')
                return None
            
            last_call = now
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


@limit_calls()
def get_fact(url):
    r = requests.get(url)
    data = r.json()
    n = data['data'][0]['attributes']['body']
    return n


@limit_calls(delay=1)
def countdown(n):
    if n <= 0:
        return "Готово"
    print(n)
    time.sleep(0.5)
    return countdown(n - 1)


url = 'https://dogapi.dog/api/v2/facts'
print(get_fact(url))
time.sleep(1)
print(get_fact(url))
time.sleep(3)
print(get_fact(url))

print(countdown(5))