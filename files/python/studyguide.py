def openFile():
    file = open("document.txt", 'r', encoding='utf-8')
    return file


# try:
studyGuide = openFile()
fileLines = [studyGuide.readline()]

for line in studyGuide.readlines():
    fileLines.append(line)
    if len(fileLines[-1]) == 0 or fileLines[-1] == "\n" or fileLines[-1] == " \n":
        # print(fileLines)
        fileLines.pop()

print(fileLines)
file = open("newDocument.txt", 'w', encoding='utf-8')
file.writelines(fileLines)
# for line in fileLines:
#     print(type(line))
#     file = open("newDocument.txt", 'w')
#     file.write(line)
#     file.close()
#     print(line)

studyGuide.close()
# except:
#     print('ERROR:')
#     studyGuide.close()