import requests
from bs4 import BeautifulSoup


xkcd_id = 1024
url_string = 'http://www.explainxkcd.com/wiki/index.php/' + str(xkcd_id)


r = requests.get(url_string)
soup = BeautifulSoup(r.content, 'html.parser')


def main():
    start = soup.find('table')
    
    for a in start.find_next_siblings('p'):
        s = a.get_text()
        print(s)
        if(a.next_sibling.name != 'p'):
            break 


if __name__ == '__main__':
    main()
