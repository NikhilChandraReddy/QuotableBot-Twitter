class QuoteFetcher:
    def __init__(self, file_path='quotes.json'):
        self.file_path = file_path
        self.quotes = self._read_quotes()
    
    def _read_quotes(self):
        with open(self.file_path, 'r') as file:
            data = eval(file.read())
        return data['quotes']
               
    def get_random_quote(self):
        return random.choice(self.quotes)