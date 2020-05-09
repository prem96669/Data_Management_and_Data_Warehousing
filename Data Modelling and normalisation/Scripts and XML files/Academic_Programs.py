from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
html = urlopen('https://www.dal.ca/academics/programs.html')
bs = BeautifulSoup(html, "html.parser")
f = open("Academic_programs.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw"> ')
tables = bs.find_all('div', { "class" : "contentPar parsys"})
#titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6','.h4-placeholder'])
#print('List all the header tags :', *titles, sep='\n\n')
for i in tables:
    lists = i.find_all(['li'])
    for i in lists:
        try:
            name = i.a.text
            name1 = str(name)
            f.write('<table name="academic_programs"><column name="Id"></column>')
            f.write('<column name="academic_program_name">' + name.strip() +'</column>')
            f.write('</table>')
        except :
            continue
f.write('   </database>')
f.write('</pma_xml_export>')
f.close()
