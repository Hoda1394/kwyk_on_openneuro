#!/usr/bin/env python3

import glob
import json
import pandas as pd

def get_table(json_path):
    # read the json file
    with open(json_path, "r") as file:
        dic = json.load(file)
        
    return pd.DataFrame.from_dict(dic)
    
if __name__ == "__main__":
    
    #root = "/om/user/hodaraja/ukb/data/T1_mri/"
    # get list of available tables
    table_list = glob.glob("table_*")
    
    #get the first table
    table = get_table(table_list[0])

    for table_path in table_list[1:]:
        this_table = get_table(table_path)
        table = pd.concat([table, this_table], axis=0)
        
    # save the final table
    table.to_csv("kwyk_openneuro.csv", index=False)
        
        
        
        
    


