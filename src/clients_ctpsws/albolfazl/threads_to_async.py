import requests
from bs4 import BeautifulSoup
from threading import Thread
from pathlib import Path
import time

def webscraper(url):
    PATH = Path.cwd()/'webscraping'

    if not PATH.exists():
        Path.mkdir(PATH)
        
    response = requests.get(url)
    name = url[url.rfind('/')+1:-4]
    filename = PATH/f'{name}.pdf'
    
    with open (filename, 'wb') as f:
        f.write(response.content)

urls = [
        'https://web.engr.oregonstate.edu/~tgd/publications/nature-ecs-machine-learning.pdf',
        'https://www.ibm.com/downloads/cas/GB8ZMQZ3',
        'https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms/@@download/fullReport'
    ]
        
def multithread():
    threads = [Thread(target=webscraper, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def singlethread():
    for url in urls:
        webscraper(url)
    
if __name__ == '__main__':
    start = time.perf_counter()
    singlethread()
    end = time.perf_counter()
    print(f'Took {end-start} seconds')
