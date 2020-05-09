from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://libraries.dal.ca/help/it-help-desk.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "twoColumnCol2 parsys"})
f = open("It_help_desk.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
for i in complete_data:
    type = i.find(['h3'])
    places = i.find_all(['li'])
    for j in places:
        place = j.find(['a'])
        header = str(type.text)
        places = str(place.text).strip()
        places1 = places.replace('&','and')
        f.write('<table name="it_help_desk"><column name="Id"></column>')
        f.write('<column name="Help_Type">' + header.strip().replace('&','and') + '</column>')
        f.write('<column name="Help_Place">' + places1 + '</column>')
        f.write('</table>')
f.write('</database>')
f.write('</pma_xml_export>')
f.close()