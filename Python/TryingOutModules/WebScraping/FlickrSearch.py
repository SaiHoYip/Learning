import requests, sys, webbrowser, bs4
print('Searching...')    # display text while downloading the search result page


img = input("What would you like to search?: ")
urlToOpen = 'https://www.flickr.com/search/?text=' + img
print('Opening', urlToOpen)
webbrowser.open(urlToOpen)
#Try on cmd: FlickrSearch.py html