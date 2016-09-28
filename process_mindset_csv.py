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

    with open(os.path.join(pathname,filename), 'r') as fp:
        i=0
        for line in fp:
            raw_dic = ast.literal_eval(line[6:])
            action = raw_dic['action']
            comment = raw_dic['comment']
            obj = raw_dic['obj']
            time = raw_dic['time']

            if (b_start == False):
                start_time = datetime.datetime.strptime(raw_dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                b_start = True
            if (action == 'down'):
                end_time = datetime.datetime.strptime(raw_dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                total_time = end_time - start_time
                start_time = end_time
                result_list.append(obj)
                if (obj == correct_sequence[i]):
                    result_list.append(1)
                else:
                    result_list.append(0)
                i = i + 1
                result_list.append(total_time.total_seconds())
    return result_list

result = analyze_result('bag_mindset_test31.bag.txt', pathname='./processed_data/')
print result
