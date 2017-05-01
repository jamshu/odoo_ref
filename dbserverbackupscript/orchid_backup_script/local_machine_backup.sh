#!/bin/sh
filename=`date +"%Y_%B_%d_%H_%M_%N"`
folder=`date +"%Y_%B_%d"`
filename_path=$HOME"/backup/"$folder
db_list='/opt/orchid_backup_script/db_list.txt'
mkdir -p ${filename_path}
databases=`cat $db_list`
for db in $databases ; do
        #ssh orchid@localhost "pg_dump --cluster 9.5/main --format=c -U orchiderp $db > "/tmp/"$db"_"$filename.dump"
        pg_dump --cluster 9.6/main --format=c -U orchiderp $db > /tmp/$db"_"$filename.dump
        #scp orchid@localhost:"/tmp/"$db"_"$filename.dump $filename_path"/"$db"_"$filename.dump
        cp /tmp/$db"_"$filename.dump $filename_path/$db"_"$filename.dump
        #ssh orchid@localhost "rm -rf /tmp/"$db"_"$filename.dump
        rm -rf /tmp/$db"_"$filename.dump
done
house_keeping_date=`date --date="-10 days" +"%Y_%B_%d"`
hfilename=$HOME"/backup/"$house_keeping_date
rm -rf ${hfilename}

exit 0



