#Refer to example.html for clarification
import requests, bs4
""""""
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup)
""""""
#summary
#this block of code 1-8
#use request to main page from nostarch and passes text to bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(elems[0].getText())
print(elems[0].attrs)
#returns the text with the id author Al Sweigart
