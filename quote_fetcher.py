import requests
import random

class QuoteFetcher:
    def __init__(self, category, api_key, api_url='https://api.api-ninjas.com/v1/quotes?category={}'):
        self.api_key = api_key
        self.api_url = api_url
        self.category = category
        self.quotes = self._fetch_quotes()

    def _fetch_quotes(self):
        headers = {
            'X-Api-Key': self.api_key
        }
        response = requests.get(self.api_url.format(self.category), headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Error: Failed to fetch quotes. Status code: {response.status_code} \n Message: {response.text}")

    def get_random_quote(self):
        if self.quotes:
            return random.choice(self.quotes)
        else:
            return "Error: No quotes available."