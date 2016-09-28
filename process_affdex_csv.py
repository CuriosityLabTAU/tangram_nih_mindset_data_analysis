import datetime
import re
import glob


def affdex_data_to_csv(filename):

    with open(filename, 'r') as affdex_file, open(filename.rstrip('txt')+'csv', 'w') as output_csv:

        affdex_file.readline()

        output_csv.write(   "time,joy,anger,disgust,contempt,engagement,fear,sadness,surprise,valence, \
                            Attention,BrowFurrow,BrowRaise,ChinRaise,EyeClosure,InnerBrowRaise,LipCornerDepressor, \
                            LipPress,LipPucker,LipSuck,MouthOpen,NoseWrinkle,Smile,Smirk,UpperLipRaise, \
                            Interocular,yaw,roll,pitch\n")

        for line in affdex_file:
            data = re.split(',',line)
            data = data[:29]

            print int(data[0])

            data[0] = datetime.datetime.fromtimestamp(int(data[0])/1000000000)
            data[0] = data[0].strftime('%Y-%m-%d-%H-%M-%S')

            data = ",".join(data)
            print data



affdex_data_to_csv("affdex_data/nih_pilot_mindset_p031_2016-09-02-10-57-46.txt")

dir = "./affdex_data"
files = glob.glob(dir+"/*.bag")

#for filename in files:
 #   affdex_data_to_csv(filename)
