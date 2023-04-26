def getexperiment_sc_IDF(file_name):
    files = file_name
    hugo_ref = file_name.split("info.json")[0]
    folder = hugo_ref + "_sc-atlafiles"
    if not os.path.exists(folder): #create a directory
        os.mkdir(folder)
    #^this is to create a new directory
    currentfile = []
    experimentfiles = []
    if os.path.isfile("sc_atlas_experiments_current"):
        with open("sc_atlas_experiments_current", "r") as sc:
            currentfile = [line.rstrip('\n') for line in sc]
        sc.close()
    print(len(currentfile))
    with open(file_name, "r") as experiments:
        experimentfiles = json.load(experiments)
    #print(experimentfiles)
    print(len(experimentfiles))
    count = 0
    cwd = os.getcwd()
    for ex in range(len(experimentfiles)):
        if experimentfiles[ex] not in currentfile:
            print(experimentfiles[ex], "is either inaccessible or archived")
            count+=1
        else:
            file = "sc-atlas_files//"+experimentfiles[ex]+".idf.txt"
            shutil.copy2(file, folder, follow_symlinks=True)
            #copy file into new folder
    experiments.close()
    print(count)

getexperimentIDF("brca1_sc_info.json")