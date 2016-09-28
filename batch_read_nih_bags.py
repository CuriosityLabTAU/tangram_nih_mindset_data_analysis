import rosbag
import json
import datetime

import glob
import re, time


def convert_bag2txt (filename, output_dir, topics_list):
	# creates txt files for each bag by app
	# bag_free  -> FreeExplorationApp
	# bag_spatial -> SpatialSkillAssessmentApp
	# bag_tangram -> TangramMindsetApp
	# bag_mindset -> mindset_assessment_app

	currentApp=""
		#file_info = re.split('[_]', filename)
        file_info = re.split('[_|.]',filename)  #rinat added . to seperate uid from .bag
        pID = file_info[8].lower()
        print pID

	bag = rosbag.Bag(filename)

	#topics = bag.get_type_and_topic_info()[1].keys()  # ['/tega_state', '/tega', '/rosout', '/rosout_agg', '/log', '/robot_affdex']
	#print(nBag,topics)  # just nice know

	f_spatial = open(output_dir+'/bag_spatial_'+pID+'.txt','w')
	#f_spatial_csv = open(output_dir+'gbag_spatial_'+pID+".csv", 'w+')
	#f_spatial_csv.write("action" + "," + "comment" + "," + "time" + '\n')

	f_free = open(output_dir+'/bag_free_'+pID+'.txt','w')
	f_mindset = open(output_dir+'/bag_mindset_'+pID+'.txt','w')
	f_tangram = open(output_dir+'/bag_tangram_'+pID+'.txt','w')


	for topic, msg, t in bag.read_messages(topics=topics_list):
		# detect what is the current app:

                #print(currentApp)
                #print (msg)

		date = datetime.datetime.fromtimestamp(t.secs)  # converts rospy.rostime.Time to datetime.datetime
		strDate = date.strftime('%Y-%m-%d-%H-%M-%S')

                mindset_app_keywords = ['buffy','fluffy']
                spatial_app_keywords = ["SpatialSkillAssessmentApp","_A'","_B'","_C'","_D'"]
                free_app_keywords = ["FreeExplorationApp",'babyseal','snowman1','penguin','kid4','cloud','dragon','dinosaur','rabbit','bird','princess']
                start_app_keywords = ["start_button_pre","start_button_post"]
                ignore_keywords = ["subject_id"]

                if any(x in str(msg) for x in ignore_keywords):
                    continue

                if any(x in str(msg) for x in start_app_keywords):
		    if (currentApp == 'SpatialSkillAssessmentApp'):
			f_spatial.write(str(msg)+'\n')
			#read_spatial_skill(topic,msg,strDate,f_spatial_csv)
		    elif (currentApp == 'FreeExplorationApp'):
			f_free.write(str(msg)+'\n')
                    else:
			f_mindset.write(str(msg) + '\n')
	
                else:
                    if any(x in str(msg) for x in mindset_app_keywords):
                        currentApp = 'mindset_assessment_app'
                    elif any(x in str(msg) for x in spatial_app_keywords):
		        currentApp = 'SpatialSkillAssessmentApp'
                    elif any(x in str(msg) for x in free_app_keywords):
			currentApp = 'FreeExplorationApp'
                    else:
			currentApp = 'TangramMindsetApp'

                
		    # write msg to the current app txt file:
		    if (currentApp == 'SpatialSkillAssessmentApp'):
			f_spatial.write(str(msg)+'\n')
			#read_spatial_skill(topic,msg,strDate,f_spatial_csv)
		    elif (currentApp == 'FreeExplorationApp'):
			f_free.write(str(msg)+'\n')
		    elif (currentApp == 'mindset_assessment_app'):
			f_mindset.write(str(msg) + '\n')
		    elif (currentApp == 'TangramMindsetApp'):
			f_tangram.write(str(msg)+'\n')

	
        bag.close()

	f_spatial.close()
	#f_spatial_csv.close()
	f_free.close()
	f_mindset.close()
	f_tangram.close()

def read_spatial_skill(topic,msg,strDate,f_spatial_csv):
	#print("goren",msg.data)
	raw_str = str(msg.data)
	raw_str = raw_str.replace("u'","'")
	#print("1",raw_str)
	raw_str = raw_str.replace('"','XXX')
	#print("2",raw_str)
	raw_str = raw_str.replace("'",'"')
	#print("3",raw_str)
	raw_str = raw_str.replace('XXX', "'")
	#print ("4",raw_str)
	#raw_str = raw_str.encode('utf-8')
	raw_str = raw_str.encode('ascii','ignore')

	raw_dict = json.loads(raw_str)

	action =  raw_dict['action']
	comment = raw_dict['comment']
	obj = raw_dict['obj']
	time = raw_dict['time']
	#print(action)

	#if (action=='down'):
		#comment=
		#f_spatial_csv.write(action+","+comment+","+obj+","+strDate+'\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
# convert bag files
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

dir = "../NIH_grit_pilot_rosbag/"
#dir = "./bags"
output_dir = "results/txt/"
#output_dir = "processed_data/txt/"

#convert_bag2txt('../NIH_grit_pilot_rosbag/nih_pilot_mindset_p006_2016-08-25-13-00-00.bag', output_dir, topics_list=['/log'])

files = glob.glob(dir+"/*.bag")

for filename in files:
    #convert_bag2txt (filename, topics_list=['/log','/tega'])
	convert_bag2txt(filename, output_dir, topics_list=['/log'])

