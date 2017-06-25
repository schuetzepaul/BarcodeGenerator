import numpy as np
import matplotlib as plt

import sys


def readCSV():
    
    arr = []
    
    i=0
    with open("code128.csv") as filein:
        for line in filein:
            subarr = []
            for el in line.split():
                subarr.append(el)
            arr.append(subarr)

    return arr

translator = readCSV()

def char2String(char):
    for i in range(0,len(translator)):
        if char == translator[i][2]:
            return translator[i][7]
    print "Could not find " + str(char) + " in the table"

def char2Code(char):
    codeStr = char2String(char)
    return string2Code(codeStr)

def char2Value(char):
    for i in range(0,len(translator)):
        if char == translator[i][2]:
            return int(translator[i][0])
    print "Could not find " + str(char) + " in the table"


def string2Code(string):
    
    arr = []

    for i,el in enumerate(string):
        arr.append(int(el))
    
    return arr

def code2Plot(code):
    codeNP = np.asarray(code)
    length = codeNP.sum()
    print "Length of code is " + str(length)
    
    dataPlot = np.zeros((length,20))
    j = 0
    black = True
    for el in code:
        for k in range(0,el):
            if black:
                dataPlot[j+k] = 1
        j += el
    
    pl = plt.imshow(dataPlot)
        
            
    

dataChars = sys.argv[1]

print "Translating " + str(dataChars) + " into barcode ..."

startStr = "211214"
startCode = string2Code(startStr)

totalCode = []
totalCode.extend(startCode)

sumVal = 104
for el in dataChars:
    code = char2Code(el)
    totalCode.extend(code)
    sumVal += char2Value(el)

print totalCode

code2Plot(totalCode)
