import ebisearch
#print(ebisearch.get_retrievable_fields(domain="atlas-genes-differential"))
print(ebisearch.get_entries(
        domain="atlas-genes-differential",
        entryids="ENSG00000012048",
        fields="description,domain_source,id,name,organism_part"))
