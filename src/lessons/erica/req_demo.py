import requests

response = requests.get("https://bbc.com")
print(response.content)
print(response.text)
