#Author Jamshid K - Orchid Infosys


generate an rsa key and paste the public key on the server accessing


create a dbuser called orchid 

sudo su - postgres
createuser -s orchid

#Cron Job Setup
ssh into server
cd /opt
sudo git clone git@orchiderp.com:/opt/git/orchid_dev/orchid_backup_script.git
crontab -l # to list cronjobs
crontab -e # to add cron job
0 */12 * * * /usr/bin/sh /opt/orchid_backup_script/backup.sh

pg_hba.conf
make peer to trust
# Don't require a password for local connections
local   all             all                                     trust

#Db Download Web Console Setup
sudo cp orchid_backup_service /etc/init.d/orchid_backup_service
sudo chmod +x /etc/init.d/orchid_backup_service
sudo update-rc.d orchid_backup_service defaults
