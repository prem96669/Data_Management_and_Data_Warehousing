
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.dal.ca/academics/important_dates.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "expandingSubsection section"})
f = open("important_dates.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
all_tables = bs.find_all(['td'])
list = []
for i in all_tables:
    data = str(i.text)
    list.append(data)
i = 0;
for i in range(len(list)):
    data_inlist = list[i];
    if(data_inlist.__contains__("Jan") or data_inlist.__contains__("Feb") or data_inlist.__contains__("Mar") or data_inlist.__contains__("Apr") or data_inlist.__contains__("May") or data_inlist.__contains__("Jun") or data_inlist.__contains__("Jul") or data_inlist.__contains__("Aug") or data_inlist.__contains__("Sep") or data_inlist.__contains__("Oct") or data_inlist.__contains__("Nov") or data_inlist.__contains__("Dec")):
        date = str(list[i])
        event = str(list[i+1])
        i = i+1;
        f.write('<table name="important_dates"><column name="Id"></column>')
        f.write('<column name="Date">' + date.strip().replace('&', 'and') + '</column>')
        f.write('<column name="Particular_of_date">' + event.strip().replace('&', 'and') + '</column>')
        f.write('</table>')
    else:
        i = i+1;
f.write('</database>')
f.write('</pma_xml_export>')
f.close()


