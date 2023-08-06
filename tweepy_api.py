import tweepy

class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.api = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret)

    def tweet(self, tweet_text):
        try:
            response= self.api.create_tweet(text=tweet_text)
            print("Tweeted successfully!")
            print(response.data)
        except tweepy.TweepyException as e:
            print(f"Error while tweeting: {e}")
            exit(1)