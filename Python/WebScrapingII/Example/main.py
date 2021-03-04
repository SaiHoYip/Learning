from bs4 import BeautifulSoup

with open('Example.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml') #Passed in the file we want to scrape and how we parse
    # tags = soup.find('h5') #looks for the first h5 tag
    tags = soup.find_all('h5') #looks for all h5 tag
    print (tags)
    for tag in tags:
        print(tag.text) #scrape using iteration 10 -11



    # print(soup.prettify()) #allows you to see code in a better way
