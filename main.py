from quote_fetcher import QuoteFetcher
from tweepy_api import TwitterAPI
import os


def main():
    
    try:
        # Twitter API credentials (replace with your own)
        consumer_key = os.environ.get('CONSUMER_KEY')
        consumer_secret = os.environ.get('CONSUMER_SECRET')
        access_token = os.environ.get('ACCESS_TOKEN')
        access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
    except KeyError:
        print("Secret Key Error")
        exit(1)
        
    
    #Initialize Twitter API
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
    
        tweet1_text = f'"{quote}" -{author}'
        tweet2_text = f'#{category} Learn more about the {wiki_link}'
        
        # Check if the tweet is within the character limit (280 characters)
        if len(tweet1_text) <= 280 and len(tweet2_text) <= 280:
            # Tweet the quote
            reponse_tweet1= twitter_api.tweet(tweet1_text, None)
            # Reply Tweet with WikiLink
            reponse_tweet2= twitter_api.tweet(tweet2_tex, reponse_tweet1["id"])
            break


if __name__ == "__main__":
    main()