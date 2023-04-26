# Instructions 

### expression_atlas_api("<<hugo_ref>>")
##### atlasExperiment-names.py
The query must be a hugo reference for this block of code to work. 
This is a program that uses EBI search to pull some information out of expression atlas
It will result in 3 files,
1) containing the ATLAS ids of a hugo_ref, 
2)containing experiment accessions for each ATLAS id
3)  Experiment information for each accession 

### singlecell_expression_atlas_api("<<query>>")
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

### get_atlas_files('<<url_ftp>>')
#### ftp_atlas.py
This is a program to pull atlas experiment idf files
This program goes to this directory: http://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments/
and pulls files that end in idf.txt. it should ignore files that don't start with "E-"
This directory contains atlas experiment information. 

### get_sc_atlas_files('<<url>>')
#### sc_atlas_ftp.py
This is a program to pull single cell experiment idf files
This program goes to this directory: http://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/sc-experiments/
and pulls files that end in idf.txt

### get_atlas_files()
### get_SC_atlas_files()
#### currentfiles.py
These programs creates a list of experiment files in each respective local directory
It removes the idf.txt extensions  to match the ftp experiment folder

### getexperimentIDF(<<hugo_ref_info.json>>)
#### atlasexperimentIDF.py
expression_atlas_api generates a list of accession ids, named <<hugo_ref>>_info.json
This takes the list of acc ids and copies the idf.txt files to a new folder for that
hugo reference

