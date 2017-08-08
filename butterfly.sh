#!/bin/sh
filename=`date +"%Y_%B_%d_%H_%M_%N"`
folder=`date +"%Y_%B_%d"`
filename_path=$HOME"/backup/"$folder
db_list=$HOME'/bfly_list.txt'
mkdir -p ${filename_path}
databases=`cat $db_list`
for db in $databases ; do
	ssh orchid@139.59.60.231 "pg_dump --cluster 9.6/main --format=c $db > "/tmp/"$db"_"$filename.dump"
	scp orchid@139.59.60.231:"/tmp/"$db"_"$filename.dump $filename_path"/"$db"_"$filename.dump
	ssh orchid@139.59.60.231 "rm -rf /tmp/"$db"_"$filename.dump
done
