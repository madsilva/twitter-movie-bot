import tweepy

API_KEY = 'NGLR87Co1AT64D39ipkViztQN'
API_SECRET = 'nxiKfdz6KLssInHVBcAK7SUWdBMysxZl6F9Xq0rwFSZxE52hV'
ACCESS_TOKEN = '909139089852649473-yXmeYbK4ib2eGs3UE2Xcw3YzR9IQH53'
ACCESS_TOKEN_SECRET = 'bcTn7Yhd1ansZlgAkQQSCnu3Bw5NGvCSqF2lKhKlVLwme'



auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = 'It (2017)'
max_tweets = 1500

searched_tweets = []
last_id = -1
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
    try:
        new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1))
        if not new_tweets:
            break
        searched_tweets.extend(new_tweets)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        print(e)
        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
        break