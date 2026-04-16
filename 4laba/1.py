import requests
import time
from functools import wraps

def limit_calls(x=None, delay=2):
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
    
    if x is None:
        return decorator
    else:
        return decorator(x)


@limit_calls
def get_fact(url):
    r = requests.get(url)
    data = r.json()
    n = data['data'][0]['attributes']['body']
    return n


<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 971e8e6f93bc0ccc3d2798cd0f5b2c5f3ce67675
@limit_calls
def f(url):
    def f1():
        r = requests.get(url)
        data = r.json()
        n = data['data'][0]['attributes']['body']
        return n
    return f1


<<<<<<< HEAD
=======
>>>>>>> 97cd910331d8b6215852ee3901dd11f4e1a050cf
>>>>>>> 971e8e6f93bc0ccc3d2798cd0f5b2c5f3ce67675
p = f('https://dogapi.dog/api/v2/facts')
=======
url = 'https://dogapi.dog/api/v2/facts'
print(get_fact(url))
time.sleep(1)
print(get_fact(url))
time.sleep(3)
print(get_fact(url))


@limit_calls(delay=1)
def countdown(n):
    if n <= 0:
        return "Готово"
    print(n)
    time.sleep(0.5)
    return countdown(n - 1)
>>>>>>> 4ac0866e370981904f7e3368d798315b48397d17


print(countdown(5))