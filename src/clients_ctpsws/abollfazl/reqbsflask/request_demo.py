import requests

response = requests.get("https://twitter.com/tweets/")

print(response.text[:100])  # parseable
print(response.url)
print(response.status_code)
print(response.encoding)
print(response.elapsed)
# http protocol
