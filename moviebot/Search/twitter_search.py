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

date = datetime.today()
end_date = datetime.today() - timedelta(days=45)
sentiment_analysis_vals = {}
while date > end_date:
    until = date + timedelta(days=1)
    query = "from:POTUS since:" + date.strftime('%Y-%m-%d') + " until:" + until.strftime('%Y-%m-%d')
    max_tweets = 100
    search = api.search(q=query, count=max_tweets)
    sum = 0
    count = 0
    try:
        for tweet in search:

            analysis = TextBlob(tweet.text)
            print(tweet.text)
            sum += analysis.sentiment.polarity
            count+= 1
            if count > 3:
                break
    except tweepy.TweepError as e:
        print(e)
    date = date - timedelta(days=1)
    if count >0:
        print(sum/count)
