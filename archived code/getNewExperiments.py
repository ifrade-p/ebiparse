import json
import re
import ftplib
from ftplib import FTP
import os, sys, os.path
import urllib.request
from urllib.parse import urlparse
from tqdm.auto import tqdm
#This program goes to this directory: http://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments/
#and pulls files that end in .txt
#RDF is the last folder checked. 
"""
Things to address:
should the txt be what's pulled? 
"""
def get_atlas_new_experiments(url):
    url_parts = urlparse(url)
    domain = url_parts.netloc
    path = url_parts.path
    ftp = ftplib.FTP(domain)
    ftp.login()
    ftp.cwd(path)
    folders = ftp.nlst()
    if not os.path.exists("atlas_files"): #create a directory
        os.mkdir("atlas_files")
    #get subfolders:
    atlasFolders = []
    ftp.retrlines("LIST", atlasFolders.append)
    atlasFolders = [x.split()[-1] for x in atlasFolders if x.startswith("d")]
    #print(atlasFolders)
    #This for loop gets all the txt files in each folder.
    count = 0
    atlasExperimentsFile = open("atlas_experiments.txt", "r")
    currentExperiments = atlasExperimentsFile.read()
    ExperimentList = currentExperiments.split("\n")
    newExperiments = []
    for folder in tqdm(atlasFolders):
        #ftp.cwd(folder)
        #print(folder)
        # get a list of all the txt files in the current folder
        if folder.startswith("E-") and folder not in ExperimentList:
            newExperiments.append(folder)
            files = []
            ftp.retrlines("NLST", files.append)
            txt_files = [f for f in files if f.endswith("idf.txt")]
            count=0
            experimentlist = {}
            # download each txt file to the atlas_files folder
            for txt_file in txt_files:
                #with open(os.path.join("atlas_files", txt_file), "wb") as f:
                #   ftp.retrbinary("RETR " + txt_file, f.write)
                    experimentACC= txt_file.split(".")[0]
                    experimentlist[count]= experimentACC
                    #print(experimentlist[count])
                    count+=1
        ftp.cwd("..")
        ftp.quit()
    with open("atlas_experiments.txt", "a") as fp:
        for ex in newExperiments:
            fp.write(ex+"\n")

    print("Done!")

get_atlas_new_experiments('http://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments/')