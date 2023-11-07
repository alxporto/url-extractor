import re

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
        
        url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/exchange')
        match = url_pattern.match(url)
        if not match:
            raise ValueError('The URL is not valid')
        
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
     
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + "\n" + "URL Base: " + self.get_url_base() + "\n" + "Params: " + self.get_url_params()
    
    def __eq__(self, other):
        return self.url == other.url   
          
url = "bytebank.com/exchange?amount=100&coinSource=real&coinDestiny=dolar"
url_extractor = URLExtractor(url)
url_extractor_2 = URLExtractor(url)

print("The length of the URL is: ", len(url_extractor))
print("The complete URL: ", url_extractor)

# Check if the two instances with the same URL are equal
print("url_extractor == url_extractor_2? ", url_extractor == url_extractor_2)

# Search for the value of the 'amount' parameter
amount_value = url_extractor.get_value_param("amount")
print("The value of the 'amount' parameter: ", amount_value)
        