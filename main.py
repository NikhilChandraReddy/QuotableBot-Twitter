from quote_fetcher import QuoteFetcher
from tweepy_api import TwitterAPI
import random

# Twitter API credentials (replace with your own)
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

def get_random_quote():
    # Instantiate the QuoteFetcher and read quotes from the file
    quote_fetcher = QuoteFetcher("quotes.txt")
    quotes = quote_fetcher.get_quotes()
    return random.choice(quotes)

def tweet_random_quote():
    quote = get_random_quote()
    
    # Instantiate the TwitterAPI with your credentials
    twitter_api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    twitter_api.tweet(quote)

if __name__ == "__main__":
    tweet_random_quote()
