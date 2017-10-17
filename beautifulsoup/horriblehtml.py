from bs4 import BeautifulSoup
import re
soup = BeautifulSoup("<html><p>asdfs<strong>Hello<a></html>", "html.parser")
print(soup)  # prints html as is

print(soup.prettify())  # prints html in semantic way
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup1 = BeautifulSoup(html_doc, "html.parser")

print(soup1.prettify())

print(soup1.title)  # prints title

print(soup1.body)  # prints body

print(soup1.body.a)  # prints first content with tag <a>

print(soup1.find_all('a'))  # returns an array

for i in soup1.body.children:
    print(i)  # prints every child component

for i in soup1.body.contents:
    print(i)

for i in soup1.descendants:
    print(i)

print(soup1.a.string)
print(soup1.title.string)  # returns text inside an element

print(soup1.head.string.parent)

# finding everything that starts with b
for tag in soup1.find_all(re.compile('^b')):
    print(tag.name)
# finding everything that has b
for tag in soup1.find_all(re.compile('t')):
    print(tag.name)