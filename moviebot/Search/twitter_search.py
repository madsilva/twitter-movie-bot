import string
import tweepy
from tweepy import Cursor

from datetime import datetime, timedelta
import re
from textblob import TextBlob

API_KEY = 'NGLR87Co1AT64D39ipkViztQN'
API_SECRET = 'nxiKfdz6KLssInHVBcAK7SUWdBMysxZl6F9Xq0rwFSZxE52hVP'
ACCESS_TOKEN = '909139089852649473-yXmeYbK4ib2eGs3UE2Xcw3YzR9IQH53'
ACCESS_TOKEN_SECRET = 'bcTn7Yhd1ansZlgAkQQSCnu3Bw5NGvCSqF2lKhKlVLwme'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

sentiment_analysis_vals = {}

search = api.user_timeline(id="POTUS", count=800)
try:
    for tweet in search:
        day = tweet.created_at.strftime('%Y-%m-%d')
        if day not in sentiment_analysis_vals.keys():
            sentiment_analysis_vals[day] = []
        listcomp = [x for x in tweet.text if x in string.printable]
        clean_tweet = ''.join(listcomp)
        analysis = TextBlob(clean_tweet)
        value = analysis.sentiment.polarity
        sentiment_analysis_vals[day].append(value)
        value = 0
except tweepy.TweepError as e:
    print(e)

for i in sentiment_analysis_vals:
    total = sum(sentiment_analysis_vals[i])
    length = len(sentiment_analysis_vals[i])
    if length == 0:
        sentiment_analysis_vals[i] = 0
    else:
        sentiment_analysis_vals[i] = total/length

print(sentiment_analysis_vals)



