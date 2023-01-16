import requests
import sys

def loop():
    for word in sys.stdin:
        response = requests.get(url=f"http://10.10.11.161/{word}")
        if response.status_code == 404:
            loop()
        else:
            data_extrected = response.json()    
            print(data_extrected)
loop()       

# the IP is from HackTheBox machine called backend.