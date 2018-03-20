tar xvf ./Monitoring.tar.gz -C /opt
pip install psutil
pip install prettytable
cd /opt/Monitoring
ln -s /setting/setting.json /opt/setting.json
cp /service/custom.service /etc/systemd/system/
cp /service/details.service /etc/systemd/system/
cp /service/process_msg.service /etc/systemd/system/
mkdir /var/log/infinity
mkdir /var/log/infinity/custom
mkdir /var/log/infinity/detail
mkdir /var/log/infinity/process
echo "alias customstart=\'systemctl start custom.service\'" >> /etc/bash.bashrc
echo "alias customstop=\'systemctl start custom.service\'" >> /etc/bash.bashrc
echo "alias detailstart=\'systemctl start detail.service\'" >> /etc/bash.bashrc
echo "alias detailstop=\'systemctl start detail.service\'" >> /etc/bash.bashrc
echo "alias processstart=\'systemctl start process_msg.service\'" >> /etc/bash.bashrc
echo "alias processstop=\'systemctl start process_msg.service\'" >> /etc/bash.bashrc
customstart