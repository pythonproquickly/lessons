DIR = "/Users/andy/ws/ctpsws-clients/lessons/src/lessons/jennniferj/assign8/"
import requests
import pandas as pd

with open(f"{DIR}api.key", "r") as k:
    api_key = k.readline().strip()

url = f"https://www.omdbapi.com/?apikey={api_key}&i="
movie_content = []
with open(f"{DIR}oscar_winners.csv", "r") as a:
    for index, line in enumerate(a):
        if index == 0:
            continue
        omdb = line.strip().split(",")[1]
        url_to_fetch = url + omdb
        r = requests.get(url_to_fetch)
        movie_content.append(r.json())

clean_data = []
for line in movie_content:
    title = line["Title"]
    runtime_mins = int(line["Runtime"].split(" ")[0])
    genre = line["Genre"]
    wins_nominations = line["Awards"].split(".")[1]
    wins_nominations = wins_nominations.split("&")
    wins = int(wins_nominations[0].strip().split(" ")[0])
    nominations = int(wins_nominations[1].strip().split(" ")[0])
    box_office_dollars = int(line["BoxOffice"][1:].replace(",", ""))
    clean_data.append(
        [title, runtime_mins, genre, wins, nominations, box_office_dollars]
    )


movies = pd.DataFrame(clean_data)
