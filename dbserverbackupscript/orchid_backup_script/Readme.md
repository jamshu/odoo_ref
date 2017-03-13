#Author Jamshid K - Orchid Infosys


#Cron Job Setup
ssh into server
cd /opt
sudo git clone git@orchiderp.com:/opt/git/orchid_dev/orchid_backup_script.git
crontab -l # to list cronjobs
crontab -e # to add cron job
0 */12 * * * /usr/bin/sh /opt/orchid_backup_script/backup.sh


#Db Download Web Console Setup
sudo cp orchid_backup_service /etc/init.d/orchid_backup_service
sudo chmod +x /etc/init.d/orchid_backup_service
sudo update-rc.d orchid_backup_service defaults
