#!/usr/bin/python

import json, csv
from collections import OrderedDict
import os, glob

SESSION = "pre"
DIR = "./spatial"
FILES = glob.glob(DIR+"/*.log")
FILES.sort()

output_filename = "spatial_"+SESSION+".csv"
TOTAL_NUM = 16

ofile  = open(output_filename, "w")
csv_out = csv.writer(ofile, delimiter=',')

csv_out.writerow(["id","initial","timestamp","#correct","#wrong"])

correct_sequence = {'pre': {}, 'post': {}}
correct_sequence['pre'] = ["1_A","3_B","5_C","7_A","9_D","11_A","13_B","15_A","17_B","19_B","21_C","23_D","25_D","27_D","29_B","31_C"]
correct_sequence['post'] = ["2_D","4_C","6_D","8_A","10_C","12_D","14_C","16_C","18_A","20_D","22_A","24_B","26_C","28_B","30_A","32_B"]


for f in FILES:
    if SESSION not in f:
        continue

    print f.replace("\n","")
    row = []
    row += f.replace(".log","").replace("\n","").split("_")[1:]
    row += [0,0]

    try:
        inf = open(f)
        input_dict = json.loads(inf.read(), object_pairs_hook=OrderedDict)
        #print(json.dumps(input_dict, indent=2, sort_keys=True))
    except IOError as e:
        print 'File does not exist: {0:s}'.format(e.filename)


    for key in input_dict:
        #print(json.dumps(input_dict[key], indent=2, sort_keys=True))

        if input_dict[key]["comment"] == "user_answer":
            # print input_dict[key]["obj"]
            if input_dict[key]["obj"] in correct_sequence[SESSION]:
                row[3] += 1
            else:
                row[4] += 1


    if row[3] + row[4] != TOTAL_NUM:
        print "total number of answer doesn't match: " + str(row[3]+row[4]) +"/" + str(TOTAL_NUM)+"\n"


    csv_out.writerow(row)







