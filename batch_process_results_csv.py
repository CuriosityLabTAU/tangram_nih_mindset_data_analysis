#!/usr/bin/python
import os, glob
import re
import sys, getopt

import process_tangram_csv
import process_spatial_csv
import process_mindset_csv
import process_free_csv


def main(argv):

    dir = "./results/txt"
    dir = "./processed_data/txt"

    if argv[0] == '-h':
        print 'batch_process_result_csv.py <analysis_argv1> <analysis_argv2> ...'
        sys.exit()

    if len(argv) == 0 :
        argv = ['tangram', 'mindset', 'spatial', 'free']

    print("Analysis Type = ", argv)

    result=''
    for root, subdirs, files in os.walk(dir):
        for filename in files:
            if "tangram" in argv and "tangram" in filename:
                print(filename)
                result = process_tangram_csv.analyze_result(filename, root)
            elif "mindset" in argv and "mindset" in filename:
                print(filename)
                result = process_mindset_csv.analyze_result(filename, root)
            elif "spatial" in argv and "spatial" in filename:
                print(filename)
                result = process_spatial_csv.analyze_result(filename, root)
            elif "free" in argv and "free" in filename:
                print(filename)
                result = process_free_csv.analyze_result(filename, root)
            print result




if __name__ == "__main__":
    main(sys.argv[1:])
