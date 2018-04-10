# Streamable-dot-bot
This Reddit Bot comments Streamable video links for those who can't access streamable website

# Requirements
1. Install pip3

`sudo apt-get install pip3`

2. Install praw

`pip3 install praw`

3. Install BeautifulSoup

`pip3 install bs4`

# Usage

Create Reddit application
1. Open your Reddit application preferences by clicking [here](https://www.reddit.com/prefs/apps/).
2. Add a new application. It doesn't matter what it's named, but calling it "clean-reddit" makes it easier to remember.
3. Select "script".
4. Redirect URL does not matter for script applications, so enter something like http://127.0.0.1:8080
5. Once created, you should see the name of your application followed by 14 character string. Enter this 14 character
   string as your `client_id`.
6. Copy the 27 character "secret" string into the `client_secret` field.
7. Add one subreddit per line in `subreddit.txt` file.

Username and password are simply your Reddit login credentials for the account that will be used.

Run the `main.py` file

`python3 main.py`

Enter `client_id`,`client-secret`,`password`,`username`

Now bot will start searching for posts containing streamable links and comment accordingly.
