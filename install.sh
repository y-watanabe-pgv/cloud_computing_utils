#!/bin/sh
''' This script should be run on your remote machine. '''

# Make your remote machine's shutdown commands available without password.
sudo chmod u+s /sbin/shutdown

# Put start_instance.sh and automatic_server_stopper.py where your PATH is through. For example,
sudo cp automatic_server_stopper.py /usr/local/bin/ # start_gcp_instance.sh 

# Set cron on you machine.
sudo cp automatic_server_stopper.cron /etc/cron.d
sudo chmod 0644 /etc/cron.d/automatic_server_stopper.cron

# rm /tmp/gpu_utils_log.csv during each booting.
sudo sh -c "echo rm /tmp/gpu_utils_log.csv >> /etc/rc.local"
