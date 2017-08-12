import praw
import time
import re
import requests
import bs4

from bs4 import BeautifulSoup
from urllib.parse import urlparse


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('explainbot', user_agent = "xkcd explain bot")
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def fetchdata(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    tag = soup.find('p')
    data = ''
    while True:
        if isinstance(tag, bs4.element.Tag):
            if (tag.name == 'h2'):
                break
            if (tag.name == 'h3'):
                tag = tag.nextSibling
            else:
                data = data + '\n' + tag.text
                tag = tag.nextSibling
        else:
            tag = tag.nextSibling
    return data


def run_explainbot(reddit):
    print("Getting 250 comments...")
    
    for comment in reddit.subreddit('test').comments(limit=250):
        match = re.findall("^https://www.xkcd.com/[0-9]+", comment.body)
        if match:
            print("String found in comment " + comment.id)
            xkcd_url = match[0]
            url_obj = urlparse(xkcd_url)
            xkcd_id = int((url_obj.path.strip("/")))
            myurl = 'http://www.explainxkcd.com/wiki/index.php/' + str(xkcd_id)

            try:
                dataobj = fetchdata(myurl)
                print(dataobj)
            except:
                print("Incorrect XKCD url...")

            #comment.reply(dataobj)
            time.sleep(5)

    print("Sleeping for 60 seconds...")
    time.sleep(60)


def main():
    reddit = authenticate()
    while True:
        run_explainbot(reddit)


if __name__ == '__main__':
    main()
