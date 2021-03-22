import requests

def makeUrl(text):
    url = text.replace(' ', '+')
    return url

searchtext = input("enter the condition: ")
url = makeUrl(searchtext)

res = requests.get(f"http://localhost:8000/{url}")
print(res.text)

