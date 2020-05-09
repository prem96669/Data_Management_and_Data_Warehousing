import os
import tweepy as tw
import pandas as pd
import csv
import re

consumer_key = "JhhHYNkZi0hb5elIa9W7CVEEa";
consumer_secret = "ugdXMjSnDd49x187e6l3pi1qd0omb5VFCqwxN9iOrK3LTx4DWj";
access_token = "1002821612364881920-r14rBuvciWdh9D8MtsAW5HzbnAwJ3P";
access_token_secret = "MDerFhZRpVUImNRwnMCy2RvLZSfqhxdpcMbmZQbLLnd84";

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit = True)
search_words = ["Halifax","Canada","Univeristy","Dalhousie University","Canada Education"]
with open('tweets.csv', mode='w', newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for value in search_words:
        tweets = tw.Cursor(api.search,
                  tweet_mode='extended',
                    q=value,
                    ).items(120)
        for tweet in tweets:
            try:
                text = tweet.retweeted_status.full_text
            except AttributeError:
                text = tweet.full_text
            final_text = re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", text)
            writer.writerow([final_text])


