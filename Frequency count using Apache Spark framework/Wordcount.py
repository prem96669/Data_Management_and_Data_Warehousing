from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

# Opening the output file in write mode.
f = open("word_count_output.txt", 'w')

con = SparkConf().setAppName("DWMA_Assignment2")
sc = SparkContext(conf=con)
sqlContext = SQLContext(sc)

# Assigning the keywords in an list.
values = ['expensive', 'faculty','canada','education', 'university', 'dalhousie', 'computer science', 'graduate',
            'good schools', 'good school', 'bad schools','bad school', 'poor school', 'poor schools']

# sc.textfile is used to load text file data.
content = sc.textFile("alltext.txt")

# FlatMap is used to create RDD from the data loaded into content using SC.textfile.
# Split function is used split the data using the condition provide, here is ','.
elements = content.flatMap(lambda x: x.lower().split(","))

# Created a for loop to find each occurrence of the keyword or value in the RDD.
for value in values:
    # Filter is a data frame which is used to create variables and their counts.
    # find function is used to find the count of the value in the RDD.
    occurrence = elements.filter(lambda v1: v1.find(value) != -1)
    # filter is used to find the value we are looking for in the RDD
    intermediate = "Word count of " + value + ":" + str(occurrence.count())
    # Intermediate variable is created to store the string value and used to load into text file
    f.write(str(intermediate))
    # Used to go to next line in the output file.
    f.write('\n')
# Closing the file
f.close()