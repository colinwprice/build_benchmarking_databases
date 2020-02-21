#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:38:37 2020

@author: cwp5j
"""

import os

#1. Build lookup taxid dictionary
acc_to_taxid = {}

filepath = "coding_domain_training_genome_taxid_sets.txt"
with open(filepath) as fp:
    for _ in range(2):
        next(fp)
    
    line = fp.readline().strip().split()
    
    while line:
        if len(line)<2:
            line = fp.readline().strip().split()
        else:
            acc_to_taxid.update({line[0] : line[2]})
            line = fp.readline().strip().split()
        
fp.close()
        
curr_dir = os.getcwd()

final=open("merged.faa2", "w")

for file in os.listdir(curr_dir+"/Train_AA/"):
    if file.endswith(".faa"):
        acc = file[0:15]
        taxid = acc_to_taxid.get(str(acc))
        with open(curr_dir+"/Train_AA/"+file) as fp:
            line = fp.readline()
            while line:
                if ">" in line:
                    final.write(">"+str(taxid)+"\n")
                else:
                    final.write(line)
                line = fp.readline()

final.close()
