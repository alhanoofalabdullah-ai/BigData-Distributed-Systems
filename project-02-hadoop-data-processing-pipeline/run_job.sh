#!/bin/bash

hdfs dfs -mkdir -p /input

hdfs dfs -put -f hdfs/input/sales-data.csv /input/sales-data.csv

hdfs dfs -rm -r -f /output/sales-summary

hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -mapper mapreduce/mapper.py \
  -reducer mapreduce/reducer.py \
  -input /input/sales-data.csv \
  -output /output/sales-summary
