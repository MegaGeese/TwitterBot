import tweepy
import requests
import datetime
from datetime import date
from datetime import time
import logging

#TODO: need to set restrictions based on manga that have chapters that are translated to english

logging.basicConfig(level = logging.INFO, filename = "output.log")

user = "IsMangaDexKill"
url = "https://api.mangadex.org/"
today = datetime.datetime.today()
post_time = datetime.time(12)

auth = tweepy.OAuthHandler("hULcG0lsEwyeN5ho6IejRzG0R", 
    "fDe7BmJ3HKNK2AtAcJMhry8eCIflzumwF663cNBG3oITFSY69Q")

auth.set_access_token("1384340442146172929-8vgMdaClUdTlkEfUEMjAWHRt13RrOB", 
    "lLf8MYbb854hFA9KPRtuvGs2ynFSJ5Dl81mN4KNQg27uS")

twitter = tweepy.API(auth)

def checkSite():
    http_resolved = True

    try:
        response = requests.get(url)
    except:
        http_resolved = False
        logging.info("HTTP RESOLVE ERROR")
        return False

    if(http_resolved):#return https://api.mangadex.org/manga/random id
        response = requests.get(url + "manga/random", params={"contentRating": ["safe", "suggestive"]})
        chapters = requests.get(url + "chapter", params={"manga": response.json()['data']['id'], "translatedLanguage[]": "en"})
        print(f"https://mangadex.org/title/{response.json()['data']['id']}")
        return response.json()


def main():
    randomManga = checkSite()
    print(f"{randomManga['data']['id']}")
    if(randomManga): #checkSite() returned a useable ID
        #twitter.update_status("The MangaDex website has updated!")
        print(f"https://mangadex.org/title/{randomManga['data']['id']}\n")
        print(f"{randomManga['data']['attributes']['description']['en']}")
        logging.info(today.strftime("%d/%m/%Y %H:%M:%S") + ": Posted new tweet")
    else: #checkSite() could not reach mangaDex
        logging.info(today.strftime("%d/%m/%Y %H:%M:%S") + ": Did not post tweet")
    
    logging.info(today.strftime("%d/%m/%Y %H:%M:%S") + ": Program Run Successfully")

main()