#!/bin/sh

YOUR_INSTANCE_NAME=?????
YOUR_INSTANCE_ZONE=????? # us-central1-a


started=false
while ! $started
do
    gcloud compute instances start $YOUR_INSTANCE_NAME --zone=$YOUR_INSTANCE_ZONE && started=true 
done

connected=false
while ! $connected
do
    ssh $YOUR_INSTANCE_NAME && connected=true
done
