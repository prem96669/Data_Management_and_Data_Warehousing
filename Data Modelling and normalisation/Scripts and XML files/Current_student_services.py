from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.dal.ca/current_students.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "autoSearchContentWrapper"})
f = open("current_student_services.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
for i in complete_data:
    hrefs = i.find_all('a', href = True)
    for j in hrefs:
        name = str(j.text).strip()
        link = str(j['href']).strip()
        f.write('<table name="Cur_Stu_Services"><column name="Id"></column>')
        f.write('<column name="Service_type">'+ name.replace('&', 'and') +'</column>')
        f.write('<column name="Link">' + link + '</column>')
        f.write('</table>')
f.write('</database>')
f.write('</pma_xml_export>')
f.close()

