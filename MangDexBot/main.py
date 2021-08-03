import tweepy
import requests
import urllib.request
import datetime
from datetime import date
from datetime import time
from bs4 import BeautifulSoup
import logging

#TODO Make the bot able to post if MangaDex.org comes back even though bot already posted tweet that day
#TODO Find a better way to check MangaDex's status
#TODO If MangaDex.org is donw, the bot will error

logging.basicConfig(level = logging.INFO, filename = "output.log")

user = "IsMangaDexKill"
url = "https://mangadex.org/index.html"
check_text = "MangaDex - See you soon!" 
today = datetime.datetime.today()
isLive = eval(open("isLive.txt",'r').read())
post_time = datetime.time(12)
updated = False

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
        return(check_text not in soup.title.string) #If true website should be live. Update isLive.txt so that the program doesn't keep runnning unnessisarily

def main():
    updated = checkSite()
    open("isLive.txt", 'w').write(str(updated))

    if(updated):
        #post up tweet
        #api.update_status("The MangaDex website has updated!")
        logging.info(today.strftime("%d/%m/%Y %H:%M:%S") + ": Posted Tweet: The MangaDex website has updated!")
    elif(today.time() > post_time and api.user_timeline(user)[0].created_at.date() != date.today()):
        #post down tweet
        #api.update_status("Today is: " + today.strftime("%d/%m/%Y") + ", and MangaDex is still down :(")
        logging.info(today.strftime("%d/%m/%Y %H:%M:%S") + ": Posted Tweet: Today is: " + today.strftime("%d/%m/%Y") + ", and MangaDex is still down :(")
    else:
        logging.info(today.strftime("%d/%m/%Y %H:%M:%S") + ": Did not post tweet")
    
    logging.info(today.strftime("%d/%m/%Y %H:%M:%S") + ": Program Run Successfully")

if(not isLive):
    main()