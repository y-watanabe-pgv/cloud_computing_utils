#!/bin/sh
sudo rm /usr/local/bin/automatic_server_stopper.py
sudo rm /etc/cron.d/automatic_server_stopper.cron
export EDITOR
sudo $EDITOR /etc/rc.local # delete the line "rm /tmp/gpu_utils_log.csv"
