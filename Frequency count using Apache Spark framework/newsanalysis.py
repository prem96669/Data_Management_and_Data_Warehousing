import requests as res
import json
import csv
import re
headers = {'Authorization': '5e29bc3cebf3478f981fa7b029cc5e89'}
# Using this URL, we will get news from all the sources and all typeof data including articles.
everything_news_url = 'https://newsapi.org/v2/everything'
# Creating query to get the news with keywords like university, language english, popularity.
everything_payload = {'q': '((Halifax) OR (Canada) OR (Dalhousie University) OR (Canada Education) OR (University))', 'language': 'en', 'sortBy': 'popularity',  'PageSize' : 100}
# Opening CSV in a write mode to write the data extracted
with open('news.csv', mode='w', newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Creating headers for CSV file.
    writer.writerow(['Author', 'Title', 'Description','Content'])
    # Using requests(get method), we are getting the news content(Meta data).
    content = res.get(url=everything_news_url, headers=headers, params=everything_payload)
    # Json object is created to store the content in json form.
    content_json = json.dumps(content.json())
    # Dictionary is created to load json object data for better extraction
    content_dict = json.loads(content_json)
    # Using key word articles, we are creating an dictionary object to store that data with metadata of articles.
    articles_list = content_dict['articles']

    # using for loop, each article is being iterated to get metadata from it.

    for article in articles_list:
        # Regular expression is used to remove special characters from the required.
        # intermediate veriables were declared to store the values using the key, later used to load to CSV file.
        author = re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "",article['author'])
        title = re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "",article['title'])
        description = re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "",article['description'])
        content = re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "",article['content'])
        # Writing data to CSV file is done below using writerow method.
        writer.writerow([author, title, description, content])

