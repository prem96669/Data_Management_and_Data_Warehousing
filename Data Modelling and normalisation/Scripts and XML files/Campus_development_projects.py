from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.dal.ca/dept/facilities/campus-development.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "expandingSubsection section"})
f = open("campus_development_projects.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
headers = bs.find_all(['h2'])
header4 = bs.find_all(['h4'])
list = []
for j in headers:
    head = str(j.text)
    if (head.__contains__("Dal") or head.__contains__("Faci")):
        continue
    else:
        list.append(head)
list2 = []
for j in header4:
    list2.append(str(j.text))
l = 0;
for l in range(3):
    f.write('<table name="cam_dev_projects"><column name="Id"></column>')
    type = str(list[1])
    name = str(list2[l])
    f.write('<column name="Project_type">' + type.strip().replace('&', 'and') + '</column>')
    f.write('<column name="Project_name">' + name.strip().replace('&', 'and') + '</column>')
    f.write('</table>')
for x in range(3,22):
    f.write('<table name="cam_dev_projects"><column name="Id"></column>')
    type2 = str(list[2])
    name2 = str(list2[x])
    f.write('<column name="Project_type">' + type2.strip().replace('&', 'and') + '</column>')
    f.write('<column name="Project_name">' + name2.strip().replace('&', 'and') + '</column>')
    f.write('</table>')
for z in range(22,24):
    try:
        f.write('<table name="cam_dev_projects"><column name="Id"></column>')
        type3 = str(list[3])
        name3 = str(list2[z])
        f.write('<column name="Project_type">' + type3.strip().replace('&', 'and') + '</column>')
        f.write('<column name="Project_name">' + name3.strip().replace('&', 'and') + '</column>')
        f.write('</table>')
    except:
        continue
f.write('</database>')
f.write('</pma_xml_export>')
f.close()


