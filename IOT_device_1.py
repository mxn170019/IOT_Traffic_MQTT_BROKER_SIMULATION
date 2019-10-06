#!/usr/bin/env python
# coding: utf-8

# In[2]:


import threading
import time
import datetime
import json
import numpy as np
from ddict import DotAccessDict

device_config = 'config_device_1.txt'
device_id = 'config_device_1'

with open(device_config) as json_file:
    conf = DotAccessDict(json.load(json_file))
    conf_device = conf.config_device_1[0]
i = 0 
ls =np.array([])

def printit(): 
    t = threading.Timer((60/conf_device.freq_per_minute), printit)
    t.start()
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    global i 
    global ls
    
    if np.count_nonzero(ls>=conf_device.thershold) >= conf_device.extreme_count:
        x = np.random.randint(low=conf_device.minima, high=conf_device.max_1)
        ls = np.append(ls,x)
    else:
        x = np.random.randint(low=conf_device.minima, high=conf_device.max_2)
        ls = np.append(ls,x)
        
    i += 1   
    measure_value = x
    output = {'device_id':conf_device.id,
            'measure_value':measure_value,
            'time_stamp':st,
            'term':i,
            'count_threshold':np.count_nonzero(ls>=conf_device.thershold),
             'ls':ls
             }
    print(output)
    if i >=conf_device.loops:
        t.cancel()
printit()


# In[ ]:





# In[ ]:





# In[ ]:




