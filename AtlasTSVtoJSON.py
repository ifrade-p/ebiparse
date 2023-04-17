import csv
import json
import os

def atlasParser(file_name):
    with open(file_name, 'r', encoding="utf8") as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t')
        rows = []
        for row in reader:
            rows.append({
                "Gene ref": row["Gene"],
                "Species" : row["Comparison"],
                "log_2 fold change": row["log_2 fold change"],
                "Adjusted p-value" : row["Adjusted p-value"],
                "t-statistic" : row["t-statistic"]
            })
        outputFileName = file_name.split(".")[0]
        outputFileName = outputFileName + ".json"
    with open(outputFileName, 'w') as fp:
        json.dump(rows, fp, indent=4, encoding="utf8")

atlasParser(".\\Users\\isabelf\\Downloads\\differentialResults (15).tsv")