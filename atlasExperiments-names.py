import requests
import json
from tqdm.auto import tqdm
#Query can only be a hugo reference now!!!!!!
#This is a program that uses EBI search to pull some information out of expression atlas
#It will result in 3 files, 1) containing the ATLAS ids of a hugo_ref, 
# 2)containing experiment accessions for each ATLAS id
# 3)  Experiment information for each accession 
#In order to write the program, I tested queries here: https://www.ebi.ac.uk/ebisearch/documentation/rest-api#examples
#And used this python library: https://github.com/bebatut/ebisearch
#The python library is useful for finding possible domains and fields

def expression_atlas_api(query_term):
    url = f"https://www.ebi.ac.uk/ebisearch/ws/rest/atlas-genes-differential?query=hgnc_symbol:{query_term}&size=1000&format=idlist"
    #print(url)
    response = requests.get(url)
    # Check if the response was successful
    if response.status_code == 200:
        # Parse the response JSON
        #response_json = response.json()
        ids = {}
        ids = response.content.decode()
        idDict = list(ids.split("\n"))
        #print(idDict)
        # Save the response JSON to a file
        with open(f"{query_term}.json", "w") as file: 
            file.write(ids) #This file contains the ATLAS IDs of a gene
        with open(f"{query_term}_info.json", "w") as file: #uses ids retrieved to get ATLAS accession
                experimentList = {}
                for i in tqdm(range(len(idDict)), desc="first loop"):
                    x= idDict[i]
                    retrieveurl= f"https://www.ebi.ac.uk/ebisearch/ws/rest/atlas-experiments?query={x}&size=10000&fields=ATLAS&format=idlist"
                    #&filter=id:{x}
                    ##EMBL,ENTREZGENE,GO,INTERPRO,REFSEQ,TAXONOMY, comparison,EMBL,ENTREZGENE,GO,INTERPRO,REFSEQ,T
                    #print(retrieveurl)
                    response = requests.get(retrieveurl)
                    retrieve = response.content.decode()
                    experimentList[i]= retrieve.split("\n")
                    #print(retrieve)
                    json.dump(experimentList[i], file)
                    """""
                    json.dump(ebisearch.get_entries( domain="atlas-genes-differential",
                    entryids= idDict[i], fields="organism_part,ATLAS,comparison,description,domain_source,name,"), file)
                    """
        with open(f"{query_term}_acc_info.json", "w") as exfile: #uses ids retrieved to get ATLAS accession
                exList = {}
                for i in range(len(experimentList)):
                    experiments= experimentList[i]
                    print(len(experiments), " experiment accessions found")
                    for acc in tqdm(experiments, desc= "secondloop"):
                        #print(acc)
                        experimentsURL= f"https://www.ebi.ac.uk/ebisearch/ws/rest/atlas-experiments?query={acc}&fields=name,description,tissue,TAXONOMY,disease,organism_part,normalized_connections&format=json"
                        exRequest = requests.get(experimentsURL)
                        exList[acc]= exRequest.content.decode()
                json.dump(exList[acc], exfile)
                        #print(exList[acc])
                        #print(exList[acc])
                    #print(retrieve)

#print(ebisearch.get_retrievable_fields(domain="atlas-genes-differential"))
  
expression_atlas_api("brca1")
#url = 'https://www.ebi.ac.uk/ebisearch/ws/rest/atlas-genes-differential?query={id}&size=1000&fields=organism_part,ATLAS&format=json'
#https://www.ebi.ac.uk/ebisearch/ws/rest/atlas-experiments?query=E-GEOD-66217&fields=description,%20log