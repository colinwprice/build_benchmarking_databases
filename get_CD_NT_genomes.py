#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" TP BUILD CD
import pickle
index = pickle.load(open("index_initial.pck", "rb"))

list_of_paths = []

filepath = "all_genome_list.txt"
with open(filepath) as fp:
    line = fp.readline().strip().split()
    
    while line:
        acc = line[0]
        
        path = index["genomes"][acc]["location"]
        list_of_paths.append(path)
        line = fp.readline().strip().split()
        
with open('all_path_list_CD.txt', 'w') as file:
    for path in list_of_paths:
        file.write(path)
        file.write('\n')
"""
''' TO BUILD NT (NOTE: ONE MISSING GENOME)
import pickle
index = pickle.load(open("index_initial.pck", "rb"))

list_of_paths = []

filepath = "all_genome_list.txt"
with open(filepath) as fp:
    line = fp.readline().strip().split()
    
    while line:
        acc = line[0]
        if index["genomes"][acc] != {}:
            path = index["genomes"][acc]['location']
            list_of_paths.append(path)
        line = fp.readline().strip().split()
        
with open('all_path_list_NT.txt', 'w') as file:
    for path in list_of_paths:
        file.write(path)
        file.write('\n')
'''


import shutil
import os
list_of_paths = []
curr_dir = os.getcwd()
#1. read in all of the paths that I need to a list. Read in all accessions too
filepath = "all_path_list_CD.txt"
with open(filepath) as fp:
    line = fp.readline().strip().split()
    
    while line:
        path = line[0]
        list_of_paths.append(path)
        line = fp.readline().strip().split()
        


#2. change the directory to the directory with both the /genbank and /refseq directories
#/project/biocomplexity/fungcat/genomes/Genomes_CD/
if not os.path.isdir("Train_CD"):
    os.mkdir("Train_CD")


#3. copy folder labeled by accession to my directory
#/project/biocomplexity/fungcat/colinwp_folder/Train/
if not os.listdir(curr_dir+"/Train_CD/"): #only do if this is empty
    for path in list_of_paths:
        os.chdir("/project/biocomplexity/fungcat/genomes/Genomes_CD"+path)
        fna = [f for f in os.listdir("/project/biocomplexity/fungcat/genomes/Genomes_CD"+path) if f.endswith('.fna')]
        if len(fna) > 0:
            shutil.copy("/project/biocomplexity/fungcat/genomes/Genomes_CD"+path+fna[0], \
                        curr_dir+"/Train_CD/")
else:
    print("Make sure the target folder Train_CD is empty")



#4. Repeat for NT
list_of_paths = []
os.chdir(curr_dir)

filepath = "all_path_list_NT.txt"
with open(filepath) as fp:
    line = fp.readline().strip().split()
    
    while line:
        path = line[0]
        list_of_paths.append(path)
        line = fp.readline().strip().split()

if not os.path.isdir("Train_NT"):
    os.mkdir("Train_NT")      

if not os.listdir(curr_dir+"/Train_NT/"): #only do if this is empty
    for path in list_of_paths:
        os.chdir("/project/biocomplexity/fungcat/genomes/Genomes_NT"+path)
        fna = [f for f in os.listdir("/project/biocomplexity/fungcat/genomes/Genomes_NT"+path) if f.endswith('.fna')]
        if len(fna) > 0:
            shutil.copy("/project/biocomplexity/fungcat/genomes/Genomes_NT"+path+fna[0], \
                        curr_dir+"/Train_NT/")
else:
    print("Make sure the target folder Train_NT is empty")

