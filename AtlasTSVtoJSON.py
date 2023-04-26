import sys
import os
import json
import re
from datetime import datetime
import time
import csv
"""
This is a script to parse the .tsv file outputed by Expression ATLAS. 
Input files can be gather here: https://www.ebi.ac.uk/gxa/home

Things to address:
-output file name should probably be from user input. 
-Adjust code so the input file from another dictory instead of the same as the python directory
-Where should the output file be?
"""
def parserAtlas(file_name):
    t0= time.clock() #test code efficiency
    if len(file_name) < 2:
        print("Error: parserPubmed(<file_name>) is empty")
        sys.exit()
    if not os.path.basename(file_name):
        print("Error: The specified file does not exist.")
        sys.exit()
    output_dir = os.path.dirname(file_name)
    outputFileName = file_name.split(".")[1]
    outputFileName = outputFileName.split("\\")[1]
    output_path = outputFileName + ".json"
    print(output_path)
    #Read in file. Note that this may need to adjusted 
    with open(file_name, 'r', encoding="utf8") as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t')
        rows = []
        log = 0.000
        for row in reader:
            if row["log_2 fold change"] != None:
                log = float(row["log_2 fold change"])
            else:
                print("log contains string")
            rows.append({
                "Gene ref": row["Gene"],
                "Species" : row["Comparison"],
                "Experiment accesion": row['Experiment accession'],
                "log_2 fold change": log,
                "Adjusted p-value" : row["Adjusted p-value"],
                "t-statistic" : row["t-statistic"]
            })
                    
    try:
        os.makedirs(output_dir, exist_ok=True) #!!!!!adjust this if output file needs to be in a different place!
        with open(output_path, "w", encoding ="utf8") as f:
            json.dump(rows, f, indent=4)
            #^this for loop is to make sure the output is formatted correctly. 
            print("Output file saved as", output_path)
        

    except OSError as e:
        print("Error writing to file:", e)
        sys.exit()
    t1 = time.clock()
    print("Time elapsed: ", t1 - t0)
   
parserAtlas('.\differentialResults.tsv')