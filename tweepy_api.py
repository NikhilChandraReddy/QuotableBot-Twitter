import tweepy

class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.api = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret)

    def tweet(self, tweet_text, reply_tweet_id ):
        try:
            response= self.api.create_tweet(text=tweet_text, in_reply_to_tweet_id= reply_tweet_id)
            print("Tweet created successfully!")
            return response.data
        except tweepy.TweepyException as exception:
            print(f"Error:  While creating a tweet. Exception: {exception}")
            exit(1)