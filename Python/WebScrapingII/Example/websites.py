from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    course_cards = soup.find_all('div', class_='card') #important the underscore so it knows its a html atrri #look for all card class inside a div tag
    for course in course_cards:
        #print(course)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')