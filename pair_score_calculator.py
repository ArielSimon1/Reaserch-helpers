#!/usr/bin/env python
import sys
import os
import itertools
import operator
from collections import Counter
import numpy as np

def get_ids(results_file):
    res = open(results_file)
    check = 0
    id_dict = {}
    for line in res:
        if line.startswith("Query="):
            id = line[7:35].strip()
            if id not in id_dict.keys():
                id_dict[id] = {}
            check = 1
    res.close()
    if check == 0:
        print("there is no sequence IDs")
        exit(0)
    return id_dict

def get_taxon(results_file, id_dict):
    taxon_dict = {}
    counter = 0
    for value in id_dict:
        taxon_dict[value] = []
        res = open(results_file)
        for line in res:
            if line.__contains__(value):
                counter = counter + 1
                res.readline()
                res.readline()
                res.readline()
                res.readline()
                res.readline()
                for x in range(100):
                    new_line = res.readline()
                    if new_line != "\n":
                        taxon = new_line.strip()
                        tmp = new_line.split()
                        taxon_dict[value].append(tmp[0])
                    elif (new_line == "\n" and x==1):
                        taxon_dict[value].append("***** No hits found *****")
                        break
                break
        res.close()
    return taxon_dict

########## MAIN ##########
# usage check
if (len(sys.argv) < 2):
    print("Usage example: python3 blastn_checker.py [blastn results file name]")
    exit(1)

# input file check
isExist = os.path.exists(sys.argv[1])
if (isExist == False):
    print("the file name isn't exists.")
    exit(1)

# set the input file
resultsFile = sys.argv[1]
id_dict = get_ids(resultsFile)

taxons = get_taxon(resultsFile, id_dict)

# d = [value for value in taxons[1] if value in taxons[2]]
Ids_dic = list(taxons.items())
for i in range(len(id_dict)):
    for j in range(len(id_dict)):
        x = np.array(Ids_dic[i][1:100])
        y = np.array(Ids_dic[j][1:100])
        if (i != j):
            if ( len(np.intersect1d(x,y)) > 90):
                print((list(id_dict.items()))[i][0],"with",(list(id_dict.items()))[j][0], "have grade of:", len(np.intersect1d(x,y)))
