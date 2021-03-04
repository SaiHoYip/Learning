#https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=
#https://www.youtube.com/watch?v=XVv6mJpFOb0&t=1091s
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)
soup = BeautifulSoup(html_text,'lxml')#instance created for soup
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")#from list elements get all with this class
for job in jobs:
#job = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")
    published_date = job.find('span', class_='sim-posted').span.text #give a condition to find jobs with publish date from few
    if "few" in published_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ','') #to align text to left leave no space
        skills = job.find('span', class_="srp-skills").text.replace(' ','')

#print(company_name)
#print(skills)
        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        Published: {published_date}
        ''')

        print('')

        #Summary: Grab job posts with filters applied
