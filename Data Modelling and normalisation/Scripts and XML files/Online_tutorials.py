from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
html = urlopen('https://libraries.dal.ca/help/online-tutorials.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "containerTwoColumn section"})
f = open("online_tutorials.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
for i in complete_data:
    data = i.find_all('div',{"class" : "text parbase section"})
    for j in data:
        headers = j.find_all(['h2'])
        for k in headers:
            header_data = k.text
            data = j.find_all(['a'])
            for d in data:
                value = str(d.text)
                header_data_replace = header_data.strip()
                replacing = header_data_replace.replace('&','and')
                value_replace = value.strip().replace('&','and')
                f.write('<table name="online_tutorials"><column name="Id"></column>')
                f.write('<column name="Tutorial_Type">' + replacing + '</column>')
                f.write('<column name="Tutorial_Name">' + value.strip().replace('&','and') + '</column>')
                f.write('        </table>')
f.write('</database>')
f.write('</pma_xml_export>')
f.close()