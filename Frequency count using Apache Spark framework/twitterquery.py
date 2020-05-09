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
# search_words list is created to search these words
search_words = ["Halifax","Canada","Univeristy","Dalhousie University","Canada Education"]

#Opening tweets.csv file in write mode with newline
with open('tweets.csv', mode='w', newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    #Creating the headers
    writer.writerow(['id', 'created_at', 'text', 'location','retweet_count'])
    #Extracting tweets using Cursor using Tweepy(tw) with extented mode to get full length of tweet
    #For each 650 tweets will be extracted
    for value in search_words:
        tweets = tw.Cursor(api.search,
                  tweet_mode='extended',
                    q=value,
                    ).items(650)
        #Tweets is the complete meta data of the tweet which contains id, location, text, etc.,
        #Using for loop, we are iterating for each tweet and assigning id, created_at, text, user_location for each tweet
        for tweet in tweets:
            id = tweet.id;
            dates = tweet.created_at;
            try:
                text = "RT " + tweet.retweeted_status.full_text
            except AttributeError:
                text = tweet.full_text
            location = tweet.user.location;
            retweet_count = tweet.retweet_count;
            #Using regular expression, special characters are being removed excluding space
            final_text = re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", text)
            #Writing each row in the csv file using writerow function
            writer.writerow([id,dates,final_text,location,retweet_count])

