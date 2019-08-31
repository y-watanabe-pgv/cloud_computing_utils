# cloud_computing_utils
This repository is to start/stop cloud virtual machine effectively.

# Starting instance
GCP instances sometimes cannot start because the resource is not sufficient. "start_instance.sh" enables you to request starting your instance by the time it's passed. It also tries ssh the server.

# Stopping instance
It's often the case that cloud computing server is charged on a connect time basis. "automatic_server_stopper.py" monitors your virtual machine's GPU utilities and decide whether to shutdown or not with regard to the infomation.

# How to setup
