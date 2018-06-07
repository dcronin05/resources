#!/usr/bin/python3

import sys

fileDir = r"c:\Users\dcron\OneDrive - GPantz\Personal\HTML\dcron.in\resources\files\python\.notes\""

try:
    fileName = fileDir + sys.argv[1]
except:
    print('Enter a filename and note please.')
    fileName = fileDir + input()

try:
    note = sys.argv[2]
except:
    print('Enter your note please.')
    note = input()

def write_file(name, note):
    try:
        file = open(name, 'r')
        print('File exists: ', file.readable())
    except:
        print('File doesn\'t exist, creating.')
        file = open(name, 'w')
    try:
        noteNumber = len(file.readlines())
    except:
        noteNumber = 0
    file.close()
    file = open(name, 'a')
    note = '[' + str(noteNumber + 1) + ']: ' + note + '\n'
    file.write(note)
    file.close()

write_file(fileName, note)