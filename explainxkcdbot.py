import praw
import time
import re
import requests


from bs4 import BeautifulSoup
from urllib.parse import urlparse


para_list = []


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('explainbot', user_agent = "xkcd explain bot")
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def main():
    reddit = authenticate()
    while True:
        run_explainbot(reddit)


def run_explainbot(reddit):
    print("Getting 250 comments...")
    
    for comment in reddit.subreddit('test').comments(limit=250):
        match = re.findall("^https://www.xkcd.com/[0-9]+", comment.body)
        if match:
            print("String found in comment " + comment.id)
            xkcd_url = match[0]
            url_obj = urlparse(xkcd_url)
            xkcd_id = int((url_obj.path.strip("/")))
            url = 'http://www.explainxkcd.com/wiki/index.php/' + str(xkcd_id)

            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            
            start = soup.find('table')

            for i in start.find_next_siblings('p'):
                para = i.get_text()
                para_list.append(para)
                if(i.next_sibling.name != 'p'):
                    break

            text = "\n".join(para_list)
            #print(text)
            comment.reply(text)

    print("Sleeping for 60 seconds...")
    time.sleep(60)


if __name__ == '__main__':
    main()
