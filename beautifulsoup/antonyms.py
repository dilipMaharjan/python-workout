import requests
from bs4 import BeautifulSoup

data = requests.get('http://www.synonym.com/synonyms/cold/')

soup = BeautifulSoup(data.text, "html.parser")
soup.prettify()
h3 = soup.find('h3', {})
h3 = soup.find('h3', {'class': 'term'})
print(h3.string)
