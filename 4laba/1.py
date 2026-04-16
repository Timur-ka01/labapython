import requests
import time



def limit_calls(x):
    last_call = 0

    def wrapper(*args, **kwargs):
        nonlocal last_call
        now = time.time()

        if now - last_call < 2:
            print('погоди')
            return None
        last_call = now
        return x(*args, **kwargs)

    return wrapper

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


print(f('https://dogapi.dog/api/v2/facts'))
time.sleep(1)
print(f('https://dogapi.dog/api/v2/facts'))
time.sleep(3)
print(f('https://dogapi.dog/api/v2/facts'))
