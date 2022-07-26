from bs4 import BeautifulSoup
import requests
url = "https://www.bbc.com/"
req = requests.get(url)
print(req.text)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)
