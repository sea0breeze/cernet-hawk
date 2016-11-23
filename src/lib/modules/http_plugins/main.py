import requests

def scan(ip):
    url = ip
    r = requests.get(ip)
    r.headers