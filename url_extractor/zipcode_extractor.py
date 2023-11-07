address = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# Regular Expression -- RegEx
import re

# 5 digits + hyphen (optional) + 3 digits
pattern = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") 
search = pattern.search(address)
if search:
    zipcode = search.group()
    print(zipcode)