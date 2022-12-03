import requests
from bs4 import BeautifulSoup

# create User-Agent (optional)
headers = {
    "User-Agent": "Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 ("
                  "KHTML, like Gecko) "
                  "Chrome/31.0.1650.0 Safari/537.36"}

response = requests.get("http://pythonjobs.github.io/", headers=headers)

webpage = response.content
soup = BeautifulSoup(webpage, "html.parser")

for job in soup.find_all('section', class_='job_list'):
    title = [a for a in job.find_all('h1')]
    for n, tag in enumerate(job.find_all('div', class_='job')):
        company_element = [x for x in tag.find_all('span', class_='info')]
        print("Job Title: ", title[n].text.strip())
        print("Location: ", company_element[0].text.strip())
        print("Company: ", company_element[3].text.strip())
        print()
