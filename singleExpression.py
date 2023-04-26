import requests
import json
from tqdm.auto import tqdm
from urllib.request import urlopen
#This is a program that uses EBI search to pull some information out of single cell expression atlas
#This program uses cross-referencing of two domains: 
#It will result in 3 files, 1) containing the SC ATLAS ids of a query, 
# 2)containing experiment accessions
# 3)  Experiment information for each accession 
#In order to write the program, I tested queries here: https://www.ebi.ac.uk/ebisearch/documentation/rest-api#examples
#And used this python library: https://github.com/bebatut/ebisearch
#The python library is useful for finding possible domains and fields

def singlecell_expression_atlas_api(query_term):
    url = f"https://www.ebi.ac.uk/ebisearch/ws/rest/sc-genes?query={query_term}&size=1000&format=idlist"
    #print(url)
    response = requests.get(url)
    # Check if the response was successful
    if response.status_code == 200:
        # Parse the response JSON
        #response_json = response.json()
        ids = {}
        ids = response.content.decode()
        idDict = list(ids.split("\n"))
        print(len(idDict), "Single Cell ATLAS ids retrieved \n")
        #print(idDict)
        # Save the response JSON to a file
        with open(f"{query_term}._sc_json", "w") as file: 
            file.write(ids) #This file contains the ATLAS IDs of a gene
        with open(f"{query_term}__sc_info.json", "w") as file: #uses ids retrieved to get ATLAS accession
                experimentList = {}
                names = []
                for i in tqdm(range(len(idDict)), desc="exp ids"):
                    x= idDict[i]
                    #print(x)
                    retrieveurl= f"https://www.ebi.ac.uk/ebisearch/ws/rest/sc-genes/entry/{x}/xref/sc-experiments?fields=name&size=100&format=json"
                    #&filter=id:{x}
                    ##EMBL,ENTREZGENE,GO,INTERPRO,REFSEQ,TAXONOMY, comparison,EMBL,ENTREZGENE,GO,INTERPRO,REFSEQ,T
                    #print(retrieveurl)
                    response = requests.get(retrieveurl)
                    data = response.json()
                    #print(data)

                    for entry in data["entries"]:
                         for reference in entry["references"]:
                            names.extend(reference['fields'].get('name', {}))
                json.dump(names, file)
                print(len(names), " experiments found \n")
                    #json.dump(ebisearch.get_entries( domain="atlas-genes-differential",
                    #entryids= idDict[i], fields="organism_part,ATLAS,comparison,description,domain_source,name,"), file)
                   
        with open(f"{query_term}__sc_acc_info.json", "w") as exfile: #uses ids retrieved to get ATLAS accession
                exList = {}
                for i in tqdm(range(len(names)), desc= "exp info"):
                    acc= names[i]
                    #print(acc)
                    experimentsURL= f"https://www.ebi.ac.uk/ebisearch/ws/rest/sc-experiments?query={acc}&size=100&fields=description,celltype,factors,collection,technology,species,&format=json"
                    exRequest = requests.get(experimentsURL)
                    test= exRequest.content.decode()
                    exList[acc]= test
                    json.dump(exList[acc], exfile)
                        #print(exList[acc])
                        #print(exList[acc])
                    #print(retrieve)

#print(ebisearch.get_retrievable_fields(domain="atlas-genes-differential"))

singlecell_expression_atlas_api("brca1")
#url = 'https://www.ebi.ac.uk/ebisearch/ws/rest/atlas-genes-differential?query={id}&size=1000&fields=organism_part,ATLAS&format=json'
#https://www.ebi.ac.uk/ebisearch/ws/rest/atlas-experiments?query=E-GEOD-66217&fields=description,%20log