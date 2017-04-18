/*
FileName: MovingWay
Create Time:   2015/09/16
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference: 
Description: （1）华为机考题，大意是输入一个n*n的矩形char字符，其中'B'表示起点，'H'表示终点，'-'表示该路可通,'#'表示该路不通，对于输入的矩形字符判断从'B'到'H'是否存在路径;
			 （2）两点之间路径是否存在;
*/

/*
示例:
1.比如输入 B###
		   #---
		   ---#
		   H---
则从B到H之间不通，输出'N'

2.比如输入 B-
		   -H
则从B到H之间通，输出'Y'
*/
#include<iostream>
#include<map>
using namespace std;
int R=0, C=0;
int endx,endy;
bool HaveRoad(char Map_Temp[400][400], int startx,int starty)//往Map_Temp相应位置写'r'表示已经读取过该位置
{
	if(startx < 0 || startx >= R || starty < 0 || starty >= C)//当超出界限时返回false
	{
		return false;
	}
	else if( startx == endx && starty == endy)//表示找到相应的路径，返回true
	{
		return true;
	}
	else if((Map_Temp[startx+1][starty] == '-' || Map_Temp[startx+1][starty] == 'H') && Map_Temp[startx+1][starty] != 'r')//下一个为'-'或者'H'表示该路可走，但是不能等于'r'，等于'r'表示该路径已经走过了，再走就会死循环
	{
		Map_Temp[startx+1][starty] = 'r';
		return HaveRoad(Map_Temp, startx+1, starty);
	}	
	else if((Map_Temp[startx][starty+1] == '-' || Map_Temp[startx][starty+1] == 'H') && Map_Temp[startx][starty+1] != 'r')
	{
		Map_Temp[startx][starty+1] = 'r';
		return HaveRoad(Map_Temp, startx, starty+1);
	}
	else if((Map_Temp[startx-1][starty] == '-' || Map_Temp[startx-1][starty] == 'H') && Map_Temp[startx-1][starty] != 'r')
	{
		Map_Temp[startx-1][starty] = 'r';
		return HaveRoad(Map_Temp, startx-1, starty);
	}
	else if((Map_Temp[startx][starty-1] == '-' || Map_Temp[startx][starty-1] == 'H') && Map_Temp[startx][starty-1] != 'r')
	{
		Map_Temp[startx][starty-1] = 'r';
		return HaveRoad(Map_Temp, startx, starty-1);
	}
	else
	{
		return false;
	}
}
int main()
{ 	
	
	int i,j;
	char Map_Temp[400][400] = {0};
	int startx,starty;
	cin >> R;
	cin >> C;
	for(i = 0; i < R; i++)
	{
		cin >> Map_Temp[i];
	}
	//find B and H
	for(i = 0; i < R; i++)
		for(j = 0; j < C; j++)
		{
		
			if(Map_Temp[i][j] == 'B')
			{
				startx = i;
				starty = j;
			}
			else if(Map_Temp[i][j] == 'H')
			{
				endx = i;
				endy = j;	
			}
		}
	bool result = HaveRoad(Map_Temp, startx, starty);
	if(result)
		cout << "Y" << endl;
	else
		cout << "N" << endl;
	return 0;
}