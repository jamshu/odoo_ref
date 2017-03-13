#!/bin/sh
filename=`date +"%Y_%B_%d_%H_%M_%N"`
folder=`date +"%Y_%B_%d"`
filename_path=$HOME"/backup/"$folder
db_list='/opt/db_backup_script/db_list.txt'
mkdir -p ${filename_path}
echo $filename_path
