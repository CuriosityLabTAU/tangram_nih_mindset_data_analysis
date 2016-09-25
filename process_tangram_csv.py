import ast
import datetime

child_play_flag = False
number_of_moves = 0
game_result = 0 # 0 for failure, 1 for success

result_list = []

filename = 'bag_tangram_17.txt'
with open('./processed_data/' + filename, 'r') as fp:
    for line in fp:
        dic = ast.literal_eval(line[6:])
        if len(dic['comment'])>0:
            if dic['comment'][0] == 'select_treasure':
                #print dic['comment']
                print dic['comment'][1][0]
            if dic['comment'][0] == 'not_solved':
                # print dic['comment']
                print dic['comment'][0]
                if child_play_flag is True:
                    number_of_moves = number_of_moves + 1
            if dic['comment'][0] == 'child_win':
                print dic['comment'][0] + ' ' + dic['time']
                end_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                total_time = end_time - start_time
                print 'total time: '
                print total_time
                result_list.append(1) # child win
                result_list.append(number_of_moves)
                result_list.append(total_time.total_seconds())
                child_play_flag = False
                number_of_moves = 0
            if dic['comment'][0] == 'finish':
                print dic['comment'][0] + ' ' + dic['time']
                if child_play_flag is True:
                    end_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    total_time = end_time - start_time
                    result_list.append(0)  # child lose
                    result_list.append(number_of_moves)
                    result_list.append(total_time.total_seconds())
                    child_play_flag = False
                    number_of_moves = 0
            if dic['comment'][0] == 'generate_selection':
                print dic['comment'][0]
            if dic['comment'][0] == 'press_treasure':
                if dic['comment'][3][0] == 'child_selection' and dic['comment'][2] == 'robot':
                    print 'child_selected ' + str(dic['comment'][1][0]) + ' ' + dic['time']
                    child_play_flag = True
                    start_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    result_list.append(dic['comment'][1][0])

print result_list
        # if dic['comment'][0]=='select_treasure':
        #     print dic['comment'][1][0]
        #if 'select_treasure' in line:
        #    print line
        #else:
            # print 'bla'