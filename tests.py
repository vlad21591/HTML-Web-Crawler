from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('a'):
        print(anchor.get('href', '/'))

html = urlopen("http://www.wikipedia.org")
bs_object = BeautifulSoup(html.read(),"html.parser")
print(bs_object.title)