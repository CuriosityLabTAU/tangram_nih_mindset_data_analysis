#!/usr/bin/python
import os, glob
import re
import sys, getopt

import process_tangram_csv
import process_spatial_csv
import process_mindset_csv
import process_free_csv


def main(argv):
    #dir = "./results/txt"
    dir = "./processed_data/txt"


    if len(argv) == 0:
        argv = ['tangram', 'mindset', 'spatial', 'free']
        argv = ['tangram', 'mindset', 'spatial', 'free']
    elif argv[0] == '-h':
        print 'batch_process_result_csv.py <analysis_argv1> <analysis_argv2> ...'
        sys.exit()



    print("Analysis Type = ", argv)

    result=''
    for root, subdirs, files in os.walk(dir):
        for filename in files:
            if "tangram" in argv and "tangram" in filename:
                print(filename)
                result = process_tangram_csv.analyze_result(filename, root)
                print result
            elif "mindset" in argv and "mindset" in filename:
                print(filename)
                result = process_mindset_csv.analyze_result(filename, root)
                print result
            elif "spatial" in argv and "spatial" in filename:
                print(filename)
                result = process_spatial_csv.analyze_result(filename, root)
                print result
            elif "free" in argv and "free" in filename:
                print(filename)
                result = process_free_csv.analyze_result(filename, root)
                print result

if __name__ == "__main__":
    argv = sys.argv[1:]
    main(argv)
