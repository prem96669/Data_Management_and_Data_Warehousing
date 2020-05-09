from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.dal.ca/campus_life/residence_housing/residence/halifax-campus/res-buildings-halifax.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "contentPar parsys"})
f = open("residence.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
for i in complete_data:
    headers = i.find_all(['li'])
    suffix = 'Hall'
    suffix1 = 'Res'
    suffix2 = 'Place'
    for j in headers:
        name = str(j.text).strip()
        if(name.endswith(suffix) or name.endswith(suffix1) or name.endswith(suffix2)):
            f.write('<table name="residence"><column name="Id"></column>')
            f.write('<column name="Residence_Type"> Traditional </column>')
            f.write('<column name="Residence_Name">' + name.strip().replace('&', 'and') + '</column>')
            f.write('</table>')
        else:
            f.write('<table name="residence"><column name="Id"></column>')
            f.write('<column name="Residence_Type"> Non Traditional </column>')
            f.write('<column name="Residence_Name">' + name.strip().replace('&', 'and') + '</column>')
            f.write('</table>')
f.write('</database>')
f.write('</pma_xml_export>')
f.close()
