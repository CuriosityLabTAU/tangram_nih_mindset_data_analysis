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

    #init txt files:
    f_tangram_txt = open('processed_data/processed/processed_tangram.txt', 'w')
    f_spatial_txt = open('processed_data/processed/processed_spatial.txt', 'w')
    f_mindset_txt = open('processed_data/processed/processed_mindset.txt', 'w')
    f_free_txt = open('processed_data/processed/processed_free.txt', 'w')

    f_all_txt = open('processed_data/processed/processed_all.txt', 'w')

    #set headers:
    headers_tangram = process_tangram_csv.get_headers()
    headers_mindset = process_mindset_csv.get_headers()
    headers_spatial = process_spatial_csv.get_headers()
    headers_free = process_free_csv.get_headers()

    for header in headers_tangram:
        f_tangram_txt.write(str(header) + '\t')
    f_tangram_txt.write('\n')

    for header in headers_mindset:
        f_mindset_txt.write(str(header) + '\t')
    f_mindset_txt.write('\n')

    for header in headers_spatial:
        f_spatial_txt.write(str(header) + '\t')
    f_spatial_txt.write('\n')

    for header in headers_free:
        f_free_txt.write(str(header) + '\t')
    f_free_txt.write('\n')

    result=''
    for root, subdirs, files in os.walk(dir):
        for filename in sorted(files):
            if "tangram" in argv and "tangram" in filename:
                print(filename)
                result = process_tangram_csv.analyze_result(filename, root)
                for data in result:
                    f_tangram_txt.write(str(data) + '\t')
                f_tangram_txt.write('\n')
            elif "mindset" in argv and "mindset" in filename:
                print(filename)
                result = process_mindset_csv.analyze_result(filename, root)
                for data in result:
                    f_mindset_txt.write(str(data) + '\t')
                f_mindset_txt.write('\n')
            elif "spatial" in argv and "spatial" in filename:
                print(filename)
                result = process_spatial_csv.analyze_result(filename, root)
                for data in result:
                    f_spatial_txt.write(str(data) + '\t')
                f_spatial_txt.write('\n')
            elif "free" in argv and "free" in filename:
                print(filename)
                result = process_free_csv.analyze_result(filename, root)
                for data in result:
                    f_free_txt.write(str(data) + '\t')
                f_free_txt.write('\n')

if __name__ == "__main__":
    argv = sys.argv[1:]
    main(argv)
