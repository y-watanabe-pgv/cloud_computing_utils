# cloud_computing_utils
This repository aims effective starting/stopping cloud machines.

## Starting instance (GCP)
GCP instances are sometimes not be able to start because the resource is not sufficient. "start_instance.sh" enables you to request starting your instance by the time it succeeds. After that, it tries to ssh the server.

## Stopping instance
It's often the case that cloud computing server is charged on a connect-time basis. "automatic_server_stopper.py" gets your virtual machine's GPU utilities and decide whether to shutdown or not w.r.t the obtained infomation. This python script might want to be run regularly. So, I decided to use cron to manage it. 

# Default threshoulds to shutdown
1) more than 30 min passed
2) the mean GPU's occupied memory percentage of the absolute diffrence between sampling points (from 1 min before) was less than threshould
3) the mean GPU's Volatile utility is less than 50%

## How to setup
1) YOUR_INSTANCE_NAME and YOUR_INSTANCE_REGION are set in start_instance.sh.
2) Make your machines shutdown commands available without password. 
```sh
sudo chmod u+s /sbin/shutdown
```
3) Put start_instance.sh and automatic_server_stopper.py where your PATH is through. (for example. /usr/local/bin/)
4) Set cron on you machine. (/etc/cron.d/automatic_server_stopper.cron, permission 644)
5) rm /tmp/gpu_utils_log.csv during each booting.
```sh
sudo sh -c "echo rm /tmp/gpu_utils_log.csv >> /etc/rc.local"
```
