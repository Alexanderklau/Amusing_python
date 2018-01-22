echo "*/1 * * * * root python /opt/checkDiskBadSectors/checkDiskBadSectors.py >> /opt/checkDiskBadSectors/checkDiskBadSectors.log" >> /etc/crontab
tar xvf ./checkDiskBadSectors.tar.gz -C /opt


