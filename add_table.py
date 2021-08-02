#!/usr/bin/env python3
import os
import json

root = "/om/user/hodaraja/kwyk_openneuro/"
# find list of tables that are not exist
no_table = []
for i in range(384):
    if not os.path.exists(root+"table_{}".format(i)):
        no_table.append(i)

print(" {} table is missing".format(len(no_table)))
        
# load the id list
with open("T1_openneuro.json", "r") as fp:
    ids = json.load(fp)
               
# extract list of ids that has no output
for chunk_no in no_table:
    # get the Id list
    n = 60
    st = chunk_no * n
    if chunk_no == 383:
        ed = len(ids)
    else:
        ed = st + n
        
    data_list = ids[st:ed]
    # create table
    ID = []
    uncertainty_value =[]
    path = "/om/user/hodaraja/kwyk_openneuro/kwyk_out"
    for data in data_list:
        ds_name = data.split("/")[5]
        file_name = img_name = data.split("/")[-1].split(".")[0]
        # Add Id
        ID.append(ds_name+"_"+file_name)
        # check the uncertainty file existance
        sbj_name = data.split("/")[6]
        out_path= os.path.join(path,ds_name,sbj_name)
        out_file = "out_"+file_name+"_uncertainty.json"
        uncertainty_file = os.path.join(out_path,out_file)
        if os.path.exists(uncertainty_file):
            with open(uncertainty_file, "r") as file:
                uncertainty = json.load(file)
            uncertainty_value.append(uncertainty["uncertainty"])
        else:
            uncertainty_value.append("Nan")
    # save table
    variables={
        "ID": ID,
        "kwyk_uncertainty": uncertainty_value
        }
    with open("table_{}".format(chunk_no), "w") as fp:
        json.dump(variables, fp, indent=4)
    
            
                
            
    
    
        


