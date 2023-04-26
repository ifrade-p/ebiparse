# Instructions 

### expression_atlas_api("brca1")
##### atlasExperiment-names.py
The query must be a hugo reference for this block of code to work. 
This is a program that uses EBI search to pull some information out of expression atlas
It will result in 3 files,
1) containing the ATLAS ids of a hugo_ref, 
2)containing experiment accessions for each ATLAS id
3)  Experiment information for each accession 

### singlecell_expression_atlas_api("<query>")
#### singleExpression.py
This is a program that uses EBI search to pull some information out of single cell expression atlas
This program uses cross-referencing of two domains: 
It will result in 3 files,
1) containing the  SC ATLAS ids of a query, 
2) containing experiment accessions
3)  Experiment information for each accession 

### parserAtlas('<file.tsv>')
#### AtlasTSVtoJSON.py
This is a script to parse the .tsv file outputed by Expression ATLAS. 
Input files can be gather here: https://www.ebi.ac.uk/gxa/home

### get_atlas_files('url_ftp')
#### ftp_atlas.py
This program goes to this directory: http://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments/
and pulls files that end in idf.txt. it should ignore files that don't start with "E-"
This directory contains atlas experiment information. 

### get_sc_atlas_files
#### sc_atlas_ftp.py
#This program goes to this directory: http://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/sc-experiments/
#and pulls files that end in idf.txt
