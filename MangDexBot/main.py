import tweepy
import requests
import urllib.request
from datetime import date
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level = logging.INFO, filename = "output.log")

user = "IsMangaDexKill"
url = "https://mangadex.org/index.html"
check_text = "Three days ago (2021-03-17), we correctly identified and reported that a malicious actor had managed to gain access to an admin account through the reuse of a session token found in an old database leak through faulty configuration of session management. Following that event, we moved to identify the vulnerable section of code and worked to patch it up, also clearing session data globally to thwart further attempts at exploitation through the same method." 
auth = tweepy.OAuthHandler("hULcG0lsEwyeN5ho6IejRzG0R", 
    "fDe7BmJ3HKNK2AtAcJMhry8eCIflzumwF663cNBG3oITFSY69Q")

auth.set_access_token("1384340442146172929-8vgMdaClUdTlkEfUEMjAWHRt13RrOB", 
    "lLf8MYbb854hFA9KPRtuvGs2ynFSJ5Dl81mN4KNQg27uS")

api = tweepy.API(auth)

def checkSite():
    http_resolved = True

    try:
        response = requests.get(url)
    except:
        http_resolved = False
        logging.info("HTTP RESOLVE ERROR")

    if(http_resolved):
        soup = BeautifulSoup(response.text, "html.parser")
        logging.info(date.today().strftime("%d/%m/%Y") + ": Program Run Successfully")
        if check_text in soup.get_text(): #If true, website still down, if false website should be live.
            #post tweet saying down
            return("Today is: " + date.today().strftime("%d/%m/%Y") + ", and MangaDex is still down :(")
        else:
            return("The MangaDex website has updated!")
            #post tweet saying live
        
output = checkSite()

logging.info(date.today().strftime("%d/%m/%Y") + ": POST: " + output)

if(api.user_timeline(user)[0].created_at.date() != date.today()):
    logging.info(date.today().strftime("%d/%m/%Y") + ": Posted Tweet")
    api.update_status(output)
else:
    logging.info(date.today().strftime("%d/%m/%Y") + ": Did not post Tweet")
