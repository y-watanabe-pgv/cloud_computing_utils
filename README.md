# cloud_computing_utils
This repository aims effective starting/stopping cloud machines.

# Starting instance (GCP)
GCP instances are sometimes not be able to start because the resource is not sufficient. "start_gcp_instance.sh" enables you to request starting your instance by the time it succeeds, of course from the client. After that, it tries to ssh the server.

# Stopping instance
It's often the case that cloud computing server is charged on a connect-time basis. "automatic_server_stopper.py" gets your virtual machine's GPU utilities and decide whether to shutdown or not w.r.t the obtained infomation. This python script might want to be run regularly, which is offered by  cron. This combination monitors your machine GPU usage and prevent you from overpayment because of keeping machines on and from being trouble with your boss. :)

## Default threshoulds to shutdown
Condition 1) Logging has been conducted for more than 30 min or not.
Condition 2) GPU memory usage has not been changed for the last 30 min.
Condition 3) GPU's volatile utility has not been less than 50% on the average.
These threshoulds are adujustable at the beginning of "automatic_server_stopper.py"
```python
## Threshoulds
log_min = 30
mem_used_delta_threshould = 10
gpu_util_mean_threshould = 50
```

## How to setup
### About starting instance (GCP)
1) YOUR_INSTANCE_NAME and YOUR_INSTANCE_REGION are to be set in start_gcp_instance.sh.
You can use the script just run by 
```bash
./start_gcp_instance.sh in the directory
```
or 
```bash
sudo cp start_gcp_instance.sh /usr/local/bin
$ start_gcp_instance.sh
```
### About stopping instance
1) Make your remote machine's shutdown commands available without password. 
```sh
sudo chmod u+s /sbin/shutdown
```
2) Write your python path at the top of automatic_server_stopper.py # ex) #!/bin/python
3) Put automatic_server_stopper.py on your PATH.
For example,
```sh
sudo cp automatic_server_stopper.py /usr/local/bin/
```
4) Set the cron script on you machine.
```sh
sudo cp automatic_server_stopper.cron /etc/cron.d
sudo chmod 0644 /etc/cron.d/automatic_server_stopper.cron
```
5) rm /tmp/gpu_utils_log.csv during each booting.
```sh
sudo sh -c "echo rm /tmp/gpu_utils_log.csv >> /etc/rc.local"
```

# Dependancies
pandas
```sh
pip install pandas
```

# How to check if this system is working
sudo systemctl status crond
ls /tmp/gpu_utils_log.csv
