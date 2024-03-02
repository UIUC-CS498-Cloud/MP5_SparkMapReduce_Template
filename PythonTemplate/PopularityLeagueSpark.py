#!/usr/bin/env python
# Use LF instead of CRLF for end-of-line in files for Windows compatibility.
#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO

leagueIds = sc.textFile(sys.argv[2], 1)

#TODO

output = open(sys.argv[3], "w")

#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")

sc.stop()

