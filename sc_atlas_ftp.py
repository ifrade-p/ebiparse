import json
import ftplib
from ftplib import FTP, error_perm
import os, sys, os.path
import urllib.request
from urllib.parse import urlparse
from tqdm.auto import tqdm
#This program goes to this directory: http://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments/
#and pulls files that end in idf.txt
#it should ignore files that don't start with "E-"

"""
Things to address:
should the txt be what's pulled? 
"""
def get_sc_atlas_files(url):
    url_parts = urlparse(url)
    domain = url_parts.netloc
    path = url_parts.path
    ftp = ftplib.FTP(domain)
    ftp.login()
    ftp.cwd(path)
    folders = ftp.nlst()
    if not os.path.exists("sc-atlas_files"): #create a directory
        os.mkdir("sc-atlas_files")
    #get subfolders:
    atlasFiles = []
    atlasFolders = []
    ftp.retrlines("LIST", atlasFolders.append)
    atlasFolders = [x.split()[-1] for x in atlasFolders if x.startswith("d")]
    atlasFolders = [f for f in atlasFolders if f.startswith("E-")]
    currentfiles = []
    newfiles = []
    if os.path.isfile("sc-atlas_experiments_current.txt"):
        with open("sc-atlas_experiments_current.txt", "r") as current:
            currentfiles = [line.rstrip('\n') for line in current]

    for i in range(len(atlasFolders)):
        if atlasFolders[i] not in currentfiles:
             newfiles.append(atlasFolders[i])
    print("There are", len(atlasFolders), "total experiment folders.")
    print("There are", len(currentfiles), "experiment files currently downloaded")
    print("There are", len(newfiles), "new possible experiment folder.")
    print("*This includes inaccessible folders and archived files. ")
    unaccessibleFiles = []
    unaccessibleFilesCount=0
    #print(atlasFolders)
    #This for loop gets all the txt files in each folder.
    fp = open("atlas_experiments.txt", "a") #this file will contain list of experiments
    for i in tqdm(range(len(newfiles)), desc="txt retrieval"):
        folder = newfiles[i]
        #print(folder)
        try:
            ftp.cwd(folder)
            files = []
            ftp.retrlines("NLST", files.append)
            txt_files = [f for f in files if (f.endswith("idf.txt"))]
            # download each txt file to the atlas_files folder
            for txt_file in (txt_files):
                if not os.path.exists(txt_file):
                    with open(os.path.join("sc-atlas_files", txt_file), "wb") as f:
                        ftp.retrbinary("RETR " + txt_file, f.write)
                        atlasFiles.append(txt_file)
                        #print(txt_file)
                        f.close()
            ftp.cwd("..")
        except error_perm as e:
            unaccessibleFiles.append(folder)
            unaccessibleFilesCount+=1
            #print({e})
            #print(folder)

        #print("\n",folder)
        
        #print("\n"+folder)
    
    print("There are", unaccessibleFilesCount, " inaccessible files")
    ftp.quit()
    fp.close()
    with open("sc_atlas_experiments_current.txt", "a") as fileslist:
        for x in tqdm(atlasFiles):
                x= x.split(".")[0]
                fileslist.write(x+"\n")
    fileslist.close()
    with open("sc_atlas_experiments_inaccessible.txt", "w") as iaf:
        for x in tqdm(unaccessibleFiles):
                iaf.write(x+"\n")
    iaf.close()
    archivedfiles = 0
    for i in range(len(newfiles)):
        if newfiles[i] not in unaccessibleFiles:
             archivedfiles+=1
             #print(newfiles[i])
    print("There are ", archivedfiles, "archived files.")
    print("Done!")

get_sc_atlas_files('http://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/sc_experiments/')