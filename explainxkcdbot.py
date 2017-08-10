import praw
import time

#Temporary value of xkcd_id
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

#need to add extraction of url elements 
def run_explainbot(reddit):
    print("Getting 2500 comments...")
    for comment in reddit.subreddit('test').comments(limit=250):
        if "https://xkcd.com/" in comment.body:
            print("String found in comment " + comment.id)
            comment.reply("Found...")

    print("Sleeping for 10 seconds...")
    time.sleep(5)

if __name__ == '__main__':
    main()
