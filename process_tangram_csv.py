import ast
import datetime
import os

# returns a list with [who_is_playing ('R'/'C'), start_time, child selection, end_time, game result, number of moves, total time of game, who_is_playing, ...]

def get_headers():
    return ['subject_id', 'player', 'start_time', 'selection', 'end_time', 'result', '#moves', 'total_game_time(sec)', 'player', 'start_time', 'selection', 'end_time', 'result', '#moves', 'total_game_time(sec)', 'player', 'start_time', 'selection', 'end_time', 'result', '#moves', 'total_game_time(sec)', 'player', 'start_time', 'selection', 'end_time', 'result', '#moves', 'total_game_time(sec)', 'player', 'start_time', 'selection', 'end_time', 'result', '#moves', 'total_game_time(sec)', 'player', 'start_time', 'selection', 'end_time', 'result', '#moves', 'total_game_time(sec)', 'player', 'start_time', 'selection', 'end_time', 'result', '#moves', 'total_game_time(sec)', 'player', 'start_time', 'selection', 'end_time', 'result', '#moves', 'total_game_time(sec)', 'player', 'start_time', 'selection', 'end_time', 'result', '#moves', 'total_game_time(sec)', 'player', 'start_time', 'selection', 'end_time', 'result', '#moves', 'total_game_time(sec)']

def analyze_result(filename, pathname='./processed_data/'):

    who_is_playing = 'R' # can be 'R' or 'C'
    child_play_flag = False
    number_of_moves = 0
    game_result = 0 # 0 for failure, 1 for success
    first_solved_flag = False
    result_list = []
    #result_list.append(who_is_playing)

    subject_id = filename.replace('bag_tangram_test', '')
    subject_id = subject_id.replace('.txt', '')
    result_list.append(subject_id)

    with open(os.path.join(pathname,filename), 'r') as fp:
        for line in fp:
            #print line[6:]
            dic = ast.literal_eval(line[6:])
            if len(dic['comment'])>0:
                # if dic['comment'][0] == 'select_treasure':
                #     #print dic['comment']
                #     #print dic['comment'][1][0]
                if dic['comment'][0] == 'not_solved':
                    # print dic['comment']
                    #print dic['comment'][0]
                    #if child_play_flag is True:
                    number_of_moves = number_of_moves + 1
                if dic['comment'][0] == 'solved':
                    if first_solved_flag is False:
                        first_solved_flag = True
                        #print dic['comment'][0] + ' ' + dic['time']
                        end_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                        total_time = end_time - start_time
                        #print 'total time: '
                        #print total_time
                        game_result = 1 # win
                        result_list.append(end_time.strftime('%Y-%m-%d-%H-%M-%S'))
                        result_list.append(game_result)
                        result_list.append(number_of_moves)
                        result_list.append(total_time.total_seconds())
                        if who_is_playing == 'R':
                            who_is_playing = 'C'
                        else:
                            who_is_playing = 'R'
                        number_of_moves = 0
                if dic['comment'][0] == 'finish':
                    #print dic['comment'][0] + ' ' + dic['time']
                    if first_finish_flag is False:
                        first_finish_flag = True
                        end_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                        total_time = end_time - start_time
                        game_result = 0  # lose
                        result_list.append(end_time.strftime('%Y-%m-%d-%H-%M-%S'))
                        result_list.append(game_result)
                        result_list.append(number_of_moves)
                        result_list.append(total_time.total_seconds())
                        if who_is_playing == 'R':
                            who_is_playing = 'C'
                        else:
                            who_is_playing = 'R'
                        number_of_moves = 0

                # if dic['comment'][0] == 'generate_selection':
                #     print dic['comment'][0]

                if dic['comment'][0] == 'press_treasure' and dic['comment'][2]=='game':
                   # if dic['comment'][3][0] != 'child_selection' or dic['comment'][2] != 'robot':
                        #print 'child_selected ' + str(dic['comment'][1][0]) + ' ' + dic['time']
                        #child_play_flag = True
                    start_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    result_list.append(who_is_playing)
                    result_list.append(start_time.strftime('%Y-%m-%d-%H-%M-%S'))
                    result_list.append(dic['comment'][1][0])
                    first_solved_flag = False
                    first_finish_flag = False
                    # else:
                    #     child_play_flag = False
                    #     start_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    #     result_list.append(dic['comment'][1][0])
            if dic['obj']=='stop_button':
                if first_finish_flag is False:
                    first_finish_flag = True
                    end_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    total_time = end_time - start_time
                    game_result = 0  # lose
                    result_list.append(end_time.strftime('%Y-%m-%d-%H-%M-%S'))
                    result_list.append(game_result)
                    result_list.append(number_of_moves)
                    result_list.append(total_time.total_seconds())
                    if who_is_playing == 'R':
                        who_is_playing = 'C'
                    else:
                        who_is_playing = 'R'
                    number_of_moves = 0


    if len(result_list) < 71:
        for n in range(71-len(result_list)):
            result_list.append('NULL')
    return result_list

result = analyze_result('bag_tangram_test31.txt', pathname='./processed_data/txt/')
print result
#result = analyze_result('maor_test_bag.bag.txt', pathname='./processed_data/')
print len(result)

# print result

# old algorithm that output only the child results
#
# with open(pathname + filename, 'r') as fp:
#     for line in fp:
#         print line[6:]
#         dic = ast.literal_eval(line[6:])
#         if len(dic['comment']) > 0:
#             # if dic['comment'][0] == 'select_treasure':
#             #     #print dic['comment']
#             #     #print dic['comment'][1][0]
#             if dic['comment'][0] == 'not_solved':
#                 # print dic['comment']
#                 # print dic['comment'][0]
#                 if child_play_flag is True:
#                     number_of_moves = number_of_moves + 1
#             if dic['comment'][0] == 'child_win':
#                 # print dic['comment'][0] + ' ' + dic['time']
#                 end_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
#                 total_time = end_time - start_time
#                 # print 'total time: '
#                 # print total_time
#                 game_result = 1  # child win
#                 result_list.append(game_result)
#                 result_list.append(number_of_moves)
#                 result_list.append(total_time.total_seconds())
#                 child_play_flag = False
#                 number_of_moves = 0
#             if dic['comment'][0] == 'finish':
#                 # print dic['comment'][0] + ' ' + dic['time']
#                 if child_play_flag is True:
#                     end_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
#                     total_time = end_time - start_time
#                     game_result = 0  # child lose
#                     result_list.append(game_result)
#                     result_list.append(number_of_moves)
#                     result_list.append(total_time.total_seconds())
#                     child_play_flag = False
#                     number_of_moves = 0
#             # if dic['comment'][0] == 'generate_selection':
#             #     print dic['comment'][0]
#
#             if dic['comment'][0] == 'press_treasure':
#                 if dic['comment'][3][0] == 'child_selection' and dic['comment'][2] == 'robot':
#                     # print 'child_selected ' + str(dic['comment'][1][0]) + ' ' + dic['time']
#                     child_play_flag = True
#                     start_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
#                     result_list.append(dic['comment'][1][0])
#                 else:
#                     child_play_flag = False
#                     start_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
#                     result_list.append(dic['comment'][1][0])