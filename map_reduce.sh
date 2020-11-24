#!/bin/sh
hdfs dfs -mkdir /mapred
hdfs dfs -put data.csv /mapred/
hadoop jar $HADOOP_STREAM_PATH/hadoop-streaming-$HADOOP_VERSION.jar -file accident_count_mapper.py -mapper accident_count_mapper.py -file accident_count_reducer.py -reducer accident_count_reducer.py -input /mapred/data.csv -output /mapred/all_accidents

hadoop jar $HADOOP_STREAM_PATH/hadoop-streaming-$HADOOP_VERSION.jar -file accdent_total_mapper.py -mapper accdent_total_mapper.py -file accdent_total_reducer.py -reducer accdent_total_reducer.py -input /mapred/all_accidents -output /mapred/make_year_count
