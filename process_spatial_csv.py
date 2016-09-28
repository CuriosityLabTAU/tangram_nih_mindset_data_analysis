import ast
import datetime
import os

# returns a list with [child selection, game result, total time of game, child_selection,...]

def analyze_result(filename, pathname='./processed_data/'):

    #titles_sequence = ["selection_pre1","result_pre1","time_pre1",...]

    correct_sequence = ["1_A","3_B","5_C","7_A","9_D","11_A","13_B","15_A","17_B","19_B","2!_C","23_D","25_D","27_D","29_B","31_C","2_D","4_C","6_D","8_A","10_C","12_D","14_C","16_C","18_A","20_D","22_A","24_B","26_C","28_B","30_A","32_B"]
   # post_correct_sequence = ["2_D","4_C","6_D","8_A","10_C","12_D","14_C","16_C","18_A","20_D","22_A","24_B","26_C","28_B","30_A","32_B"]
    result_list = []

    data = {'pre': {}, 'post': {}}
    current_game = 'pre'

    # init an empty dictionary:
    for game in ["pre", "post"]:
        for x in range(0, 16):
            data[game]['selection' + str(x)] = 'Null'
            data[game]['result' + str(x)] = 'Null'
            data[game]['time' + str(x)] = 'Null'


    with open(os.path.join(pathname,filename), 'r') as fp:
        i=0
        for line in fp:
            raw_dic = ast.literal_eval(line[6:])
            action = raw_dic['action']
            comment = raw_dic['comment']
            obj = raw_dic['obj']
            time = raw_dic['time']

            if (action == 'down'):
                if (obj == 'start_button_pre'):
                    start_time = datetime.datetime.strptime(raw_dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    current_game="pre"
                elif (obj == 'start_button_post'):
                    start_time = datetime.datetime.strptime(raw_dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    current_game = "post"
                    i=0
                else:
                    end_time = datetime.datetime.strptime(raw_dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    total_time = (end_time - start_time).total_seconds()
                    start_time = end_time
                    data[current_game]['selection' + str(i)] = obj
                    if (obj == correct_sequence[i]):
                        data[current_game]['result' + str(i)] = 1
                    else:
                        data[current_game]['result' + str(i)] = 0
                    data[current_game]['time' + str(i)] = total_time
                    i = i + 1

    subject_id = filename.replace('bag_spatial_test','')
    subject_id = subject_id.replace('.txt','')
    result_list.append(subject_id)

    for game in ["pre","post"]:
        for x in range (0,16):
            result_list.append (data[game]['selection'+str(x)])
            result_list.append (data[game]['result'+str(x)])
            result_list.append(data[game]['time' + str(x)])
    return result_list

result = analyze_result('bag_spatial_test17.txt', pathname='./processed_data/txt/')
print result
