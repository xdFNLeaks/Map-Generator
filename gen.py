import requests
import tweepy
from time import sleep
import PIL
from PIL import Image
import os

#-----------------------------#

# Grabs Map! (DONT CHANGE THIS!)
api = 'https://benbot.app/api/v1/status'
api = requests.get(api)
version = api.json()['currentFortniteVersionNumber']
url = 'https://fortnite-api.com/images/map_en.png'
r = requests.get(url, allow_redirects=True)

# Twitter Username | Replace "XXXXX" with your username!
username = 'XXXXX'

# Replace "XXXXX" with your API Keys!
twitAPIKey = 'XXXXX'
twitAPISecretKey = 'XXXXX'
twitAccessToken = 'XXXXX'
twitAccessTokenSecret = 'XXXXX'

# Sets up Tweepy
auth = tweepy.OAuthHandler(twitAPIKey, twitAPISecretKey)
auth.set_access_token(twitAccessToken, twitAccessTokenSecret)
api = tweepy.API(auth)

#-----------------------------#
print("Saving Image...")
open('map.png', 'wb').write(r.content)
img=Image.open('map.png')
img=img.resize((1200,1200),PIL.Image.ANTIALIAS)
img.save(f'{version}0 - map.png')
img.close()
os.remove('map.png')
sleep(0.5)
print(f"Success!\nWant to Tweet Out Map? y/n")
tweet = input(">> ")

if(tweet == "y"):
    api.update_with_media(f'{version}0 - map.png', f'#Fortnite Map Update for v{version}0!')
    print(f"Successfully tweeted to: {username}!")
else:
    print("Closing...")
