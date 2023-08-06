class QuoteFetcher:
    def __init__(self, file_path):
        self.file_path = file_path
               
    def get_quotes(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            quotes = [line.strip() for line in file if line.strip()]
        return quotes