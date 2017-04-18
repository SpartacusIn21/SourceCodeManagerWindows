/*
FileName: BinaryTree.cpp
Create Time:   2015/09/26
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference:  http://acm.acmcoder.com/showproblem.php?pid=2001 
Description:
*/

/*
Problem Description
输入两点坐标（X1,Y1）,（X2,Y2）,计算并输出两点间的距离。
Input
输入数据有多组，每组占一行，由4个实数组成，分别表示x1,y1,x2,y2,数据之间用空格隔开。
Output
对于每组输入数据，输出一行，结果保留两位小数。
Sample Input
0 0 0 1
0 1 1 0
Sample Output
1.00
1.41
*/
#include<iostream>
#include<cmath>
#include <iomanip>
using namespace std;
int TwoPointDis()
{
	double x1,y1,x2,y2;
	double Result[1000] = {0};
	int count = 0;
	while(cin>>x1>>y1>>x2>>y2)
	{
		Result[count++] = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
	}
	for(int i = 0; i < count; i++)
		cout<< fixed << setprecision(2) << Result[i] << endl;

	return 0;
}