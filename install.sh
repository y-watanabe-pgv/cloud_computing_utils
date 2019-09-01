#!/bin/sh
# This script should be run on your remote machine.

# Make your remote machine's shutdown commands available without password.
sudo chmod u+s /sbin/shutdown

# Put start_instance.sh and automatic_server_stopper.py where your PATH is through. For example,
sudo cp automatic_server_stopper.py /usr/local/bin/ # start_gcp_instance.sh 
sudo chmod +x /usr/local/bin/automatic_server_stopper.py

# Set cron on you machine.
sudo cp automatic_server_stopper.cron /etc/cron.d
sudo chmod 0644 /etc/cron.d/automatic_server_stopper.cron

# rm /tmp/gpu_utils_log.csv during each booting.
sudo sh -c "echo rm /tmp/gpu_utils_log.csv >> /etc/rc.local"
sudo chmod +x /etc/rc.local

## Check
# automatic_server_stopper.py
# sudo systemctl status crond # @reboot jobs will be run at computer's startup.
# sudo systemctl restart crond
# ls /tmp/gpu_utils_log.csv

# Permissions
# 777
# /sbin/shutdown
# 644
# /etc/cron.d/automatic_server_stopper.cron
# 755
# /usr/local/bin/automatic_server_stopper.py
