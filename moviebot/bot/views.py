from django.shortcuts import render
from datetime import datetime, timedelta
import re
from textblob import TextBlob
import tweepy
from tweepy import Cursor

API_KEY = 'NGLR87Co1AT64D39ipkViztQN'
API_SECRET = 'nxiKfdz6KLssInHVBcAK7SUWdBMysxZl6F9Xq0rwFSZxE52hVP'
ACCESS_TOKEN = '909139089852649473-yXmeYbK4ib2eGs3UE2Xcw3YzR9IQH53'
ACCESS_TOKEN_SECRET = 'bcTn7Yhd1ansZlgAkQQSCnu3Bw5NGvCSqF2lKhKlVLwme'


def index(request):
    context = {}

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)


    date = datetime.today()
    end_date = datetime.date(day=1, month=1, year=2017)
    sentiment_analysis_vals = {}
    while date > end_date:
        query = date
        max_tweets = 100
        search = api.search(q=query, count=max_tweets)
        sum = 0
        count = 0
        try:
            for tweet in search:
                clean_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
                analysis = TextBlob(clean_tweet)
                sum += analysis.sentiment.polarity
                count+= 1
        except tweepy.TweepError as e:
            print(e)

        date = date - timedelta(day=1)



    return render(request, "bot/index.html", context)
