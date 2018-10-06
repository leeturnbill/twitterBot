
# themodelbot

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = '3oItC280vFgNLtHa9FLCUSrn6'
consumer_secret = 'J1GwmtT3JbNi3SSkRpqlZHhTaJFwuHOEDI0uaTvlNz0fAmbFTw'
access_token = '1009266220984659969-XekO15oXO6wURY4DVgAm6PNtFDqIUO'
access_secret = 'Nu2NIHSDYfRrVghQiA07Kz0SpecPxJyyN1xf3KRFeSx2w'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('models')

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(3)
