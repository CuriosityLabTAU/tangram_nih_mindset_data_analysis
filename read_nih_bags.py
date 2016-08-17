import rosbag
import json


def convert_bag2txt (nBag, topics_list):
	# creates txt files for each bag by app
	# bag_free  -> FreeExplorationApp
	# bag_spatial -> SpatialSkillAssessmentApp
	# bag_tangram -> TangramMindsetApp
	# bag_mindset -> mindset_assessment_app

	currentApp=""

	bag = rosbag.Bag('bags/nih_pilot_mindset_subject_id_test' + str(nBag) + '.bag')
	topics = bag.get_type_and_topic_info()[1].keys()  # ['/tega_state', '/tega', '/rosout', '/rosout_agg', '/log']
	print(nBag,topics)  # just nice know

	f_spatial = open('processed_data/bag_spatial_'+str(nBag)+'.txt','w')
	f_free = open('processed_data/bag_free_'+str(nBag)+'.txt','w')
	f_mindset = open('processed_data/bag_mindset_'+str(nBag)+'.txt','w')
	f_tangram = open('processed_data/bag_tangram_'+str(nBag)+'.txt','w')
	f_unknown = open('processed_data/bag_unknown_'+str(nBag)+'.txt','w')

	for topic, msg, t in bag.read_messages(topics=topics_list):
		# detect what is the current app:
		if ('SpatialSkillAssessmentApp' in str(msg)):
			currentApp = 'SpatialSkillAssessmentApp'
		elif ('FreeExplorationApp' in str(msg)):
			currentApp = 'FreeExplorationApp'
		elif ('TangramMindsetApp' in str(msg)):
			currentApp = 'TangramMindsetApp'
		elif ('mindset_assessment_app' in str(msg)):
			currentApp = 'mindset_assessment_app'

		# write msg to the current app txt file:
		if (currentApp == 'SpatialSkillAssessmentApp'):
			f_spatial.write(str(msg)+'\n')
		elif (currentApp == 'FreeExplorationApp'):
			f_free.write(str(msg)+'\n')
		elif (currentApp == 'mindset_assessment_app'):
			f_mindset.write(str(msg) + '\n')
		elif (currentApp == 'TangramMindsetApp'):
			f_tangram.write(str(msg)+'\n')
		else:
			f_unknown.write(str(msg) + '\n')
	bag.close()
	f_spatial.close()
	f_free.close()
	f_tangram.close()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
# convert bag files
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

convert_bag2txt (nBag=14, topics_list=['/log','/tega'])
convert_bag2txt (nBag=15, topics_list=['/log','/tega'])
convert_bag2txt (nBag=17, topics_list=['/log','/tega'])
convert_bag2txt (nBag=18, topics_list=['/log','/tega'])
