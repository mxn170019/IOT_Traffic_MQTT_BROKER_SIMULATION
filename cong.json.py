#!/usr/bin/env python
# coding: utf-8

# In[48]:


#Generate Config file
import json

device_id = "config_device_2"
d_id = 'device_1'
data = {}
data[device_id] = []
data[device_id].append({
    'id':d_id,
    'freq_per_minute': 10,
    'minima': 60,
    'max_1':75,
    'max_2':85,
    'thershold':75,
    'extreme_count':5})

with open(device_id+".txt", 'w') as outfile:
    json.dump(data, outfile)


# In[ ]:




