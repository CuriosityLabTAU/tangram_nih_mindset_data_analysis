import ast
import datetime

# returns a list with [child selection, game result, number of moves, total time of game, child_selection,...]


def analyze_tangram_game(filename, pathname='./processed_data/'):

    child_play_flag = False
    number_of_moves = 0
    game_result = 0 # 0 for failure, 1 for success

    result_list = []

    with open(pathname + filename, 'r') as fp:
        for line in fp:
            dic = ast.literal_eval(line[6:])
            if len(dic['comment'])>0:
                # if dic['comment'][0] == 'select_treasure':
                #     #print dic['comment']
                #     #print dic['comment'][1][0]
                if dic['comment'][0] == 'not_solved':
                    # print dic['comment']
                    #print dic['comment'][0]
                    if child_play_flag is True:
                        number_of_moves = number_of_moves + 1
                if dic['comment'][0] == 'child_win':
                    #print dic['comment'][0] + ' ' + dic['time']
                    end_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    total_time = end_time - start_time
                    #print 'total time: '
                    #print total_time
                    game_result = 1 # child win
                    result_list.append(game_result)
                    result_list.append(number_of_moves)
                    result_list.append(total_time.total_seconds())
                    child_play_flag = False
                    number_of_moves = 0
                if dic['comment'][0] == 'finish':
                    #print dic['comment'][0] + ' ' + dic['time']
                    if child_play_flag is True:
                        end_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                        total_time = end_time - start_time
                        game_result = 0  # child lose
                        result_list.append(game_result)
                        result_list.append(number_of_moves)
                        result_list.append(total_time.total_seconds())
                        child_play_flag = False
                        number_of_moves = 0
                # if dic['comment'][0] == 'generate_selection':
                #     print dic['comment'][0]
                if dic['comment'][0] == 'press_treasure':
                    if dic['comment'][3][0] == 'child_selection' and dic['comment'][2] == 'robot':
                        #print 'child_selected ' + str(dic['comment'][1][0]) + ' ' + dic['time']
                        child_play_flag = True
                        start_time = datetime.datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                        result_list.append(dic['comment'][1][0])

    return result_list


result = analyze_tangram_game('bag_tangram_17.txt', pathname='./processed_data/')
print result