#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check Uncertainty on opennero data
Created on Mon Jun  7 15:27:53 2021

@author: hoda
"""
import os
import pandas as pd
import json

# load the id list
with open("T1_openneuro.json", "r") as fp:
    ids = json.load(fp)
    
ID = []
uncertainty_value =[]

# load mask and entropy
        mask = nib.load(output + "_means_orig.nii.gz" ).get_fdata().astype(np.uint8)
        entropy = nib.load(output + "_entropy_orig.nii.gz").get_fdata()
        # calculate uncertainty
        uncertainty = np.mean(ma.masked_where(mask==0, entropy))
        volume_uncertainty = {"uncertainty":uncertainty}
        with open(os.path.join(data, "average_uncertainty.json"), "w") as fp:
            json.dump(volume_uncertainty, fp, indent=4)
        
        uncertainty_value.append(uncertainty)
            
    variables={
        "ID": ID,
        "kwyk_uncertainty": uncertainty_value
        }
    with open("table_{}".format(chunk_no), "w") as fp:
        json.dump(variables, fp, indent=4)
        
    

