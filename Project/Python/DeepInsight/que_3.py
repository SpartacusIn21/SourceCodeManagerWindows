import numpy as np
import math
import sys

MAX = 1e10
INIFI_POINT = [MAX,MAX]
r = 0
iPoint = [0]*50
jPoint = [0]*50
#calculate Euclidean distance
def Cal_Dis(point1,point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def IsReachable(ReachablePoints,LeftPoints):
    print(ReachablePoints)
    print(LeftPoints)
    if len(ReachablePoints) == 0:
        return 0 
    for point in ReachablePoints:
        if Cal_Dis(point,jPoint) < r:
            return 1
    temp = ReachablePoints
    ReachablePoints = []
	#delIndex = []
    for i in range(len(temp)):
        for j in range(len(LeftPoints)):
            print("i,j=%d,%d"%(i,j))
            if LeftPoints[j] != INIFI_POINT and Cal_Dis(temp[i],LeftPoints[j]) < r:
                if LeftPoints[j] == jPoint:
                    return 1
                else:
                    ReachablePoints.append(LeftPoints[j])
                    LeftPoints[j] = INIFI_POINT
                    #delIndex.append(j)
    temp1 = []
    for left in LeftPoints:
        if left != INIFI_POINT:
            temp1.append(left)
    LeftPoints = temp1

    return IsReachable(ReachablePoints, LeftPoints)

#main
print("Please input points set txt file name(like \"data.txt\"):")
fileName = ""
if sys.version > '3':
    fileName = input()
else:
    fileName = raw_input()
file = open(fileName)
lines = file.readlines()
Input=[]
for line in lines:
	temp = line.replace('\n','').split(',')
	Input.append([float(temp[0]),float(temp[1])])
print(Input)
print("Please input r:")
if sys.version > '3':
    r = float(input())
else:
    r = input()
print ("Please input i(like \"[0,0\"):")
if sys.version > '3':
    temp = input()
    temp = temp.replace("[","").replace("]","").split(",")
    iPoint = [float(temp[0]),float(temp[1])]
else:
    iPoint = input()
print ("Please input j(like \"[1,1]\"):")
if sys.version > '3':
    temp = input()
    temp = temp.replace("[","").replace("]","").split(",")
    jPoint = [float(temp[0]),float(temp[1])]
else:
    jPoint = input()
Input.append(jPoint)
bReachable = IsReachable([iPoint], Input)
if bReachable == 1:
	print("(%d,%d) has at least  a path to (%d,%d)!"%(iPoint[0],iPoint[1],jPoint[0],jPoint[1]))
else:
	print("ops, no path was found!")
