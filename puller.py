import re
from bs4 import BeautifulSoup

with open("likes.html", errors="ignore") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
artistList = []
trackList = []
artistName = []
trackName = []

tags = soup('div')
for tag in soup.find_all('div', {'class': 'track-artist'}):
    # tmpArtist = re.findall('<div class=\"track-artist\">(.*)</div>', str(tag))
    artistList.extend(re.findall('<div class=\"track-artist\">(.*)</div>', str(tag)))

for tag in soup.find_all('div', {'class': 'track-name'}):
    # trackList.extend(tag)
    print(tag)

# print(artistList)
print(trackList)
