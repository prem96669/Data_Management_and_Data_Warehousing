import csv
import math
artFile = "article/article"
key_words = ['canada', 'university', 'dalhousie university', 'halifax', 'canada education']
count = 500
document_count = 0;
total = []
article = ''
max_rel_freq = -1
file_count = 0
with open("TF_IDF.csv",mode='w', newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Total Documents', count])
    writer.writerow(
        ["Search Query", "Document containing term(df)", "Total Documents(N)/ number of documents term appeared(df)",
         "Login(N/df)"])
    for key in key_words:
        key_count = 0
        for i in range(1,count,1):
            filename = artFile + str(i) + ".txt"
            file = open(filename,"r")
            content = file.read();
            content = content.lower()
            if key in content:
                key_count = key_count + content.count(key);
                if key == "canada":
                    file_count = file_count + 1
        if key_count != 0:
            indf = str(count) + "/" + str(key_count)
            ndf = count/key_count
            log = math.log(ndf)
            writer.writerow([key,key_count,indf,log])
        else:
            continue
    with open("FreqCount.csv", mode='w', newline="", encoding="utf-8") as hovcanada:
        max_relative_freq = -1
        writer = csv.writer(hovcanada)
        writer.writerow(['Term', "Canada"])
        firstcolumn = "canada appeared in " + str(file_count) + "documents"
        writer.writerow(
            [firstcolumn, "Total words (m)", "Frequency (f)", "Relative frequency (Rf)"])
        for i in range(1,count ,1):
            filename = artFile + str(i) + ".txt"
            file = open(filename,"r")
            content = file.read()
            content = content.lower()
            f_len = content.split(" ")
            one_key = "canada"
            if one_key in content:
                key_count = key_count + 1
                length = len(f_len)
                word_count = content.count("canada")
                rel_freq = word_count/length
                if rel_freq > max_relative_freq:
                    max_relative_freq = rel_freq
                    article = filename
                writer.writerow([filename, length, word_count, rel_freq])
print("File name:  " + article)
print("Relative frequency:  " + str(max_relative_freq))
f = open(article, 'r')
print("Content" + f.read())

