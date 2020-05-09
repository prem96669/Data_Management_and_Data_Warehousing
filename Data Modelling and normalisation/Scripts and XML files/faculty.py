from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.dal.ca/faculty/computerscience/faculty-staff.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "contentPar parsys"})
f = open("faculty.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
all = bs.find_all(['td'])
list = []
for i in all:
    data = str(i.text).strip()
    if(data == " "):
        continue
    else:
        list.append(data)
list.pop(12)
list.pop(64)
for k in range(4,176,4):
    if(list[k] == " "):
        k = k+1;
        continue
    else:
        name = list[k]
        email = list[k+1]
        office = list[k+2]
        name = name.lstrip("Dr.")
        name = name.lstrip("Mr.")
        name = name.lstrip("Ms.")
        try:
            first_name,last_name = name.split()
            f.write('<table name="Faculty"><column name="Id"></column>')
            f.write('<column name="First_name">' + first_name + '</column>')
            f.write('<column name="Last_name">' + last_name + '</column>')
            f.write('<column name="Department">Computer Science</column>')
            f.write('<column name="Mailid">' + email + '</column>')
            f.write('<column name="Office">' + office + '</column>')
            f.write('</table>')
        except ValueError:
            print()
for k in range(309,len(list),4):
    name = list[k]
    email = list[k+1]
    office = list[k+2]
    name = name.lstrip("Dr.")
    name = name.lstrip("Mr.")
    name = name.lstrip("Ms.")
    try:
        first_name, last_name = name.split()
        f.write('<table name="Faculty"><column name="Id"></column>')
        f.write('<column name="First_name">' + first_name + '</column>')
        f.write('<column name="Last_name">' + last_name + '</column>')
        f.write('<column name="Department">Computer Science</column>')
        f.write('<column name="Mailid">' + email + '</column>')
        f.write('<column name="Office">' + office + '</column>')
        f.write('</table>')
    except ValueError:
        print()
f.write('</database>')
f.write('</pma_xml_export>')
f.close()


