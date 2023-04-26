import json
import ftplib
from ftplib import FTP
import os, sys, os.path
import urllib.request
from urllib.parse import urlparse
from tqdm.auto import tqdm
#This program creates a list of experiment files in each local directory
#It removes the idf.txt extensions  to match the ftp experiment folder 
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
    with open("sc_atlas_experiments_current.txt", "w") as fp:
        for x in tqdm(folder):
            if x.startswith("E-"):
                x= x.split(".")[0]
                fp.write(x+"\n")
    print("Done!")

def main():
    print("====")

if __name__== "__main__":
  main()
  get_atlas_files()
  main()
  get_SC_atlas_files()
  main()