#!/usr/bin/env python

# Use LF instead of CRLF for end-of-line in files for Windows compatibility.
# Do not change the existing code as it may lead to unexpected errors.
'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath) as f:
	#TODO

with open(delimitersPath) as f:
    #TODO

conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[3], 1)

#TODO

outputFile = open(sys.argv[4],"w")

#TODO
#write results to output file. Foramt for each line: (line +"\n")

sc.stop()
