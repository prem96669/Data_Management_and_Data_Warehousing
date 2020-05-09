import csv

with open("positive_words.txt", 'r') as positive_words:
    positive_words_list = positive_words.read().split("\n")

with open("negative_words.txt", 'r') as negative_words:
    negative_words_list = negative_words.read().split("\n")

with open("tweets.csv", 'r') as tweet:
    with open("sentiment_analysis.csv", mode="w", newline="", encoding="utf-8") as record:
        writer = csv.writer(record)
        count = 1
        writer.writerow(["Tweet", "Message","Match", "Polarity"])
        for each in tweet:
            bag = {}
            tweet_words = each.split()
            for each_word in tweet_words:
                if each_word in bag.keys():
                    bag[each_word] += 1
                else:
                    bag[each_word] = 1
            print(bag)
            polarity = 0
            tweet_polarity = "false"
            for x,y in bag.items():
                if x in positive_words_list:
                    polarity = "positive"
                    writer.writerow([count, each.strip(), x, polarity])
                    tweet_polarity = "true"
                elif x in negative_words_list:
                    polarity = "negative"
                    writer.writerow([count, each.strip(), x, polarity])
                    tweet_polarity = "true"
            if tweet_polarity == "true":
                count = count + 1
                continue
            elif tweet_polarity == "false":
                writer.writerow([count, each.strip(), "", "neutral"])
                count = count + 1
                continue



















