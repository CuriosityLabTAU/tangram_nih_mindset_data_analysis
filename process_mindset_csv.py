import ast
import datetime
import os

# returns a list with [child selection, game result, number of moves, total time of game, child_selection,...]

def get_headers():
    headers = []
    headers.append("subject_id")
    for game in ['pre','post']:
        for i in range(0, 10):
            headers.append(game+'_selection_'+str(i))
            headers.append(game + '_result_' + str(i))
            headers.append(game + '_time_' + str(i))
    return headers

def analyze_result(filename, pathname='./processed_data/'):
    b_start = False
    result_list = []
    data =  {'pre': {}, 'post': {}}
    current_game = 'pre'

    #init an empty dictionary:
    for game in ["pre","post"]:
        for x in range (0,10):
            data[game]['selection'+str(x)]='Null'
            data[game]['result'+str(x)]='Null'
            data[game]['time' + str(x)] = 'Null'

    with open(os.path.join(pathname,filename), 'r') as fp:
        i=0
        for line in fp:

            raw_dic = ast.literal_eval(line[6:])
            action = raw_dic['action']
            obj = raw_dic['obj']

            if (b_start == False):
                start_time = datetime.datetime.strptime(raw_dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                b_start = True
            if (action == 'down'):
                index = str(obj[0])
                end_time = datetime.datetime.strptime(raw_dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                total_time = (end_time - start_time).total_seconds()
                if (total_time>300):  #indicating switch to post
                    current_game = 'post'
                start_time = end_time

                data[current_game]['selection'+index] = obj
                data[current_game]['result'+index] = obj[4]
                data[current_game]['time' + index] = total_time
                i = i + 1

    #generate result_list from data dictionary:
    subject_id = filename.replace('bag_mindset_test','')
    subject_id = subject_id.replace('.txt','')
    result_list.append(subject_id)

    for game in ["pre","post"]:
        for x in range (0,10):
            result_list.append (data[game]['selection'+str(x)])
            result_list.append (data[game]['result'+str(x)])
            result_list.append(data[game]['time' + str(x)])
    return result_list

#result = analyze_result('bag_mindset_test31.txt', pathname='./processed_data/txt/')
#print result
