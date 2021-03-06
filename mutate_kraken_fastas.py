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

'''
for file in os.listdir(curr_dir+"/Train_NT/"):
    if file.endswith(".fna"):
        acc = file[0:15]
        taxid = acc_to_taxid.get(str(acc))
        final = open(curr_dir+"/Train_NT/"+str(acc)+".fna2", "w")
        with open(curr_dir+"/Train_NT/"+file) as fp:
<<<<<<< HEAD
            line = fp.readline()
            while line:
                if ">" in line:
                    final.write(">"+str(acc)+"|kraken:taxid|"+str(taxid)+"\n")
                else:
                    final.write(line)
                line = fp.readline()
        final.close()
'''

for file in os.listdir(curr_dir+"/Train_CD/"):
    if file.endswith(".fna"):
        acc = file[0:15]
        taxid = acc_to_taxid.get(str(acc))
        final = open(curr_dir+"/Train_CD/"+str(acc)+".fna2", "w")
        with open(curr_dir+"/Train_CD/"+file) as fp:
            line = fp.readline()
            while line:
                if ">" in line:
                    final.write(">"+str(acc)+"|kraken:taxid|"+str(taxid)+"\n")
                else:
                    final.write(line)
                line = fp.readline()
        final.close()



for file in os.listdir(curr_dir+"/Train_AA/"):
    if file.endswith(".faa"):
        acc = file[0:15]
        taxid = acc_to_taxid.get(str(acc))
        final = open(curr_dir+"/Train_AA/"+str(acc)+".faa2", "w")
        with open(curr_dir+"/Train_AA/"+file) as fp:
=======
>>>>>>> ffdc66ff7395e4dfc5718b28d011d4098bdb3701
            line = fp.readline()
            while line:
                if ">" in line:
                    final.write(">"+str(acc)+"|kraken:taxid|"+str(taxid)+"\n")
                else:
                    final.write(line)
                line = fp.readline()
        final.close()
