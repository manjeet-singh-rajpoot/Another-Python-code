import requests
r=requests.get("https//api.github.com//users/havenke")
print(r)
print(r.content)
