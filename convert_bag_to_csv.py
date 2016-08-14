#this code converts the data from Omer experiment from bag to csv
import rosbag
#bag = rosbag.Bag('data/comsar_openday_humanoid_2016-02-04-22-00-40.bag')
# bag = rosbag.Bag('data/comsar_openday_humanoid_2016-02-05-12-40-13.bag')

#for topic, msg, t in bag.read_messages(topics=['chatter', 'numbers']):
#
#
#
# topics = bag.get_type_and_topic_info()[1].keys()
# types = []
# print (topics)
# print(bag.get_type_and_topic_info()[1].values()[0][0])
#
# print (len(bag.get_type_and_topic_info()[1].values()))
# for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
#     print(bag.get_type_and_topic_info()[1].values()[i][0])
#     types.append(bag.get_type_and_topic_info()[1].values()[i][0])
#
#
# #for topic, msg, t in bag.read_messages(topics=['/skeleton_markers']):
# for topic, msg, t in bag.read_messages(topics=['/to_meccanoid']):
# 	#print topic
#         #print msg.points(0)
# 	print msg
#
# 	#print value of msg.post.position.x (for example):
# 	#print "THE VALUE OF msg.pose.position.x is: {}".format(msg.pose.position.x)
#         #print "THE VALUE OF msg.pose.position.y is: {}".format(msg.pose.position.y)
#         #print t

import datetime                 #needed for date conversion
import sys                      #needed for printing the error msg
from os import listdir
from os.path import isfile, join
data_path = '../data/dinoData'
processed_path = '../processed/dinoProcessed/'
onlyfiles = [join(data_path, f) for f in listdir(data_path) if isfile(join(data_path, f)) and 'active' not in f]

print(onlyfiles)
for bag_file in onlyfiles:
    try:
        bag = rosbag.Bag(bag_file)
        file_open = False
        for topic, msg, t in bag.read_messages(topics=['/skeleton_markers', '/movement_log']):
            if topic == '/movement_log':
                if msg.data == 'start episode':
                    date=datetime.datetime.fromtimestamp(t.secs)  #converts rospy.rostime.Time to datetime.datetime
                    strDate=date.strftime('%Y-%m-%d-%H-%M-%S')
                    file_kinect = open(processed_path + 'time_' + str(strDate) + '_kinect.csv', 'w+')
                    file_meccanoid = open(processed_path + 'time_' + str(strDate) + '_meccanoid.csv', 'w+')
                    file_open = True
                if msg.data == 'end episode':
                    file_kinect.close()
                    file_meccanoid.close()
                    file_open = False

            if topic == '/skeleton_markers':
                if file_open:
                    s = str(t) + ','
                    for p in msg.points:
                        s += str(p.x) + ',' + str(p.y) + ',' + str(p.z) + ','
                    s += '\n'
                    file_kinect.write(s)

            if topic == '/movement_log':
                if file_open:
                    file_meccanoid.write(str(t) + ',' + msg.data + '\n')
        print('done!')
    except:
        print('error', sys.exc_info()[0])



    bag.close()
