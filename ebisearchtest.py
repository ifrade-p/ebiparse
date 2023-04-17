import ebisearch
import json
print(ebisearch.get_retrievable_fields(domain="allebi"))
file = "fields.txt"
with open('allebi.txt', 'w') as f:
    #f.write(json.dumps(ebisearch.get_domains()))
    f.write(json.dumps(ebisearch.get_retrievable_fields(domain="allebi")))
"""""
print(ebisearch.get_entries(
        domain="atlas-genes-differential",
        entryids="ENSG00000012048",
        fields="description,domain_source,id,name,organism_part"))
"""""