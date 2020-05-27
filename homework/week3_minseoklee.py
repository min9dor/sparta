import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, "html.parser")

# body-content > div.newest-list > div > table > tbody > tr.list > td.number
# body-content > div.newest-list > div > table > tbody > tr.list > td.info > a.title.ellipsis
# body-content > div.newest-list > div > table > tbody > tr.list > td.info > a.artist.ellipsis

songs = soup.select("#body-content > div.newest-list > div > table > tbody > tr.list")

for song in songs:
    rank = song.select_one("td.number").text[0:2].strip()
    title = song.select_one("td.info > a.title.ellipsis").text.strip()
    artist = song.select_one("td.info > a.artist.ellipsis").text
    print(rank, title, artist)