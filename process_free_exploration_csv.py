# usage:
#   results = analyze_free_exploration(filename='bag_free_17.txt')
#
# returns a dictionary, results:
# results = {
#     'pre': {                    # in the pre-app
#         't0': 0,                # time from start of app to first child action
#         'total_duration': 0,    # total duration of audio played
#         'multi_entropy': 0      # entropy of character selection
#     },
#     'post': {                   # in the post-app
#         't0': 0,
#         'total_duration': 0,
#         'multi_entropy': 0
#     }
# }

import ast
from datetime import datetime
import numpy as np


def analyze_free_exploration(filename, pathname='./processed_data/'):
    data = {'pre': {}, 'post': {}}

    with open(pathname + filename, 'r') as fp:
        for line in fp:
            dic = ast.literal_eval(line[6:])
            if len(dic['comment'])>0:
                if dic['obj'] == 'start_button_pre':
                    current_game = 'pre'
                    data['pre']['start'] = datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                if dic['obj'] == 'start_button_post':
                    current_game = 'post'
                    data['post']['start'] = datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')

                if dic['action'] == 'play':
                    try:
                        data[current_game]['sequence'].append(dic['obj'])
                    except:
                        data[current_game]['sequence'] = [dic['obj']]
                    try:
                        data[current_game][dic['comment']]['start'] =\
                            datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    except:
                        data[current_game][dic['comment']] = {
                            'start': datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')}
                elif dic['action'] == 'stop':
                    try:
                        data[current_game][dic['comment']]['stop'] =\
                            datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')
                    except:
                        data[current_game][dic['comment']] = {
                            'stop': datetime.strptime(dic['time'], '%Y_%m_%d_%H_%M_%S_%f')}

    for p in data['pre'].values():
        try:
            p['duration'] = p['stop'] - p['start']
        except:
            pass
    for p in data['post'].values():
        try:
            p['duration'] = p['stop'] - p['start']
        except:
            pass

    # calculating results:
    results = {
        'pre': {  # in the pre-app
            't0': 0,  # time from start of app to first child action
            'total_duration': 0,  # total duration of audio played
            'multi_entropy': 0  # entropy of character selection
        },
        'post': {  # in the post-app
            't0': 0,
            'total_duration': 0,
            'multi_entropy': 0
        }
    }

    # calculate t0: time from start to first character movement

    pre_first_t0 = None
    post_first_t0 = None
    for p in data['pre'].values():
        try:
            if pre_first_t0 is None:
                pre_first_t0 = p['start']
            else:
                pre_first_t0 = min([pre_first_t0, p['start']])
        except:
            pass
    for p in data['post'].values():
        try:
            if post_first_t0 is None:
                post_first_t0 = p['start']
            else:
                post_first_t0 = min([post_first_t0, p['start']])
        except:
            pass

    results['pre']['t0'] = (pre_first_t0 - data['pre']['start']).total_seconds()
    results['post']['t0'] = (post_first_t0 - data['post']['start']).total_seconds()

    # calculate total_duration: total time that had playing sound
    for p in data['pre'].values():
        try:
            results['pre']['total_duration'] += p['duration'].total_seconds()
        except:
            pass
    for p in data['post'].values():
        try:
            results['post']['total_duration'] += p['duration'].total_seconds()
        except:
            pass

    # calculate multi_entropy: the entropy of the different characters

    results['pre']['multi_entropy'] = sequence_entropy(data['pre']['sequence'])
    results['post']['multi_entropy'] = sequence_entropy(data['post']['sequence'])
    print(results)
    return results


def sequence_entropy(sequence):
    characters = list(set(sequence))
    num_characters = len(characters)
    sequence_length = len(sequence)
    prob = np.zeros([num_characters])
    for c in sequence:
        prob[characters.index(c)] += 1.0 / float(sequence_length)
    entropy = 0.0
    for p in prob:
        entropy -= p * np.log2(p)
    return entropy


results = analyze_free_exploration(filename='bag_free_17.txt')