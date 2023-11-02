address = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# Regular Expression -- RegEx
import re

# 5 digits + hyphen (optional) + 3 digits
pattern = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]") 
match = pattern.search(address)
if match:
    zipcode = match.group()
    print(zipcode)