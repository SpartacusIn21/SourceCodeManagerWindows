/*
FileName: BinaryTree.cpp
Create Time:   2015/09/26
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference:  http://acm.acmcoder.com/showproblem.php?pid=2000
Description:
*/

/*
Problem Description
输入三个字符后，按各字符的ASCII码从小到大的顺序输出这三个字符。
Input
输入数据有多组，每组占一行，有三个字符组成，之间无空格。
Output
对于每组输入数据，输出一行，字符中间用一个空格分开。
Sample Input
qwe
asd
zxc
Sample Output
e q w
a d s
c x z
*/
#include<iostream>
#include<cmath>
#include <iomanip>
using namespace std;
int SortInputString()
{
	char Str[1000][3] = {0};
	int count = 0;
	while(cin>>Str[count])
	{
		for(int i = 0; i < 3; i++)
			for(int j = 1; j < 3-i; j++) 
			{
				if(Str[count][j] < Str[count][j-1])
				{
					Str[count][j] = Str[count][j] ^ Str[count][j-1];
					Str[count][j-1] = Str[count][j] ^ Str[count][j-1];
					Str[count][j] = Str[count][j] ^ Str[count][j-1];
				}
			}
		count++;
	}
	for(int i = 0; i < count; i++)
	{
		cout << Str[i][0] << " " << Str[i][1] << " " << Str[i][2] << endl;
	}
	return 0;
}