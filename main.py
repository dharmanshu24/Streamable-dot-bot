#! /usr/bin/python3

import praw
import requests
import time
import getpass
from bs4 import BeautifulSoup


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
def getSubmissions(reddit):
    subreddit = reddit.subreddit('test')
    replyTemplate = """[{}]({})


^^Link ^^for ^^Indians ^^who ^^can't ^^access ^^Streamable

I'm a bot :)"""
    for submission in subreddit.new(limit=50):
        url = submission.url
        if url.find("streamable.com/") != -1:
            if str(submission.title) not in history:
                history[str(submission.title)] = 1
                link, title = getVideoLinkTitle(url)
                print("Working On", link)
                submission.reply(replyTemplate.format(title, link))
                print("Commented Successfully")
    return history


# Authentication
client_id = input("client_id ")
client_secret = input("client_secret ")
password = getpass.getpass()
username = input("username ")
user_agent = "StreamableDOTBot 1.0"
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=username, username=username)
print("Authentication Successfull")
history = {}
# getting new posts
while True:
    print("Running")
    history = getSubmissions(reddit)
    time.sleep(30)
