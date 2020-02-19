# -*- coding: utf-8 -*-
import shutil
import os
list_of_paths = []
curr_dir = os.getcwd()
filepath = "all_path_list_CD.txt" 

#1. read in all of the paths that I need to a list. Read in all accessions too
filepath = "all_path_list_CD.txt"
with open(filepath) as fp:
    line = fp.readline().strip().split()
    
    while line:
        path = line[0]
        list_of_paths.append(path)
        line = fp.readline().strip().split()
        
#2. change the directory to the directory with both the /genbank and /refseq directories
#/project/biocomplexity/fungcat/genomes/Genomes_AA/
if not os.path.isdir("Train_AA"):
    os.mkdir("Train_AA")
    
    
#3. copy folder labeled by accession to my directory
#/project/biocomplexity/fungcat/colinwp_folder/Train/
if not os.listdir(curr_dir+"/Train_AA/"): #only do if this is empty
    for path in list_of_paths:
        os.chdir("/project/biocomplexity/fungcat/genomes/Genomes_AA"+path)
        faa = [f for f in os.listdir("/project/biocomplexity/fungcat/genomes/Genomes_AA"+path) if f.endswith('.faa')]
        if len(faa) > 0:
            shutil.copy("/project/biocomplexity/fungcat/genomes/Genomes_AA"+path+faa[0], \
                        curr_dir+"/Train_AA/")
else:
    print("Make sure the target folder Train_AA is empty")
