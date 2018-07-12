#!/usr/bin/python

import json, csv
from collections import OrderedDict
import os, glob
import ast
import numpy as np

SESSION = "pre"
DIR = "./freeExploration"
REWRITE_DIR = os.path.join(DIR,"rewrite")
FILES = glob.glob(DIR+"/*.log")
FILES.sort()

output_filename = "free_"+SESSION+".csv"
TOTAL_NUM = 12

ofile  = open(output_filename, "w")
csv_out = csv.writer(ofile, delimiter=',')

csv_out.writerow(["id","initial","timestamp",'pre_t0', 'pre_total_duration', 'pre_multi_entropy'])

prev_id = ''

for f in FILES:
    if SESSION not in f:
        continue

    print f.replace("\n","")
    row = []
    row += f.replace(".log","").replace("\n","").split("_")[1:]
    row += [0,0]

    if prev_id == row[0]:
        print "duplicate: " + row[0] 
        print
    
    prev_id = row[0]

    try:
        inf = open(f)
        input_dict = json.loads(inf.read(), object_pairs_hook=OrderedDict)
        with open(os.path.join(REWRITE_DIR, os.path.basename(f)), "w") as outf:
            outf.write(json.dumps(input_dict, indent=2, sort_keys=True))
    except IOError as e:
        print 'File does not exist: {0:s}'.format(e.filename)


    for key in input_dict:
        #if row[0] == "p104":
        #    print(json.dumps(input_dict[key], indent=2, sort_keys=True))

        if input_dict[key]["comment"] == "user_answer":
            # print input_dict[key]["obj"]
            if "pos" in input_dict[key]["obj"]:
                row[3] += 1
            elif "neg" in input_dict[key]["obj"]:
                row[4] += 1


    #if row[3] + row[4] != TOTAL_NUM:
    #    print "total number of answer doesn't match: " + str(row[3]+row[4]) +"/" + str(TOTAL_NUM)+"\n"
        #exit()


    csv_out.writerow(row)







