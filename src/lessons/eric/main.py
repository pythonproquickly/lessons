import requests
from bs4 import BeautifulSoup
from loguru import logger

# TODO: Run each hour

PREFIX = 'http://www.carreradepuntos.com/index.php/en/'
HEADER_CHECK_VALUE = 'Puesto'

urls = {
    'holdem_1_url': 
        {
            'rows': [], 
            'url': PREFIX + "current-month/1ra-carrera/hold-emxxx"},
    'holdem_2_url': 
        {
            'rows': [], 
            'url': PREFIX + "current-month/2da-carrera-2/hold-em"},
    'omaha_1_url': 
        {
            'rows': [], 
            'url': PREFIX + "current-month/1ra-carrera/omaha"},
    'omaha_2_url': 
        {
            'rows': [], 
            'url': PREFIX + "current-month/2da-carrera-2/omaha"},
    'tlb_1_url': 
        {
            'rows': [], 
            'url': PREFIX + "tournaments-leaderboard/1"},
    'tlb_2_url': 
        {
            'rows': [], 
            'url': PREFIX + "tournaments-leaderboard/2nd-race"},
}

fields = ['Place', 'Name', 'Points', 'Prize(USDT)']


def process_urls(url_dict):
    for key, value in url_dict.items():
        # TODO: put historical results/archive in place
        response = requests.get(value['url'])
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.info(e)
        else:
            response = requests.get(value['url'])
            soup = BeautifulSoup(response.content, features="lxml")
            page = soup.find_all('div', class_='page-header')

            # Race Title - need to add this to the output
            title = page[0].find('h2').text.strip()
            results = soup.find_all('table')
            rake_table = results[1]
            table_rows = rake_table.find_all('tr')

            # not used (this may work better if we output dictionaries and use this as a dict key)
            #race_name = 'f{key}'

            # Pull all rows as list items
            urls[key]['rows'] = [table_rows[i].text.strip().split('\n') 
                                 for i in range(len(table_rows)) 
                                 if len(table_rows[i].text.strip().split('\n')) >= 4]


def make_table(headers, data):
    maxn = []
    maxn.append(7)
    maxn.append(15)
    maxn.append(12)
    maxn.append(32)
    for n in data:
        if n[0] == HEADER_CHECK_VALUE:
            print()
            print()
            print(f"{'**LEVEL**'.center(sum(maxn) + 13 - 4)}")
            print()
            print(f"| {headers[0]}{' ' * (maxn[0] - len(headers[0]))} | {headers[1]}{' ' * (maxn[1] - len(headers[1]))} | {' ' * (maxn[2] - len(headers[2]))}{headers[2]} | {' ' * (maxn[3] - len(headers[3]))}{headers[3]} |")
            print(f"{'-' * (sum(maxn) + 13)}")
        else:
            print(f"| {n[0]}{' ' * (maxn[0] - len(n[0]))} | {n[1]}{' ' * (maxn[1] - len(n[1]))} | {' ' * (maxn[2] - len(n[2]))}{n[2]} | {' ' * (maxn[3] - len(n[3]))}{n[3].replace(',','.')} |")


#TODO: Add the Bronze, Silver, Gold (iterator?)
#TODO: Replace ticet names with a ticket value or english name

def main():
    process_urls(urls)
    make_table(fields, urls['omaha_1_url']['rows'])


if __name__ == "__main__":
    main()


# for race in races:
#     print('|PLACE|PLAYER|POINTS|PRIZE|')
#     for i in race:
#         print(f'|{i[0]}|{i[1]}|{i[2]}|{i[3]}|')
