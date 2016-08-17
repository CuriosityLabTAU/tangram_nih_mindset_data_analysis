import rosbag
import json

#bag = rosbag.Bag('data/comsar_openday_humanoid_2016-02-04-22-00-40.bag')


#for topic, msg, t in bag.read_messages(topics=['chatter', 'numbers']):
print ("rinat")


nBag = 17
bag = rosbag.Bag('bags/nih_pilot_mindset_subject_id_test'+str(nBag)+'.bag')
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
json_list = []

#f=open('topics-log.txt','w')
f_spatial = open('processed_data/bag_SpatialSkillAssessmentApp_'+str(nBag)+'.txt','w')
f_free = open('processed_data/bag_FreeExplorationApp_'+str(nBag)+'.txt','w')
f_tangram = open('processed_data/bag_TangramMindsetApp_'+str(nBag)+'.txt','w')

for topic, msg, t in bag.read_messages(topics=['/log','/tega']): #'/log','/tega_state','/tega'
	#print msg.data
	if ('SpatialSkillAssessmentApp' in str(msg)):
		currentApp = 'SpatialSkillAssessmentApp'
	elif ('FreeExplorationApp' in str(msg)):
		currentApp = 'FreeExplorationApp'
	elif ('TangramMindsetApp' in str(msg)):
		currentApp = 'TangramMindsetApp'
	if (currentApp == 'SpatialSkillAssessmentApp'):
		f_spatial.write(str(msg)+'\n')
	elif (currentApp == 'FreeExplorationApp'):
		f_free.write(str(msg)+'\n')
	elif (currentApp == 'TangramMindsetApp'):
		f_tangram.write(str(msg)+'\n')

	#print(str(msg))
	#data_json = json.loads(str(msg))
	#print(data_json)
	#f.write(str(msg) + "\n")
	#print topic
        #print msg.points(0)
	#print msg,t

	#json_str = json.dumps (msg)
	#print value of msg.post.position.x (for example):
	#print "THE VALUE OF msg.pose.position.x is: {}".format(msg.pose.position.x)
        #print "THE VALUE OF msg.pose.position.y is: {}".format(msg.pose.position.y)
bag.close()
f_spatial.close()
f_free.close()
f_tangram.close()
