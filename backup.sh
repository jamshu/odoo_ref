#!/bin/sh
filename=`date +"%Y_%B_%d_%H_%M_%N"`
folder=`date +"%Y_%B_%d"`
filename_path=$HOME"/backup/"$folder
db_list=$HOME'/db_list.txt'
mkdir -p ${filename_path}
databases=`cat $db_list`
for db in $databases ; do
	ssh orchid@128.199.103.178 "pg_dump --cluster 9.5/main --format=c $db > "/tmp/"$db"_"$filename.dump"
	scp orchid@128.199.103.178:"/tmp/"$db"_"$filename.dump $filename_path"/"$db"_"$filename.dump
	ssh orchid@128.199.103.178 "rm -rf /tmp/"$db"_"$filename.dump
done
