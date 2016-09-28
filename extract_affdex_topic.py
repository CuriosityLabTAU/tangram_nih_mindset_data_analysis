import os
from subprocess import call
from subprocess import Popen
from subprocess import check_output
import glob
import time


def run_rosbag_play(bag_file):
    
    txt_file = bag_file.rstrip("bag")+"txt"

    #cmd = "echo \"%s\" >> affdex.txt"%(bag_file+'\n')
    #print cmd

    #os.system(cmd)

    log = open(txt_file, 'w')
    log.flush()
    
    rosbag = Popen(["rosbag","play","-i",bag_file])

    rostopic = Popen(['rostopic', 'echo', '-p', '/robot_affdex'], stdout=log)

    time.sleep(15)
    
    rosbag.terminate()
    rostopic.terminate()


#run_rosbag_play("nih_pilot_mindset_p039_2016-09-17-13-00-58.bag")


dir = "./"
files = glob.glob(dir+"/*.bag")

for filename in files:
    run_rosbag_play(filename)



