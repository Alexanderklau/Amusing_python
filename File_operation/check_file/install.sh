mkdir /infinityfs1/.del
echo "*/1 * * * * root python /opt/checkDiskBadSectors/checkDiskBadSectors.py >> /opt/checkDiskBadSectors/checkDiskBadSectors.log" >> /etc/crontab
