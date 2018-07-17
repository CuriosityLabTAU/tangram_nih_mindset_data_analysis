#!/usr/bin/python

import json, csv
from collections import OrderedDict
import os, glob
import sys

def main(argv):
	SESSION = argv[1]
	DIR = argv[0]
	FILES = glob.glob(DIR+"/*.log")
	FILES.sort()

	output_filename = "buffyfluffy_"+SESSION+".csv"
	TOTAL_NUM = 12

	ofile  = open(output_filename, "w")
	csv_out = csv.writer(ofile, delimiter=',')

	csv_out.writerow(["id","initial","timestamp","#pos","#neg"])

	for f in FILES:
	    if SESSION not in f:
	        continue

	    print f.replace("\n","")
	    row = []
	    row += f.split("/")[-1].replace(".log","").replace("\n","").split("_")[1:]
	    row += [0,0,0]

	    try:
	        inf = open(f)
	        input_dict = json.loads(inf.read(), object_pairs_hook=OrderedDict)
	        #if row[0] == "p112":
	        #    print(json.dumps(input_dict, indent=2, sort_keys=True))
	    except IOError as e:
	        print 'File does not exist: {0:s}'.format(e.filename)


	    for key in input_dict:
	        #if row[0] == "p104":
	        #    print(json.dumps(input_dict[key], indent=2, sort_keys=True))

	        if input_dict[key]["comment"] == "user_answer":
	            # print input_dict[key]["obj"]
	            if "pos_" in input_dict[key]["obj"]:
	                row[3] += 1
	            elif "neg_" in input_dict[key]["obj"]:
	                row[4] += 1


	    if row[3] + row[4] != TOTAL_NUM:
	        print "total number of answer doesn't match: " + str(row[3]+row[4]) +"/" + str(TOTAL_NUM)+"\n"
	        #exit()
	    row[5] = row[3]/float(row[3]+row[4])

	    csv_out.writerow(row)


if __name__ == "__main__":
    main(sys.argv[1:])




