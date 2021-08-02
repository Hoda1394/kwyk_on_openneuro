#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 06:40:16 2021
run kwyk on openneuro T1 images

@author: hoda
"""
import os
import json
import sys
import subprocess as sp


if __name__ == "__main__":
    
    # load the id list
    with open("T1_openneuro.json", "r") as fp:
        ids = json.load(fp)
        
                
    chunk_no = int(sys.argv[1])
    # number of the files to run the container
    n = 60
    st = chunk_no * n
    if chunk_no == 383:
        ed = len(ids)
    else:
        ed = st + n
        
    data_list = ids[st:ed]
    
    # save the values
    ID = []
    uncertainty_value =[]
    path = "/om/user/hodaraja/kwyk_openneuro/kwyk_out"
    image = "kwyk_master-gpu.sif"
    for data in data_list:
        # create folder and build the output path
        ds_name = data.split("/")[5]
        sbj_name = data.split("/")[6]
        file_name = img_name = data.split("/")[-1].split(".")[0]
        out_path= os.path.join(path,ds_name,sbj_name)
        os.makedirs(out_path, exist_ok=True)
        out_file = os.path.join(out_path,"out_"+file_name)
        
        ID.append(ds_name+"_"+file_name)
        # run kwyk on data
        cmd = ["singularity", "run", "-e", "-B", "$(pwd):/data",
               "-B", "/om/user/hodaraja/openneuro/",
               "-W", "/data", 
               "--nv", 
               image, 
               "-m", 
               "bvwn_multi_prior", 
               "-n", "2", 
               "--save-variance",
               "--save-entropy", 
               data,
               out_file]
        
        p0 = sp.run(cmd, stdout=sp.PIPE, stderr=sp.STDOUT ,text=True)
        print(p0.stdout)
        
        # load mask and entropy
        uncertainty_file = out_file+"_uncertainty.json"
        with open(uncertainty_file) as f:
            var = json.load(f)
        
        uncertainty_value.append(var["uncertainty"])
        
        
    variables={
        "ID": ID,
        "kwyk_uncertainty": uncertainty_value
        }
    with open("table_{}".format(chunk_no), "w") as fp:
        json.dump(variables, fp, indent=4)
            
        
        
            
        
        
        
        
        
    
   
       
    
    
    
