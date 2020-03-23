from random import random

file = open("testData.txt", "w")


def addZero(aStr):
    if len(aStr) == 1:
        return '0' + aStr
    else:
        return aStr


testColorString = ''

cnt = int(input("The number of test data groups: "))
while cnt > 0:
    cnt -= 1
    r = addZero(str(hex(int(random() * 255)))[2:])
    g = addZero(str(hex(int(random() * 255)))[2:])
    b = addZero(str(hex(int(random() * 255)))[2:])
    testColorString = '#' + r + g + b
    file.write(testColorString + '\n')

file.close()
