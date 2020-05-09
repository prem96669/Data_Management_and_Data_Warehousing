from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.dal.ca/academics/programs.html')
bs = BeautifulSoup(html, "html.parser")
complete_data = bs.find_all('div', { "class" : "autoSearcher section"})
f = open("Sub_programs.xml","w",encoding = "utf-8")
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<pma_xml_export version="1.0" xmlns:pma="http://www.phpmyadmin.net/some_doc_url/">')
f.write('<database name="dmdw">')
hrefs = bs.find_all('a', href = True)
list = []
j = 0
for i in hrefs:
    name = i.text
    link = i['href']
    list.append(name)
    list.append(link)
for k in range(128,len(list)-1,2):
    name = list[k]
    link = str(list[k+1])
    link = "https://dal.ca"+link
    html = urlopen(link)
    bs = BeautifulSoup(html, "html.parser")
    faculty_name = bs.find_all('div', {"class": "aaPlainText parbase section"})
    data = bs.find_all(['a'])

    for i in data:
        try:
            intermediate = str(i.text)
            if (intermediate.startswith('Faculty of')):
                links = str(link)
                if(link.__contains__("/undergraduate")):
                    program = "undergraduate"
                    f.write('<table name="Sub_programs"><column name="Id"></column>')
                    f.write('<column name="Program_type">' + program + '</column>')
                    f.write('<column name="Program_course">' + intermediate + '</column>')
                    f.write('</table>')
                elif(links.__contains__("/graduate")):
                    program = "graduate"
                    f.write('<table name="Sub_programs"><column name="Id"></column>')
                    f.write('<column name="Program_type">' + program + '</column>')
                    f.write('<column name="Program_course">' + intermediate + '</column>')
                    f.write('</table>')
            else:
                continue
        except :
            continue
            f.write('</database>')
            f.write('</pma_xml_export>')
            f.close()

f.write('</database>')
f.write('</pma_xml_export>')
f.close()


