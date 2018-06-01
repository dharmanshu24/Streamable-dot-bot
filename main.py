#! /usr/bin/python3

import praw
import requests
import time
from bs4 import BeautifulSoup
import configparser
import json

# Getting Comment History

dfile = 'data.txt'
history = {}
try:
    data = open(dfile, 'r')
    history = json.load(data)
except Exception:
    pass


replyTemplate = """[{}]({})


^^Link ^^for ^^who ^^can't ^^access ^^Streamable

^^I'm ^^a ^^bot ^^:)"""


def getVideoLinkTitle(url):
    print("Url =", url)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')

    # getting link
    videolink = soup.find_all(attrs={"property": "og:video:secure_url"})
    link = str(videolink[0].get("content"))

    # getting title
    titleTage = soup.select("title")
    title = str(titleTage[0].contents)[2:-15]

    return link, title


# Getting Posts
def comment(reddit):
    for subreddits in open('subreddits.txt'):
        subreddit = reddit.subreddit(subreddits[:-1])
        for submission in subreddit.new(limit=50):
            url = submission.url
            if url.find("streamable.com/") != -1:
                if str(submission.title) not in history:
                    history[str(submission.title)] = True
                    history[str(submission.title)] = 1
                    print("Working On", url)
                    link, title = getVideoLinkTitle(url)
                    submission.reply(replyTemplate.format(title, link))
                    print("Commented Successfully")
    return history


# Getting data from user.client_id
config = configparser.ConfigParser()
config.read('user.ini')
# Authentication
client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')
password = config.get('credentials', 'password')
username = config.get('credentials', 'username')
user_agent = config.get('credentials', 'user_agent')
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=username, username=username)
print("Authentication Successfull")
# getting new posts
while True:
    print("Running")
    history = comment(reddit)
    with open(dfile, 'w') as outfile:
        json.dump(history, outfile)
    time.sleep(15)
