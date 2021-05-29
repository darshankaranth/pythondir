import sys
import requests
import json

def main():
    headers = {
            'Content-Type' : 'application/json'
            }
    s = requests.Session()
    r = s.get('https://vco7-sin1.velocloud.net', headers=headers)
    print(r)


if __name__ == '__main__':
    main()