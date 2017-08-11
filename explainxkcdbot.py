import praw
import time
import re

xkcd_id = 1024

def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('explainbot', user_agent = "xkcd explain bot v0.1")
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit

def main():
    reddit = authenticate()
    while True:
        run_explainbot(reddit)

def run_explainbot(reddit):
    print("Getting 2500 comments...")
    
    for comment in reddit.subreddit('test').comments(limit=250):
        matches = re.findall("^https://www.xkcd.com/[0-9]+", comment.body)
        if matches:
            print("String found in comment " + comment.id)
            print(matches)            
            #comment.reply("Found...")

    print("Sleeping for 10 seconds...")
    time.sleep(5)

if __name__ == '__main__':
    main()
