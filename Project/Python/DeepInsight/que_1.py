import numpy as np
import math
import sys
import os


MAX = 1e5

#declare an input array and intermediate result array
ar = [[MAX,MAX]]*50
br = [[MAX,MAX]]*50
sys.setrecursionlimit(1500)

#calculate Euclidean distance
def Cal_Dis(point1,point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def Find_Smallest_Len(nStart,nEnd):
    #print("nStart %d,nEnd:%d"%(nStart,nEnd))
    if nStart == nEnd:
        return MAX
    nMid = int((nStart + nEnd) / 2)
    #print("nMid %d"%nMid)
    #use "divide and conquer" idea
    Dis = min(Find_Smallest_Len(nStart, nMid),Find_Smallest_Len(nMid+1, nEnd))
    nTail = 0
    #get left points around mid within "Dis"
    nIndex = nMid
    while nIndex >= nStart:
        if ar[nMid][0] - ar[nIndex][0] < Dis:
            br[nTail] = ar[nIndex]
            nTail += 1
        nIndex -= 1
    #get right points around mid within "Dis"
    nIndex = nMid + 1 
    while nIndex < nEnd:
        if ar[nIndex][0] - ar[nMid][0] < Dis:
            br[nTail] = ar[nIndex]
            nTail += 1
        nIndex += 1
    #sorted by y coordinate
    #print(br)
    br[0:nTail] = sorted(br[0:nTail],key=lambda x:x[1])
    for nIndex in (0,1,nTail):
        nj = nIndex + 1
        while nj < nTail:
            if br[nj][1] - br[nIndex][1] < Dis:
                Dis1 = Cal_Dis(br[nIndex],br[nj])
                if Dis > Dis1:
                    Dis = min(Dis,Dis1) 
            nj += 1
    return Dis


#main
print("Please input points set txt file name:(like \"data.txt\")")
fileName = raw_input()
file = open(fileName)
lines = file.readlines()
Input=[]
for line in lines:
	temp = line.replace('\n','').split(',')
	Input.append([float(temp[0]),float(temp[1])])
print(Input)
ar[0:len(Input)] = sorted(Input,key=lambda x:x[0]) 
#print(ar)
n = len(Input)
Dis = Find_Smallest_Len(0,n)
print("Smallest Distance:")
print(Dis)
