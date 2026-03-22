import requests
import time

def f():
    def f1():
        r = requests.get('https://dogapi.dog/api/v2/facts')
        data = r.json()
        n = data['data'][0]['attributes']['body']
        return n
    return door()

def limit_calls(x):
    last_call = 0

    def wrapper():
        nonlocal last_call
        now = time.time()

        if now - last_call < 2:
            return
        last_call = now
        return x()

    return wrapper


decorationpi = limit_calls(pi)
print(decorationpi())

