#!/bin/sh

started=false
while ! $started
do
    gcloud compute instances start [YOUR_INSTANCE_NAME] --zone=us-central1-a && started=true
done

connected=false
while ! $connected
do
    ssh [YOUR_INSTANCE_NAME] && connected=true
done
