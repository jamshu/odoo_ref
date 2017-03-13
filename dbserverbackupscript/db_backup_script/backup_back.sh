#!/bin/sh
filename=`date +"%Y_%B_%d_%H_%M_%N"`
folder=`date +"%Y_%B_%d"`
filename_path=$HOME"/backup/"$folder
db_list='/opt/db_backup_script/db_list.txt'
mkdir -p ${filename_path}
databases=`cat $db_list`
for db in $databases ; do
        ssh admin@erp.foodtech.ae "pg_dump --cluster 9.5/main --format=c $db > "/tmp/"$db"_"$filename.dump"
        scp admin@erp.foodtech.ae:"/tmp/"$db"_"$filename.dump $filename_path"/"$db"_"$filename.dump
        ssh admin@erp.foodtech.ae "rm -rf /tmp/"$db"_"$filename.dump
done
house_keeping_date=`date --date="-10 days" +"%Y_%B_%d"`
hfilename="/home/foodtech_erp/backup/$house_keeping_date"
rm -rf ${hfilename}

exit 0
