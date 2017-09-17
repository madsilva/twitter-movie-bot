import tweepy

consumer_key = 'NGLR87Co1AT64D39ipkViztQN'
consumer_secret = 'nxiKfdz6KLssInHVBcAK7SUWdBMysxZl6F9Xq0rwFSZxE52hVP'
access_token = '909139089852649473-yXmeYbK4ib2eGs3UE2Xcw3YzR9IQH53'
access_token_secret = 'bcTn7Yhd1ansZlgAkQQSCnu3Bw5NGvCSqF2lKhKlVLwme'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search = api.search(q ='Kesha')

print (search[0])