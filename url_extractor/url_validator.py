# Checks if the URL base conforms to the correct pattern.
import re

url = 'https://www.bytebank.com.br/exchange'
url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/exchange')
match = url_pattern.match(url)

if not match:
    raise ValueError('The URL is not valid')
print('The URL is valid')
    
