#!/usr/bin/python
# -*- coding: utf-8 -*-
import rosbag
import datetime         
import sys, os, errno
import json, operator
from collections import OrderedDict



target= ['/log','/jibo','/to_twisted','/from_twisted']

def main(argv):
    data_path = argv[0]
    # Output Directory
    processed_path = argv[1]

    try:
        os.makedirs(processed_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    for root, subdirs, files in os.walk(data_path):

        if "Session" not in root:
            continue
        if "archive" in root:
            continue
    
        for bag_file in files:
            if bag_file.endswith('.bag'):

                #print bag_file
                try:
                    print os.path.join(root,bag_file)
                    bag = rosbag.Bag(os.path.join(root,bag_file))
                    csv_filename = "-".join(bag_file.replace(".bag","").split("-")[:3])+"_RAW.csv"
                    
                    with open(os.path.join(processed_path,csv_filename), 'a') as csv_file:
        
                        for topic, msg, t in bag.read_messages(topics=target):
                            if topic == '/jibo':
                                csv_file.write(topic + ',' + str(t) + ',' + msg.tts_text + '\n')
                            else:
                                csv_file.write(topic + ',' + str(t) + ',' + msg.data + '\n')
                except Exception as e:
                    print
                    print e.message, e.args

            if bag_file.endswith('.log'):
                #try:
                if True:
                    print os.path.join(root,bag_file)
                    csv_filename = "-".join(bag_file.replace(".log","").split("-")[:3])+"_RAW.csv"
                    
                    with open(os.path.join(root,bag_file), 'r') as log_file, open(os.path.join(processed_path,csv_filename), 'a') as csv_file:

                        data = json.load(log_file)
                        data = sorted(data.items(), key=lambda x:x[0])
                        #data = json.load(log_file, object_pairs_hook=OrderedDict)

                        for t, log in data:
                            log = log.replace('\\"','\'')
                            log = json.dumps(json.loads(log)["log"])
                            csv_file.write('/log' + ',' + t + ',' + log + '\n')
                #except Exception as e:
                #    print
                #    print e.message, e.args


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1:])
    else:
        print "Usage: ./bag_to_csv.py <input-bag-dir> <output-csv-dir>"
        exit()
