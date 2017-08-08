import requests
from bs4 import BeautifulSoup
from explainxkcdbot import xkcd_id


url_string = 'http://www.explainxkcd.com/wiki/index.php/' + str(xkcd_id)
r = requests.get(url_string)

soup = BeautifulSoup(r.content, 'html.parser')

start = soup.find('table')

for a in start.find_next_siblings('p'):
    print(a.get_text())
    if(a.next_sibling.name != 'p'):
        break
