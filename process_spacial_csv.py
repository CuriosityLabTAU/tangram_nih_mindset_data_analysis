import ast
import datetime

# returns a list with [child selection, game result, number of moves, total time of game, child_selection,...]

def analyze_spacial_skills (filename, pathname='./processed_data/'):

    titles_sequence = ["pre_1","pre_2","pre_3","pre_4","pre_5","pre_6","pre_7","pre_8","pre_9","pre_10","pre_11","pre_12","pre_13","pre_14","pre_15","pre_16","post_1","post_2","post_3","post_4","post_5","post_6","post_7","post_8","post_9","post_10","post_11","post_12","post_13","post_14","post_15","post_16"]
    correct_sequence = ["1_A","3_B","5_C","7_A","9_D","11_A","13_B","15_A","17_B","19_B","2!_C","23_D","25_D","27_D","29_B","31_C","2_D","4_C","6_D","8_A","10_C","12_D","14_C","16_C","18_A","20_D","22_A","24_B","26_C","28_B","30_A","32_B"]
   # post_correct_sequence = ["2_D","4_C","6_D","8_A","10_C","12_D","14_C","16_C","18_A","20_D","22_A","24_B","26_C","28_B","30_A","32_B"]
    result_list = []

    with open(pathname + filename, 'r') as fp:
        i=0
        for line in fp:
            raw_dic = ast.literal_eval(line[6:])
            action = raw_dic['action']
            comment = raw_dic['comment']
            obj = raw_dic['obj']
            time = raw_dic['time']
            if (action == 'down'):
                result_list.append(obj)
                if (obj == correct_sequence[i]):
                    result_list.append(1)
                else:
                    result_list.append(0)
                i = i + 1

    return result_list

result = analyze_spacial_skills('bag_spatial_test31.bag.txt', pathname='./processed_data/')
print result