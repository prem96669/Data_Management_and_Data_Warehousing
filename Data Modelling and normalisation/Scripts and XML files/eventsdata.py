from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
html = urlopen('https://www.dal.ca/news/events.weekOf.html/2019-09-29.html')
bs = BeautifulSoup(html, "html.parser")
f = open("eventsdata.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw"> ')
tables = bs.find_all('div', { "class" : "h4-placeholder"})
#titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6','.h4-placeholder'])
#print('List all the header tags :', *titles, sep='\n\n')
for i in tables:
    heading = i.find(['h4'])
    name = i.find(['a'])
    dd = i.find(['dd'])
    date = heading.string
    time = str(dd.text)
    f.write('<table name="events"><column name="Id"></column>')
    date_module = '<column name="Event_date">' + date +'</column>'
    name = name.string
    name_module = '<column name="Event_name">' + name +'</column>'
    time_module = '<column name="Event_time">' + time.strip() +'</column>'
    f.write(date_module)
    f.write(name_module)
    f.write(time_module)
    f.write('        </table>')
f.write('   </database>')
f.write('</pma_xml_export>')
    

f.close()
