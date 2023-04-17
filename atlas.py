import sys
import os
import json
import re
from datetime import datetime
import time
import csv
"""
This is a script that contains a function to create, 
from these downloaded files, a single json file which contains
a non-redundant set of pubmed records from all these files.

"""
"""""
Useful website: https://www.nlm.nih.gov/bsd/mms/medlineelements.html
Stuff to fix:
# What happens with revised versions of the same article?-revised versions have the same PMID! 
# May need to use PHST- <date> [pubmed] to get a more recent year
#adjust output name?
# This probably can't handle subfolders at the moment
# Right now it has only been tested with parser3.py and the folder in the same
spot. Needs further testing there
#add a part where it can get a pubMed element key as an argument, and then add it to subdata? 
"""""

def parserAtlas(file_name):
    t0= time.clock() #test code efficiency
    if len(file_name) < 2:
        print("Error: parserPubmed(<file_name>,<hugo_ref>, <source>) is missing a value")
        sys.exit()
    if not os.path.basename(file_name):
        print("Error: The specified folder does not exist.")
        sys.exit()
    output_dir = os.path.dirname(file_name)
    outputFileName = file_name.split(".")[1]
    outputFileName = outputFileName.split("\\")[1]
    output_path = outputFileName + ".json"
    print(output_path)
    with open(file_name, 'r', encoding="utf8") as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t')
        rows = []
        for row in reader:
            rows.append({
                "Gene ref": row["Gene"],
                "Species" : row["Comparison"],
                "log_2 fold change": row["log_2 fold change"],
                "Adjusted p-value" : row["Adjusted p-value"],
                "t-statistic" : row["t-statistic"]
            })
                    
    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(output_path, "w", encoding ="utf8") as f:
            json.dump(rows, f, indent=4)
            #^this for loop is to make sure the output is formatted correctly. 
            print("Output file saved as", output_path)
        

    except OSError as e:
        print("Error writing to file:", e)
        sys.exit()
    t1 = time.clock()
    print("Time elapsed: ", t1 - t0)
    # with open (pmidListdoc, "w", encoding ="utf8") as fp:
    #     for item in pmidList:
    #         fp.write("%s\n" % item)
    #     print("done")
    #     fp.close()
    #     print(len(pmidList))
    #print(len(data))
#example run of parsePubmed. likely the folder path needs to be more specific
#at this time, both brca1 & parser3 are in the same folder
parserAtlas('.\differentialResults.tsv')
#parserPubmed("<folder_path>", "<hug_ref>", "<source>")