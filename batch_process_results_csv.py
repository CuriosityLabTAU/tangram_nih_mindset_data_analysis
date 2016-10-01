#!/usr/bin/python
import os, glob
import re
import sys, getopt

import process_tangram_csv
import process_spatial_csv
import process_mindset_csv
import process_free_csv
import analyze_tangram_moves


def main(argv):
    #dir = "./results/txt"
    dir = ""

    if len(argv) == 1 or '-h' in argv:
        print 'batch_process_result_csv.py <path_to_data_folder> <analysis_argv1> <analysis_argv2> ...'
        sys.exit()
    elif not os.path.isdir(argv[1]):
        print "Directory not found in '%s'" % argv[1]
        sys.exit(2)
    else:
        dir = argv[1]
        if len(argv) < 3:
            argv = ['tangram', 'mindset', 'spatial', 'free']
        else:
            argv = argv[2:]

    txt_dir = os.path.abspath(dir+'/txt')
    csv_dir = os.path.abspath(dir+'/csv')

    print "Analysis Type = ", argv

    tangram_matrix = []
    mindset_matrix = []
    spatial_matrix = []
    free_matrix =[]

    #-------------------------------------------------------------------------------
    #init txt files:
    # -------------------------------------------------------------------------------
    f_tangram_csv = open(csv_dir+'/processed_tangram.csv', 'w')
    f_tangram_grit_csv = open(csv_dir+'/processed_tangram_grit.csv', 'w')
    f_tangram_grit_inc_csv = open(csv_dir+'/processed_tangram_grit_inc.csv', 'w')
    f_spatial_csv = open(csv_dir+'/processed_spatial.csv', 'w')
    f_mindset_csv = open(csv_dir+'/processed_mindset.csv', 'w')
    f_free_csv = open(csv_dir+'/processed_free.csv', 'w')
    f_all_csv = open(csv_dir+'/processed_all.csv', 'w')

    #-------------------------------------------------------------------------------
    #set headers
    #-------------------------------------------------------------------------------
    headers_tangram = process_tangram_csv.get_headers()
    headers_mindset = process_mindset_csv.get_headers()
    headers_spatial = process_spatial_csv.get_headers()
    headers_free = process_free_csv.get_headers()


    for header in headers_mindset:
        f_mindset_csv.write(str(header) + ',')
        f_all_csv.write(str(header) + ',')
    f_mindset_csv.write('\n')

    for header in headers_spatial:
        f_spatial_csv.write(str(header) + ',')
        f_all_csv.write(str(header) + ',')
    f_spatial_csv.write('\n')

    for header in headers_free:
        f_free_csv.write(str(header) + ',')
        f_all_csv.write(str(header) + ',')
    f_free_csv.write('\n')

    for header in headers_tangram:
        f_tangram_csv.write(str(header) + ',')
        f_all_csv.write(str(header) + ',')
    f_tangram_csv.write('\n')

    f_all_csv.write('\n')

    result=''

    # -------------------------------------------------------------------------------
    # process data
    # -------------------------------------------------------------------------------
    for root, subdirs, files in os.walk(txt_dir):
        for filename in sorted(files):

            if "mindset" in argv and "mindset" in filename:
                print(filename)
                result = process_mindset_csv.analyze_result(filename, root)
                mindset_matrix.append(result)
                for data in result:
                    f_mindset_csv.write(str(data) + ',')
                f_mindset_csv.write('\n')
            elif "spatial" in argv and "spatial" in filename:
                print(filename)
                result = process_spatial_csv.analyze_result(filename, root)
                spatial_matrix.append(result)
                for data in result:
                    f_spatial_csv.write(str(data) + ',')
                f_spatial_csv.write('\n')
            elif "free" in argv and "free" in filename:
                print(filename)
                result = process_free_csv.analyze_result(filename, root)
                free_matrix.append(result)
                for data in result:
                    f_free_csv.write(str(data) + ',')
                f_free_csv.write('\n')
            elif "tangram" in argv and "tangram" in filename:
                print(filename)
                #general:
                result = process_tangram_csv.analyze_result(filename, root)
                tangram_matrix.append(result)
                for data in result:
                    f_tangram_csv.write(str(data) + ',')
                f_tangram_csv.write('\n')
                #grit:
                result,result_inc = analyze_tangram_moves.analyze_tangram_grit_moves(filename, root)
                for data in result:
                    f_tangram_grit_csv.write(str(data) + ',')
                for data in result_inc:
                    f_tangram_grit_inc_csv.write(str(data) + ',')
                f_tangram_grit_csv.write('\n')
                f_tangram_grit_inc_csv.write('\n')

    # -------------------------------------------------------------------------------
    # make one big file with all the data
    # -------------------------------------------------------------------------------

    for i in range (0,len(tangram_matrix)): #I assume that all the matrices are of the same length
        for data in mindset_matrix[i]:
            f_all_csv.write(str(data) + ',')
        for data in spatial_matrix[i]:
            f_all_csv.write(str(data) + ',')
        for data in free_matrix[i]:
            f_all_csv.write(str(data) + ',')
        for data in tangram_matrix[i]:
            f_all_csv.write(str(data) + ',')
        f_all_csv.write('\n')

if __name__ == "__main__":
    main(sys.argv)
