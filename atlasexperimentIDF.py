import json
import ftplib
from ftplib import FTP, error_perm
import os, sys, os.path
import urllib.request
from urllib.parse import urlparse
import tqdm
import shutil
#To run getexperimentIDF, you must have the atlas_files folder generated by ftp_atlas
#and a gene's acc_info.json file generated by atlasExperiment-names. 
def getexperimentIDF(file_name):
    files = file_name
    hugo_ref = file_name.split("info.json")[0]
    folder = hugo_ref + "atlafiles"
    if not os.path.exists(folder): #create a directory
        os.mkdir(folder)
    #^this is to create a new directory
    currentfile = []
    experimentfiles = []
    if os.path.isfile("atlas_experiments_current.txt"):
        with open("atlas_experiments_current.txt", "r") as current:
            currentfile = [line.rstrip('\n') for line in current]
        current.close()
    with open(file_name, "r") as experiments:
        experimentfiles = json.load(experiments)
    #print(experimentfiles)
    print(len(experimentfiles))
    count = 0
    cwd = os.getcwd()
    for ex in range(len(experimentfiles)):
        if experimentfiles[ex] not in currentfile:
            print(experimentfiles[ex], "is either inaccessible or archived")
        else:
            file = "atlas_files//"+experimentfiles[ex]+".idf.txt"
            shutil.copy2(file, folder, follow_symlinks=True)
            #copy file into new folder
    experiments.close()
def getexperiment_sc_IDF(file_name):
    files = file_name
    hugo_ref = file_name.split("info.json")[0]
    folder = hugo_ref + "_sc-atlafiles"
    if not os.path.exists(folder): #create a directory
        os.mkdir(folder)
    #^this is to create a new directory
    currentfile = []
    experimentfiles = []
    if os.path.isfile("sc_atlas_experiments_current.txt"):
        with open("sc_atlas_experiments_current.txt", "r") as sc:
            currentfile = [line.rstrip('\n') for line in sc]
        sc.close()
    with open(file_name, "r") as experiments:
        experimentfiles = json.load(experiments)
    #print(experimentfiles)
    #print(len(experimentfiles))
    count = 0
    cwd = os.getcwd()
    for ex in range(len(experimentfiles)):
        if experimentfiles[ex] not in currentfile:
            print(experimentfiles[ex], "is either inaccessible or archived")
            count+=1
        else:
            file = "sc-atlas_files//"+experimentfiles[ex]+".idf.txt"
            shutil.copy2(file, folder, follow_symlinks=True)
            #copy file into new folder
    experiments.close()
    print(count)
def main():
    print("===")
if __name__== "__main__":
  main()
  getexperimentIDF("brca1_info.json")
  main()
  getexperiment_sc_IDF("brca1_sc_info.json")
  main()

