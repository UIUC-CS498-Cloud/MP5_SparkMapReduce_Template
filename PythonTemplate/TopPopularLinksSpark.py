#!/usr/bin/env python
# Use LF instead of CRLF for end-of-line in files for Windows compatibility.
# Do not change the existing code as it may lead to unexpected errors.

import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopPopularLinks")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO

output = open(sys.argv[2], "w")

#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")

sc.stop()

