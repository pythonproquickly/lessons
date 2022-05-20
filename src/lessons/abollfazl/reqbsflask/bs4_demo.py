from bs4 import BeautifulSoup
import requests
import datetime

response = requests.get("https://bbc.com")

soup = BeautifulSoup(response.text, "html.parser")

print(f"{soup.title.string} main stories on {datetime.datetime.now()}")

for num, story in enumerate(soup.find_all("div", {"class": "media block-link"})):
    print(f"{num + 1}. {story.get('data-bbc-title').strip()}")
