import re
from bs4 import BeautifulSoup

with open("likes.html", errors="ignore") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
artistList = []
trackList = []
artistName = []
trackName = []

# print(soup)
# soup = BeautifulSoup("<html>a web page</html>", 'html.parser')
tags = soup('div')
# for tag in soup.find_all('a', href=True):
for tag in soup.find_all('div', {'class': 'track-artist'}):
    # artistList.append(tag)
    # print(tag)
    artistList.append(tag)



# for tag in soup.find_all('div', {'class': 'track-name'}):
    # trackList.append(tag)
    # print(tag)

# for artist in artistList:
    # print(artist)
    # print(re.findall('<div class=\"track-artist\">(.*)</div>', artist))
    # print(tmpArtist)
    # print(artist)

# print(type(artistList))
print(artistList[0])
print(re.findall('<div class=\"track-artist\">(.*)</div>', artistList))

# print(trackList)
