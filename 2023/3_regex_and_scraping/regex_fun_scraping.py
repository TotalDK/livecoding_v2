import re
import requests

#Comment: Use BeautifilSoup library instead ;)
# I think it's called bs4 when you pip install it.


block_to_match = "blockquote"

pattern = f"<{block_to_match}>(.+)</{block_to_match}>"
url = "https://studentcouncil.dk/organisations/connect"
#url = "https://studentcouncil.dk/organisations/aitu"


pattern = re.compile(pattern)
s = requests.get(url).content.decode('utf-8')

print(re.findall(pattern, s))