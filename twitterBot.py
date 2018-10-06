import tweepy

def followEveryoneThatFollowsYou():
	for follower in tweepy.Cursor(api.followers).items():
		follower.follow()
	print("Followed everyone that is following " + user.name)

def updateStatus(text):
	api.update_status(text)

# query = '#ocean', since = '2018-9-1', until = '2018-9-1', geocode = '1.3552217,103.8231561,1000km', numResults = 10
def searchAndReturnUserThatTweeted(query, since, until, geocode,numResults):
	for tweet in tweepy.Cursor(api.search,
                           q=query,								# search for
                           since=since,
                           until=until,
                           geocode=geocode,	# lat,long,distance
                           lang='fr').items(numResults):	# list last 10 results
		print('Tweet by: @' + tweet.user.screen_name)



# credentials to login to twitter api
consumer_key = 'iNA7KFShLySmUfqtD68J8dOPt'
consumer_secret = 'EfHrYM7r5YRL8zUPsxHUTfDJrlUJGfFPaRihukfjt4zV1uGwJn'
access_token = '1009266220984659969-q7pEWyp91Z6VAzvsf9zWSuPfVdwIkP'
access_secret = 'sKwqcn0ULdaS5YmYZ5lYqwyeHE7xqcsJMsy5ufChIBRSZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.location)

searchAndReturnUserThatTweeted('#vols','2018-1-1','2018-10-2','35.9606,-83.9207,1000km',10)