import ast
import datetime
import os

# returns a list with [child selection, game result, number of moves, total time of game, child_selection,...]

def analyze_result(filename, pathname='./processed_data/'):
    b_start = False
    #titles_sequence = ["selection_pre1","result_pre1","time_pre1",...]

    correct_sequence = ["1_A","3_B","5_C","7_A","9_D","11_A","13_B","15_A","17_B","19_B","2!_C","23_D","25_D","27_D","29_B","31_C","2_D","4_C","6_D","8_A","10_C","12_D","14_C","16_C","18_A","20_D","22_A","24_B","26_C","28_B","30_A","32_B"]
   # post_correct_sequence = ["2_D","4_C","6_D","8_A","10_C","12_D","14_C","16_C","18_A","20_D","22_A","24_B","26_C","28_B","30_A","32_B"]
    result_list = []
    data =  {'pre': {}, 'post': {}}
    current_game = 'pre'

    with open(os.path.join(pathname,filename), 'r') as fp:
        i=0
        for line in fp:

            raw_dic = ast.literal_eval(line[6:])
            action = raw_dic['action']
            comment = raw_dic['comment']
            obj = raw_dic['obj']

            if (b_start == False):
                start_time = datetime.datetime.strptime(raw_dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                b_start = True
            if (action == 'down'):
                index = str(obj[0])
                print(index)
                end_time = datetime.datetime.strptime(raw_dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                total_time = (end_time - start_time).total_seconds()
                if (total_time>300):  #indicating switch to post
                    current_game = 'post'
                print(total_time)
                start_time = end_time

                data[current_game]['selection'+index] = obj
                data[current_game]['time'+index] = total_time
                data[current_game]['result'+index] = obj[4]
                i = i + 1

    #generate result_list from data dictionary:
    for game in ["pre","post"]:
        for x in range (0,10):
            result_list.append (data[game]['selection'+str(x)])
            result_list.append (data[game]['time'+str(x)])
            result_list.append (data[game]['result'+str(x)])
    return result_list

result = analyze_result('bag_mindset_p031.txt', pathname='./processed_data/')
print result
