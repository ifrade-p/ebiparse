import ebisearch
import json
file = "sc_fields.txt"
json.dumps(ebisearch.get_domains())
with open('sc_atlas_experiments.txt', 'w') as f:
    #f.write(json.dumps(ebisearch.get_domains()))
    f.write(json.dumps(ebisearch.get_retrievable_fields(domain="sc-experiments")))
"""
with open('allebi.txt', 'w') as f:
    #f.write(json.dumps(ebisearch.get_domains()))
    f.write(json.dumps(ebisearch.get_retrievable_fields(domain="allebi")))
with open(f"all_experiments_info.json", "w") as file:
    json.dump(ebisearch.get_entries(
        domain="atlas-experiments",
        fields="description,id,name,organism_part"))
"""