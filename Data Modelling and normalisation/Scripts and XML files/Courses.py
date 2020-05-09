from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.dal.ca/academics/programs.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "contentPar parsys"})
f = open("Courses.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
all = bs.find_all(['dt'])
list = []
for i in all:
    value = str(i.text).strip()
    list.append(value)
last = len(list)
i = 0
for i in range(1,117,1):
    course = str(list[i])
    f.write('<table name="course"><column name="Id"></column>')
    f.write('<column name="Course_type">UnderGraduate</column>')
    f.write('<column name="Sub_Course_name">' + course.strip().replace('&', 'and') + '</column>')
    f.write('</table>')
for i in range(117,202,1):
    course = str(list[i])
    f.write('<table name="course"><column name="Id"></column>')
    f.write('<column name="Course_type">Graduate</column>')
    f.write('<column name="Sub_Course_name">' + course.strip().replace('&', 'and') + '</column>')
    f.write('</table>')
for i in range(202,210,1):
    course = str(list[i])
    f.write('<table name="course"><column name="Id"></column>')
    f.write('<column name="Course_type">Professional</column>')
    f.write('<column name="Sub_Course_name">' + course.strip().replace('&', 'and') + '</column>')
    f.write('</table>')
f.write('</database>')
f.write('</pma_xml_export>')
f.close()
