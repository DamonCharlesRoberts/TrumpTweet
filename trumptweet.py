#------------------------------
#  Trump Tweets
#------------------------------
import tweepy
import key
auth = tweepy.OAuthHandler(key.consumer_key,
key.consumer_secret)
auth.set_access_token(key.access_token, key.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#Get Trump's info
trump = api.get_user('realDonaldTrump')
trump.id
trump.name
trump.description
trump.status.text
trump.followers_count
trump.friends_count
trump_recent = api.user_timeline(screen_name = 'realDonaldTrump', count = 3)
for tweet in trump_recent:
    print(f'{tweet.user.screen_name}: {tweet.text}\n')