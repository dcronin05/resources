#!/usr/bin/env python3

import random

filename = str('final-scores.' + str(random.randint(1, 99999999)))


def average_score(scores):

    def score_file():
        scorefile = open(filename, 'a')
        scorefile.write(scores[1][0:-6] + ': ' + str(grade) + '\n')
        scorefile.close()

    if len(scores[0]) >= 2:
        total_score = 0
        for testVar in range(len(scores[0])):
            total_score = total_score + float(scores[0][testVar])
            print(total_score)
        grade = float(total_score) / 13
        file = open(scores[1], 'a')
        file.write('\nTotal score = ' + str(total_score) + '\nAverage = ' + str(grade))
        file.close()
        score_file()
        return str('\nTotal score = ' + str(total_score) + '\nAverage = ' + str(grade))
    else:
        # file = open(scores[1], 'a')
        # file.write('\nAverage = ' + str(scores[0]))
        # file.close()
        return str('File Created.')

    # return total_score


def input_score():
    score_list = []
    file_name = str(input('Name: ') + '.score')
    score_file = open(file_name, 'w')
    score_file.write(file_name[0:-6] + ':\n\n')
    current_score = input('Enter current average (\'enter\' for new score): ')

    if len(current_score) == 0:
        i = 1
        while i <= 13:
            score = input('Score: ')
            score_list.append(score)
            i += 1

        for i in range(len(score_list)):
            score_file.write(str(score_list[i]) + '\n')
        score_file.close()
    else:
        score_list = [current_score]
        score_file.write('Average = ' + str(score_list[0]) + '\n')
        score_file.close()
        scorefile = open(filename, 'a')
        scorefile.write(file_name[0:-6] + ': ' + current_score + '\n')
        scorefile.close()

    return (score_list,file_name)


# result = 0

# total_score = total_score / 13

while input("Press any key for new score, 'q' to quit: ") != str('q'):

    print(average_score(input_score()))
    print('')