import tweepy
from tweepy import Cursor

API_KEY = 'NGLR87Co1AT64D39ipkViztQN'
API_SECRET = 'nxiKfdz6KLssInHVBcAK7SUWdBMysxZl6F9Xq0rwFSZxE52hVP'
ACCESS_TOKEN = '909139089852649473-yXmeYbK4ib2eGs3UE2Xcw3YzR9IQH53'
ACCESS_TOKEN_SECRET = 'bcTn7Yhd1ansZlgAkQQSCnu3Bw5NGvCSqF2lKhKlVLwme'



auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = 'It (2017)'
max_tweets = 100

try:
    search = api.search(q = query, count = max_tweets)
    # process status here
    for tweet in search:
        print(tweet.coordinates)

except tweepy.TweepError as e:
    print(e)
