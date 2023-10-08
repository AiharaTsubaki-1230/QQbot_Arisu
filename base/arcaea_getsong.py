import requests
from bs4 import BeautifulSoup

song_list = []

html = requests.get("https://zh.moegirl.org.cn/Phigros/%E6%9B%B2%E7%9B%AE%E5%88%97%E8%A1%A8")

text = html.content
soup = BeautifulSoup(text, 'lxml')

trs = soup.find_all('tr')

content = ""
list_of_song = []

for tr in trs:
    td_list = tr.find_all('td')
    if len(td_list) <= 1:
        continue
    td = td_list[0].string
    if td == None or td == "DX":
        continue
    if td[:2] == "20":
        td = td_list[1].string
    if td == None or td == "DX":
        continue
    if td.isascii() == False:
        continue
    if td in list_of_song:
        continue
    list_of_song.append(td)
    content += td + "\n"

open("./src/guess_song/phi.txt", "w").write(content)