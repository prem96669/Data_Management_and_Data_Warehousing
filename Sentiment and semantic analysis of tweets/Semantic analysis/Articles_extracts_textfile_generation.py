import requests
import json
import pandas
import csv
import re
headers = {'Authorization': '5e29bc3cebf3478f981fa7b029cc5e89'}
top_headlines_url = 'https://newsapi.org/v2/top-headlines'
everything_news_url = 'https://newsapi.org/v2/everything'
sources_url = 'https://newsapi.org/v2/sources'
direc = "article/article"
everything_payload_hal = {'q': '(Halifax)', 'language': 'en', 'sortBy': 'popularity',  'PageSize' : 100}
everything_payload_ca = {'q': '(Canada)', 'language': 'en', 'sortBy': 'popularity',  'PageSize' : 100}
everything_payload_du = {'q': '(Dalhousie University)', 'language': 'en', 'sortBy': 'popularity',  'PageSize' : 100}
everything_payload_univ = {'q': '(University)', 'language': 'en', 'sortBy': 'popularity',  'PageSize' : 100}
everything_payload_ca_edu = {'q': '(Canada Education)', 'language': 'en', 'sortBy': 'popularity',  'PageSize' : 100}

with open('news.csv', mode='w', newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Content'])
    response_hal = requests.get(url=everything_news_url, headers=headers, params=everything_payload_hal)
    response_ca = requests.get(url=everything_news_url, headers=headers, params=everything_payload_ca)
    response_du = requests.get(url=everything_news_url, headers=headers, params=everything_payload_du)
    response_univ = requests.get(url=everything_news_url, headers=headers, params=everything_payload_univ)
    response_ca_edu = requests.get(url=everything_news_url, headers=headers, params=everything_payload_ca_edu)
    response_json_string_hal = json.dumps(response_hal.json())
    response_json_string_ca = json.dumps(response_ca.json())
    response_json_string_du = json.dumps(response_du.json())
    response_json_string_univ = json.dumps(response_univ.json())
    response_json_string_ca_edu = json.dumps(response_ca_edu.json())
    response_dict_hal = json.loads(response_json_string_hal)
    response_dict_ca = json.loads(response_json_string_ca)
    response_dict_du = json.loads(response_json_string_du)
    response_dict_univ = json.loads(response_json_string_univ)
    response_dict_ca_edu = json.loads(response_json_string_ca_edu)
    articles_list = response_dict_hal['articles'] + response_dict_ca['articles'] + response_dict_du['articles'] + response_dict_univ['articles'] + response_dict_ca_edu['articles']
    count = 1
    key_words = ['canada', 'university', 'dalhousie university', 'halifax', 'canada education']
    document_count = 0;
    for article in articles_list:
        text = article['content']
        title = article['title']
        desc = article['description']
        articl = str(text) + str(title) + str(title)
        content = re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "",str(articl))
        file = open(direc + str(count) + ".txt","w")
        file.write(str(content));
        file.close()
        writer.writerow([content])
        count = count + 1

