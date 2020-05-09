from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://libraries.dal.ca/')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "col-last"})
f = open("libraries.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
for i in complete_data:
    names = i.find_all(['a'])
    for j in names:
        name = str(j.text)
        suffex = 'Library'
        suffex1 = 'LC'
        if(name.endswith(suffex) or name.endswith(suffex1)):
            f.write('<table name="libraries"><column name="Id"></column>')
            f.write('<column name="Library_name">' + name.strip().replace('&', 'and') + '</column>')
            f.write('</table>')
        else:
            continue
f.write('</database>')
f.write('</pma_xml_export>')
f.close()
