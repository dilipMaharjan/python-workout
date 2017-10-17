import re
import urllib.request as urlReq
#methods in re
# print dir(re);

string = "The night was cold and dark"
result = re.search("night", string)
print (result)

start = result.start()
end = start + 5
print(string[start:end])

url = 'https://finance.google.com/finance?q='
stock = input('Enter your stock')
url += stock
print (url)

data = urlReq.urlopen(url).read()
print(data)
decodedData = data.decode('utf-8')
seachResult = re.search('meta itemprop="price"', decodedData)