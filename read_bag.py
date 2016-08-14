import rosbag
#bag = rosbag.Bag('data/comsar_openday_humanoid_2016-02-04-22-00-40.bag')
bag = rosbag.Bag('bags/nih_pilot_mindset_subject_id_test14.bag')

#for topic, msg, t in bag.read_messages(topics=['chatter', 'numbers']):
print ("rinat")


topics = bag.get_type_and_topic_info()[1].keys()
types = []
print (topics)
print(bag.get_type_and_topic_info()[1].values()[0][0])

print (len(bag.get_type_and_topic_info()[1].values()))
for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
    print(bag.get_type_and_topic_info()[1].values()[i][0])
    types.append(bag.get_type_and_topic_info()[1].values()[i][0])


#for topic, msg, t in bag.read_messages(topics=['/skeleton_markers']):
#for topic, msg, t in bag.read_messages(topics=['/log']):  
for topic, msg, t in bag.read_messages(topics=['/to_twisted']):
	#print topic
        #print msg.points(0)
	print msg
	
	#print value of msg.post.position.x (for example):
	#print "THE VALUE OF msg.pose.position.x is: {}".format(msg.pose.position.x)
        #print "THE VALUE OF msg.pose.position.y is: {}".format(msg.pose.position.y)
        print t
bag.close()
