
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.dal.ca/academics/exam_schedule/halifax_campus_exam_schedule.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "contentPar parsys"})
f = open("exams.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
all_tables = bs.find_all(['td'])
list = []
for i in all_tables:
    data = i.text
    list.append(data)
k = 0;
for i in range(len(list)):
    try:
        faculty = list[k]
        course = list[k+1]
        section = list[k+2]
        Date = list[k+3]
        time = list[k+4]
        location = list[k+5]
        k = k + 6;
        f.write('<table name="exam"><column name="Id"></column>')
        f.write('<column name="faculty">' + str(faculty).strip().replace('&', 'and') + '</column>')
        f.write('<column name="course">' + str(course).strip().replace('&', 'and') + '</column>')
        f.write('<column name="section">' + str(section).strip().replace('&', 'and') + '</column>')
        f.write('<column name="Exam_date">' + str(Date).strip().replace('&', 'and') + '</column>')
        f.write('<column name="Exam_time">' + str(time).strip().replace('&', 'and') + '</column>')
        f.write('<column name="Exam_location">' + str(location).strip().replace('&', 'and') + '</column>')
        f.write('</table>')
    except:
        continue
f.write('</database>')
f.write('</pma_xml_export>')
f.close()

