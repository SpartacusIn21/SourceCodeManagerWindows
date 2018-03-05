import sys
#example
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
print("Please inpute [Xmin,Xmax](like \"[0,0]\"):")
X = input()
print("Please inpute [Ymin,Ymax](like \"[1,1]\"):")
Y = input()
nPoints = 0
for nIndex in range(len(Input)):
	if Input[nIndex][0] >= X[0] and Input[nIndex][0] <= X[1] and Input[nIndex][1] >= Y[0] and Input[nIndex][1] <= Y[1]:
		nPoints += 1
print("The number of points inclued in the rectangel [Xmin,Xmax]x[Ymin,Ymax] is:%d"%nPoints)
