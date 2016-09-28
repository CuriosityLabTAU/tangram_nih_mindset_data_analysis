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
        argv = ['tangram', 'mindset', 'spatial']
    elif argv[0] == '-h':
        print 'batch_process_result_csv.py <analysis_argv1> <analysis_argv2> ...'
        sys.exit()


    print("Analysis Type = ", argv)

    tangram_matrix = []
    mindset_matrix = []
    spatial_matrix = []
    free_matrix =[]
    f_spatial_csv = open('processed_data/processed/processed_spatial.csv', 'w')
    f_mindset_csv = open('processed_data/processed/processed_mindset.csv', 'w')
    f_tangram_csv = open('processed_data/processed/processed_tangram.csv', 'w')
    f_free_csv = open('processed_data/processed/processed_free.csv', 'w')

    result=''
    for root, subdirs, files in os.walk(dir):
        for filename in sorted(files):
            if "tangram" in argv and "tangram" in filename:
                print(filename)
                result = process_tangram_csv.analyze_result(filename, root)
                tangram_matrix.append(result)
            elif "mindset" in argv and "mindset" in filename:
                print(filename)
                result = process_mindset_csv.analyze_result(filename, root)
                mindset_matrix.append(result)
            elif "spatial" in argv and "spatial" in filename:
                print(filename)
                result = process_spatial_csv.analyze_result(filename, root)
                spatial_matrix.append(filename)
            elif "free" in argv and "free" in filename:
                print(filename)
                result = process_free_csv.analyze_result(filename, root)
                free_matrix.append()

if __name__ == "__main__":
    argv = sys.argv[1:]
    main(argv)
