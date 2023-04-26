import json
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
def get_atlas_files():
    folder = os.listdir("atlas_files")
    with open("atlas_experiments_current.txt", "w") as fp:
        for x in tqdm(folder):
            if x.startswith("E-"):
                x= x.split(".")[0]
                fp.write(x+"\n")
    print("Done!")
def get_SC_atlas_files():
    folder = os.listdir("sc-atlas_files")
    with open("sc-atlas_experiments_current.txt", "w") as fp:
        for x in tqdm(folder):
            if x.startswith("E-"):
                x= x.split(".")[0]
                fp.write(x+"\n")
    print("Done!")
get_atlas_files()
get_SC_atlas_files()