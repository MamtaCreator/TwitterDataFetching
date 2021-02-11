import tweepy as tp
from tweepy import OAuthHandler
consumer_key='ryvf7yXNzl5PojoLk1PDJgMb1'
comsumer_secret='kpnhZhv7XVCWbAkmVnntVoWQTz0oVEHFVrcy9kL4EUeaJlMWLS'
access_token='3189776639-60BgYqB56Aq0LsK8iI0T8dy6vqd1iutul5wXdHC'
access_secret='VFrRsCcrmcRsm3PVOoiylPVBGIYB0qspDepmSABY74QNr'
auth = OAuthHandler(consumer_key,comsumer_secret)
auth.set_access_token(access_token,access_secret)
args=["facebook"]
api =tp.API(auth,timeout=10)
list_tweets = []
query = args[0]
if len(args)==0:
    for status in tp.Cursor(api.search,q=query+"-filtered:retweets",lang="en",result_typ='recent').items(100):
        list_tweets.append(status.text)
        print(list_tweets)
