from quote_fetcher import QuoteFetcher
from tweepy_api import TwitterAPI
import os


def get_random_category():
    import random

    #Availble category list
    category_list = [
        'amazing', 'attitude', 'beauty', 'best', 'change', 'courage', 'dreams', 'education', 'equality',
        'experience', 'faith', 'family', 'freedom', 'friendship', 'happiness', 'hope', 'imagination',
        'inspirational', 'intelligence', 'leadership', 'learning', 'life', 'love', 'success'
    ]
    #fetch random category
    return random.choice(category_list)


def main():
    
    try:
        # Twitter API credentials (replace with your own)
        consumer_key = os.environ.get('CONSUMER_KEY')
        consumer_secret = os.environ.get('CONSUMER_SECRET')
        access_token = os.environ.get('ACCESS_TOKEN')
        access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
        # API-credentials Api-ninjas quotes API(replace with your own)
        api_key = os.environ.get('QUOTES_API_KEY')
    except KeyError:
        print("Error: Failed to fetch secret-keys")
        exit(1)
        
    
    #Initialize Twitter API
    twitter_api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

    # Initialize Quote Reader
    quote_fetcher = QuoteFetcher(api_key=api_key, category=get_random_category())
    
    #Loop until the tweet is with 280 characters
    while True:
        # Get a random quote
        quote_data = quote_fetcher.get_random_quote()
        quote_text = quote_data['quote']
        quote_author = quote_data['author']
        quote_category = quote_data.get('category')
    
        #Construct tweets
        tweet1_text = '"{}" - {}\n'.format(quote_text, quote_author)
        tweet2_text = (
            "🌟 What an Inspiring quote! 🌟\n"
            "Share your thoughts! 💬\n"
            "What does this quote mean to you? Let's discuss! ⬇️\n\n"
            "#Quotes #{} #Motivation #Thoughts #Discussion #TwitterBot"
        ).format(quote_category.capitalize())
        
        # Check if the tweet is within the character limit (280 characters)
        if len(tweet1_text) <= 280 and len(tweet2_text) <= 280:
            # Tweet the quote
            reponse_tweet1= twitter_api.tweet(tweet1_text, None)
            # Reply Tweet with category
            twitter_api.tweet(tweet2_text, reponse_tweet1["id"])
            break


if __name__ == "__main__":
    main()