#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 08:41:45 2021

@author: hoda
"""
import os
import json

path = "/om/user/hodaraja/openneuro/"

file_list=[]
for root, dirs, files in os.walk(path):
    for name in files:
        if "T1w.nii.gz" in name:
            file_list.append(os.path.join(root,name))
            

with open("T1_openneuro.json","w") as fp:
    json.dump(file_list,fp)
            
