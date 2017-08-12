import requests
from bs4 import BeautifulSoup


xkcd_id = 1024
url = 'http://www.explainxkcd.com/wiki/index.php/' + str(xkcd_id)
para_list = []


r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


def main():
    start = soup.find('table')
    
    for i in start.find_next_siblings('p'):
        para = i.get_text()
        para_list.append(para)
        if(i.next_sibling.name != 'p'):
            break 

    text = "\n".join(para_list)
    print(text)

if __name__ == '__main__':
    main()
