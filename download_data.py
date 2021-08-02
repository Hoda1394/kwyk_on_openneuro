#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 06:06:08 2021
Download openneuro data

@author: hoda
"""
import subprocess as sp
import json

with open("T1_openneuro.json","r") as fp:
    data_list = json.load(fp)
    
for path in data_list:
    p0=sp.run(["datalad","get", "-d", "../openneuro", path], stdout=sp.PIPE, stderr=sp.STDOUT,text=True)
    print(p0.stdout)
    print("========================================================================")
    
