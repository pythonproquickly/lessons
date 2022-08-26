#!/usr/bin/env python
# coding: utf-8

# In[29]:


import requests
from bs4 import BeautifulSoup
import csv

# for translating the spanish
# from googletrans import Translator, constants
# from pprint import pprint


# In[15]:


# TODO: Run each hour


# In[27]:


urls = {
    'holdem_1_url': "https://www.carreradepuntos.com/index.php/en/current-month/1ra-carrera/hold-em",
    #'holdem_2_url': "https://www.carreradepuntos.com/index.php/en/current-month/2da-carrera-2/hold-em",
    'omaha_1_url': "https://www.carreradepuntos.com/index.php/en/current-month/1ra-carrera/omaha",
    #'omaha_2_url': "https://www.carreradepuntos.com/index.php/en/current-month/2da-carrera-2/omaha",
    'tlb_1_url': "https://www.carreradepuntos.com/index.php/en/tournaments-leaderboard/1",
    #'tlb_2_url': "https://www.carreradepuntos.com/index.php/en/tournaments-leaderboard/2nd-race",
}

holdem_1_url = []
holdem_2_url = []
omaha_1_url = []
omaha_2_url = []
tlb_1_url = []
tlb_2_url = []

races = [
    holdem_1_url,
    holdem_2_url,
    omaha_1_url,
    omaha_2_url,
    tlb_1_url,
    tlb_2_url,
]

fields = ['Place', 'Name', 'Points', 'Prize(USDT)']


def process_urls(url_dict):
    for key, value in url_dict.items():
        # TODO: add a check for if page exists
        # TODO: put historical results/archive in place
        response = requests.get(value)
        soup = BeautifulSoup(response.content)
        page = soup.find_all('div', class_='page-header')

        # Race Title - need to add this to the output
        title = page[0].find('h2').text.strip()

        results = soup.find_all('table')
        rake_table = results[1]
        table_rows = rake_table.find_all('tr')

        # not used (this may work better if we output dictionaries and use this as a dict key)
        race_name = 'f{key}'

        # Pull all rows as list items
        for i in range(len(table_rows)):
            if table_rows[i].text.strip().split('\n')[0] == 'Puesto':
                continue
            if len(table_rows[i].text.strip().split('\n')) < 4:
                continue
            if key == 'holdem_1_url':
                holdem_1_url.append(table_rows[i].text.strip().split('\n'))
            if key == 'holdem_2_url':
                holdem_2_url.append(table_rows[i].text.strip().split('\n'))
            if key == 'omaha_1_url':
                omaha_1_url.append(table_rows[i].text.strip().split('\n'))
            if key == 'omaha_2_url':
                omaha_2_url.append(table_rows[i].text.strip().split('\n'))
            if key == 'tlb_1_url':
                tlb_1_url.append(table_rows[i].text.strip().split('\n'))
            if key == 'tlb_2_url':
                tlb_2_url.append(table_rows[i].text.strip().split('\n'))


process_urls(urls)

for race in races:
    print(fields)
    for i in race:
        print(i)

# In[17]:

#
# # Can some of this be built as a function? (attempted above)
# # Loop through urls to get results for each? (attempted above)
#
# holdem_1_url = "https://www.carreradepuntos.com/index.php/en/current-month/1ra-carrera/hold-em"
# holdem_2_url = "https://www.carreradepuntos.com/index.php/en/current-month/2da-carrera-2/hold-em"
# omaha_1_url = "https://www.carreradepuntos.com/index.php/en/current-month/1ra-carrera/omaha"
# omaha_2_url = "https://www.carreradepuntos.com/index.php/en/current-month/2da-carrera-2/omaha"
# tlb_1_url = "https://www.carreradepuntos.com/index.php/en/tournaments-leaderboard/1"
# response = requests.get(tlb_1_url)
#
# # In[18]:
#
#
# soup = BeautifulSoup(response.content)
#
# # In[19]:
#
#
# # Get the Rake Race Title
#
# page = soup.find_all('div', class_='page-header')
# title = page[0].find('h2').text.strip()
# print(title)
#
# # In[6]:
#
#
# # Get the table elements
#
# results = soup.find_all('table')
# rake_table = results[1]
# table_rows = rake_table.find_all('tr')
#
# omaha_2nd_race = []
# # Pull all rows as list items
# for i in range(len(table_rows)):
#     if table_rows[i].text.strip().split('\n')[0] == 'Puesto':
#         continue
#     if len(table_rows[i].text.strip().split('\n')) < 4:
#         continue
#     omaha_2nd_race.append(table_rows[i].text.strip().split('\n'))
#
# fields = ['Place', 'Name', 'Points', 'Prize(USDT)']
#
# # In[7]:
#
#
# # Dump the data to file if needed for website updating
#
# with open('omaha_2nd_race.csv', 'w') as file:
#     write = csv.writer(file)
#     write.writerow(fields)
#     write.writerows(omaha_2nd_race)
#
# # In[ ]:
#
#
# # In[ ]:
