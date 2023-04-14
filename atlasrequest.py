import requests
import json
import ebisearch

def expression_atlas_api(query_term):
    url = f"https://www.ebi.ac.uk/ebisearch/ws/rest/atlas-genes-differential?query={query_term}&size=10000&format=idlist"
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
        idfromList = " "
        with open(f"{query_term}.json", "w") as file:
            file.write(ids)
        
        with open(f"{query_term}_info.json", "w") as file:
                #for i in range(0,100):
                    i = 0
                    x= idDict[i]
                    retrieveurl= f"https://www.ebi.ac.uk/ebisearch/ws/rest/atlas-genes-differential?query={idDict[i]}&fields=organism_part,ATLAS,EMBL,ENTREZGENE,GO,INTERPRO,REFSEQ,TAXONOMY,id,description,name&format=json"
                    #&filter=id:{x}
                    ##EMBL,ENTREZGENE,GO,INTERPRO,REFSEQ,TAXONOMY
                    #print(retrieveurl)
                    response = requests.get(retrieveurl)
                    retrieve = response.content.decode()
                    #print(retrieve)
                    json.dump(retrieve, file)
                    """""
                    json.dump(ebisearch.get_entries( domain="atlas-genes-differential",
                    entryids= idDict[i], fields="organism_part,ATLAS,description,domain_source,name,"), file)
                    """

        print(f"API request for query term '{query_term}' successful")
    else:
        print(f"API request for query term '{query_term}' failed with status code {response.status_code}")

#print(ebisearch.get_retrievable_fields(domain="atlas-genes-differential"))
  
expression_atlas_api("brca1")
#url = 'https://www.ebi.ac.uk/ebisearch/ws/rest/atlas-genes-differential?query={id}&size=1000&fields=organism_part,ATLAS&format=json'