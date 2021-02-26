#from reading https://automatetheboringstuff.com/2e/chapter7
# r' means escape characters will be ignored like \
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 328-555-4242')
print(mo.group())
Num = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mor = Num.search('My number is 389-555-4343')
print(mor.group(1))
print(mor.groups())
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
soup = re.compile(r'Pine(cone|tree|leaf)')
mo3 = soup.search('Pinecone turn into pinetrees when buried')
print(mo3.group())