from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.dal.ca/faculty/health/health-administration/faculty-staff.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "contentPar parsys"})
f = open("other_department_faculty.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
all = bs.find_all(['a'])
list = []
for i in all:
    list.append(str(i.text).strip())
for j in range(48,66,1):
    name = list[j]
    try:
        first_name, last_name = name.split()
        f.write('<table name="Faculty"><column name="Id"></column>')
        f.write('<column name="First_name">' + first_name + '</column>')
        f.write('<column name="Last_name">' + last_name + '</column>')
        f.write('<column name="Department"> Health Administration </column>')
        f.write('<column name="Mailid"> </column>')
        f.write('<column name="Office"> </column>')
        f.write('</table>')
    except ValueError:
        print()
f.write('</database>')
f.write('</pma_xml_export>')
f.close()