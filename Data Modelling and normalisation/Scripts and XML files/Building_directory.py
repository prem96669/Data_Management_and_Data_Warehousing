from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.dal.ca/campus-maps/building-directory.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "autoSearchContentWrapper"})
f = open("Building_directory.xml","w",encoding = "utf-8")
dds = bs.find_all(['dt'])
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
for i in dds:
    try:
        name = str(i.text).strip()
        f.write('<table name="Building_directory"><column name="Id"></column>')
        f.write('<column name="Building_name">'+ name.replace('&', 'and ') +'</column>')
        f.write('</table>')
    except :
        continue
f.write('</database>')
f.write('</pma_xml_export>')
f.close()
