class URLExtractor:
    def __init__(self, url):
        self.url = self.url_sanitize(url)
        self.url_validate()
    
    def url_sanitize(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
        
    def url_validate(self):
        if not self.url:
            raise ValueError("The URL is empty.")
        
    def get_url_base(self):
        question_index = self.url.find('?')
        url_base = self.url[:question_index]
        return url_base
    
    def get_url_params(self):
        question_index = self.url.find('?')
        url_params = self.url[question_index+1:]
        return url_params
    
    def get_value_param(self, search_param):
        index_param = self.get_url_params().find(search_param)
        index_value = index_param + len(search_param) + 1
        index_e_commercial = self.get_url_params().find('&', index_value)
        if index_e_commercial == -1:
            value = self.get_url_params()[index_value:]
        else:
            value = self.get_url_params()[index_value:index_e_commercial]
        return value
     
url_extractor = URLExtractor("bytebank.com/exchange?amount=100&coinSource=real&coinDestiny=dolar")
value_amount = url_extractor.get_value_param('amount')
print(value_amount)
        