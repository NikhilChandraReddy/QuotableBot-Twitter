import tweepy

class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        try:
            self.api.update_status(message)
            print("Tweeted successfully!")
        except tweepy.TweepError as e:
            print("Error occurred while tweeting:", e)
