tar xvf ./Monitoring.tar.gz -C /opt
pip install psutil
pip install prettytable
cd /opt/Monitoring
ln -s /setting/setting.json /home/setting.json
cp /service/custom.service /etc/systemd/system/
cp /service/details.service /etc/systemd/system/
cp /service/process_msg.service /etc/systemd/system/
mkdir /var/log/infinity/custom
mkdir /var/log/infinity/detail
mkdir /var/log/infinity/proces
