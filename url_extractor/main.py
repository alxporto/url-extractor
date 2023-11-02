url = "bytebank.com/exchange?coinSource=real&coinDestiny=dolar&amount=100"

# url sanitization
url = url.strip()

# url validation
if url == "":
    raise ValueError("The URL is empty.")

# separates the base and parameters
question_index = url.find('?')
url_base = url[:question_index]
url_params = url[question_index+1:]
print(url_params)

# search for the value of a parameter
search_param = 'coinSource'
index_param = url_params.find(search_param)
index_value = index_param + len(search_param) + 1
index_e_commercial = url_params.find('&', index_value)
if index_e_commercial == -1:
    value = url_params[index_value:]
else:
    value = url_params[index_value:index_e_commercial]
print(value)