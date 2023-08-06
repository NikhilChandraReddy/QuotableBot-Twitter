from quote_fetcher import QuoteFetcher
from tweepy_api import TwitterAPI
import random

# Twitter API credentials (replace with your own)
consumer_key = "A2YiaY8zFXipy7BjDpruNVZ1q"
consumer_secret = "LJiwRRLLG3ENsa27FMCvdGr6pyJoyISI7ANu0YaTUsbLjqdJFX"
access_token = "1649185990907424768-AS4Hn5rVOozvKM8lVmDLX9dk5KUBi2"
access_token_secret = "H8GoqBlfqm0DeZu7GwlihUmPEnTpZ1Ptc9bz9GMrxzo8i"

def main():
    # Initialize Twitter API
    twitter_api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

    # Initialize Quote Reader
    quote_fetcher = QuoteFetcher()
    
    #Loop until the tweet is with 280 characters
    while True:
        # Get a random quote
        quote_data = quote_fetcher.get_random_quote()
        quote = quote_data['quote']
        author = quote_data['author']
        category = quote_data.get('category', 'Uncategorized')
        wiki_link = quote_data.get('wiki_link', '')
    
        tweet_text = f'{quote} - {author}'
        
        # Check if the tweet is within the character limit (280 characters)
        if len(tweet_text) <= 280:
            break
    
    # Print the tweet text
    print(tweet_text)

    # Tweet the quote
    # twitter_api.tweet_status(tweet_text)
    

if __name__ == "__main__":
    main()