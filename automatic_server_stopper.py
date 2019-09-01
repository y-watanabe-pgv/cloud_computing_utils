#!/bin/python

import subprocess
import json
import pprint
# import time
import datetime
import pandas as pd
import os
# import utils.myfunc as mf


## Threshoulds
log_min = 30
mem_used_delta_threshould = 10
gpu_util_mean_threshould = 50


## Load csv
csv_path = '/tmp/gpu_utils_log.csv'
exist = os.path.isfile(csv_path)
if exist:
  df = pd.read_csv(csv_path, parse_dates=['Time'])
if not exist:
  columns = ['Time', 'Memory_Usage (%)', 'GPU_Util (%)']
  df = pd.DataFrame(columns=columns)
  df.columns = columns
  exist = True


## Functions
DEFAULT_ATTRIBUTES = (
    'index',
    'uuid',
    'name',
    'timestamp',
    'memory.total',
    'memory.free',
    'memory.used',
    'utilization.gpu',
    'utilization.memory'
)

def get_gpu_info(nvidia_smi_path='nvidia-smi', keys=DEFAULT_ATTRIBUTES, no_units=True):
    nu_opt = '' if not no_units else ',nounits'
    cmd = '%s --query-gpu=%s --format=csv,noheader%s' % (nvidia_smi_path, ','.join(keys), nu_opt)
    output = subprocess.check_output(cmd, shell=True)
    lines = output.decode().split('\n')
    lines = [ line.strip() for line in lines if line.strip() != '' ]

    return [ { k: v for k, v in zip(keys, line.split(', ')) } for line in lines ]

# pprint.pprint(get_gpu_info())

def get_Memory_Usage():
  gpus_info = get_gpu_info()
  n_gpus = len(gpus_info)
  mem_tot = 0
  mem_used = 0
  for i in range(n_gpus):
    mem_tot += int(gpus_info[i]['memory.total'])
    mem_used += int(gpus_info[i]['memory.used'])
  return mem_used/mem_tot*100

# print(get_Memory_Usage())

def get_GPU_util():
  gpus_info = get_gpu_info()
  n_gpus = len(gpus_info)
  util = 0
  for i in range(n_gpus):
    util += int(gpus_info[i]['utilization.gpu'])
  return util/i

# print(get_GPU_util())


## Get current GPU utilities
mem_used = get_Memory_Usage()
gpu_util = get_GPU_util()
now = datetime.datetime.now()
df_now = pd.Series({"Time":now,
                    "Memory_Usage (%)":mem_used,
                    "GPU_Util (%)":gpu_util,
                     })


## Update the logging table
log_start_time = now - datetime.timedelta(minutes=log_min)
df = df.append(df_now, ignore_index=True)


## Save
df.to_csv(csv_path, index=False)


## Caluculate Metrices
df_for_calc = df[log_start_time < df['Time']]
mem_used_delta = abs(df_for_calc['Memory_Usage (%)'].diff(1)).mean()
gpu_util_mean = df_for_calc['GPU_Util (%)'].mean()
print(mem_used_delta, gpu_util_mean)


## Decide whether to shutdown or not
condition_1 = (log_min < len(df)) # Time
condition_2 = (mem_used_delta < mem_used_delta_threshould) # Mem
condition_3 = (gpu_util_mean < gpu_util_mean_threshould) # Util
print(condition_1, condition_2, condition_3)
# rm /tmp/gpu_utils.csv

if [condition_1, condition_2, condition_3] == [True, True, True]:
  os.remove(csv_path)
  os.system('shutdown now')
