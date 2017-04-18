/*
题1
描述
Given a circle on a two-dimentional plane.

Output the integral point in or on the boundary of the circle which has the largest distance from the center.

输入
One line with three floats which are all accurate to three decimal places, indicating the coordinates of the center x, y and the radius r.

For 80% of the data: |x|,|y|<=1000, 1<=|r|<=1000

For 100% of the data: |x|,|y|<=100000, 1<=|r|<=100000

输出
One line with two integers separated by one space, indicating the answer.

If there are multiple answers, print the one with the largest x-coordinate.

If there are still multiple answers, print the one with the largest y-coordinate.



样例输入
1.000 1.000 5.000
样例输出
6 1
/*
Soure:http://hihocoder.com/contest/msbop2015round2a/problem/1
Date:4-25-2015
Author:Yangchun, Chen
*/
/*#include<stdio.h>
#include<iostream>
#include <string>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include <math.h>
#include <algorithm>
using namespace std;


int main(void){
	
	int count = 0;//count用于统计找到的点数
	float MaxDis = 0;//用于统计满足条件的最远的距离
	float x0 = 0, y0 =0, R = 0;//x0,y0,R分别为圆心点和半径
	cin >> x0 >> y0 >> R;
	int xMax = int(x0), yMax = int(y0);

	//处理模块1
	for(int x = floor(x0-R); x <= ceil(x0); x++)//x循环
	{
		int tempY = ceil(y0+sqrt(R*R-(x-x0)*(x-x0)));
		for(int y = floor(x+y0-(x0-R)); y <= tempY; y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis)
				{
					if(x>xMax)
					{
						xMax = x;
						yMax = y;
					}
					else if(y > yMax)
					{
						xMax = x;
						yMax = y;
					}
				}
			}
		}
	}

	//处理模块2
	for(int x = floor(x0); x <= ceil(x0+R); x++)//x循环
	{
		int tempY = ceil(y0+sqrt(R*R-(x-x0)*(x-x0)));
		for(int y = floor(-x+x0+y0+R); y <= tempY; y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis)
				{
					if(x>xMax)
					{
						xMax = x;
						yMax = y;
					}
					else if(y > yMax)
					{
						xMax = x;
						yMax = y;
					}
				}
			}
		}
	}

	//处理模块3
	for(int x = floor(x0-R); x <= ceil(x0); x++)//x循环
	{
		int tempY = floor(y0-sqrt(R*R-(x-x0)*(x-x0)));
		for(int y = tempY; y <= ceil(-x+x0+y0-R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis)
				{
					if(x>xMax)
					{
						xMax = x;
						yMax = y;
					}
					else if(y > yMax)
					{
						xMax = x;
						yMax = y;
					}
				}
			}
		}
	}

	//处理模块4
	for(int x = floor(x0); x <= ceil(x0+R); x++)//x循环
	{
		int tempY = floor(y0-sqrt(R*R-(x-x0)*(x-x0)));
		for(int y = tempY; y <= ceil(x-x0+y0-R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis)
				{
					if(x>xMax)
					{
						xMax = x;
						yMax = y;
					}
					else if(y > yMax)
					{
						xMax = x;
						yMax = y;
					}
				}
			}
		}
	}
	
	cout << xMax << " " << yMax << endl;
	return 0;
}*/

/*
#include<stdio.h>
#include<iostream>
#include <string>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include <math.h>
#include <algorithm>
using namespace std;


int main(void){
	
	int count = 0;//count用于统计找到的点数
	float MaxDis = 0;//用于统计满足条件的最远的距离
	float x0 = 0, y0 =0, R = 0;//x0,y0,R分别为圆心点和半径
	cin >> x0 >> y0 >> R;
	int xMax = int(x0), yMax = int(y0);

	//处理模块1
	for(int x = floor(x0-R); x <= ceil(x0); x++)//x循环
	{
		for(int y = floor(x+y0-(x0-R)); y <= ceil(y0+R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis)
				{
					if(x>xMax)
					{
						xMax = x;
						yMax = y;
					}
					else if(y > yMax)
					{
						xMax = x;
						yMax = y;
					}
				}
			}
		}
	}

	//处理模块2
	for(int x = floor(x0); x <= ceil(x0+R); x++)//x循环
	{
		for(int y = floor(-x+x0+y0+R); y <= ceil(y0+R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis)
				{
					if(x>xMax)
					{
						xMax = x;
						yMax = y;
					}
					else if(y > yMax)
					{
						xMax = x;
						yMax = y;
					}
				}
			}
		}
	}

	//处理模块3
	for(int x = floor(x0-R); x <= ceil(x0); x++)//x循环
	{
		for(int y = floor(y0-R); y <= ceil(-x+x0+y0-R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis)
				{
					if(x>xMax)
					{
						xMax = x;
						yMax = y;
					}
					else if(y > yMax)
					{
						xMax = x;
						yMax = y;
					}
				}
			}
		}
	}

	//处理模块4
	for(int x = floor(x0); x <= ceil(x0+R); x++)//x循环
	{
		for(int y = floor(y0-R); y <= ceil(x-x0+y0-R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis)
				{
					if(x>xMax)
					{
						xMax = x;
						yMax = y;
					}
					else if(y > yMax)
					{
						xMax = x;
						yMax = y;
					}
				}
			}
		}
	}
	
	cout << xMax << " " << yMax << endl;
	return 0;
}
*/
/*
#include<stdio.h>
#include<iostream>
#include <string>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include <math.h>
#include <algorithm>
using namespace std;


int main(void){

	int count = 0;//count用于统计找到的点数
	float MaxDis = 0;//用于统计满足条件的最远的距离
	float x0 = 0, y0 =0, R = 0;//x0,y0,R分别为圆心点和半径
	cin >> x0 >> y0 >> R;
	int xMax = int(x0), yMax = int(y0);

	//处理模块1
	for(int x = floor(x0-R); x <= ceil(x0); x++)//x循环
	{
		for(int y = floor(x+y0-(x0-R)); y <= ceil(y0+R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) < R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
			}
			else if(R*R - (x-x0)*(x-x0) - (y-y0)*(y-y0) > 0.001)
			{
				if(x>xMax)
				{
					xMax = x;
					yMax = y;
				}
				else if(y > yMax)
				{
					xMax = x;
					yMax = y;
				}
			}
		}
	}

	//处理模块2
	for(int x = floor(x0); x <= ceil(x0+R); x++)//x循环
	{
		for(int y = floor(-x+x0+y0+R); y <= ceil(y0+R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) < R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
			}
			else if(R*R - (x-x0)*(x-x0) - (y-y0)*(y-y0) > 0.001)
			{
				if(x>xMax)
				{
					xMax = x;
					yMax = y;
				}
				else if(y > yMax)
				{
					xMax = x;
					yMax = y;
				}
			}
		}
	}

	//处理模块3
	for(int x = floor(x0-R); x <= ceil(x0); x++)//x循环
	{
		for(int y = floor(y0-R); y <= ceil(-x+x0+y0-R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) < R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
			}
			else if(R*R - (x-x0)*(x-x0) - (y-y0)*(y-y0) > 0.001)
			{
				if(x>xMax)
				{
					xMax = x;
					yMax = y;
				}
				else if(y > yMax)
				{
					xMax = x;
					yMax = y;
				}
			}
		}
	}

	//处理模块4
	for(int x = floor(x0); x <= ceil(x0+R); x++)//x循环
	{
		for(int y = floor(y0-R); y <= ceil(x-x0+y0-R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) < R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
			}
			else if(R*R - (x-x0)*(x-x0) - (y-y0)*(y-y0) > 0.001)
			{
				if(x>xMax)
				{
					xMax = x;
					yMax = y;
				}
				else if(y > yMax)
				{
					xMax = x;
					yMax = y;
				}
			}
		}
	}

	cout << xMax << " " << yMax << endl;
	return 0;
}
*/


#include <iostream>
#include<string>
using namespace std;

int Ques1(void){

	int count = 0;//count用于统计找到的点数
	float MaxDis = 0;//用于统计满足条件的最远的距离
	float x0 = 0, y0 =0, R = 0;//x0,y0,R分别为圆心点和半径
	int xMax = 0, yMax = 0;
	int x = 0, y =0;
	//cin >> x0 >> y0 >> R;
	scanf("%f %f %f", &x0, &y0, &R);
	
	xMax = (x0);
	yMax = (y0);

	//处理模块1
	for(x = floor(x0-R); x <= ceil(x0); x++)//x循环
	{
		for(y = floor(x+y0-(x0-R)); y <= ceil(y0+R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis  && x>xMax)
				{
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis  && y > yMax)
				{
					xMax = x;
					yMax = y;
				}
			}
		}
	}

	//处理模块2
	for(x = floor(x0); x <= ceil(x0+R); x++)//x循环
	{
		for(y = floor(-x+x0+y0+R); y <= ceil(y0+R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis  && x>xMax)
				{
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis  && y > yMax)
				{
					xMax = x;
					yMax = y;
				}
			}
		}
	}

	//处理模块3
	for(x = floor(x0-R); x <= ceil(x0); x++)//x循环
	{
		for(y = floor(y0-R); y <= ceil(-x+x0+y0-R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis  && x>xMax)
				{
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis  && y > yMax)
				{
					xMax = x;
					yMax = y;
				}
			}
		}
	}

	//处理模块4
	for(x = floor(x0); x <= ceil(x0+R); x++)//x循环
	{
		for(y = floor(y0-R); y <= ceil(x-x0+y0-R); y++)
		{
			if((x-x0)*(x-x0) + (y-y0)*(y-y0) <= R*R)//判断是否在圆内(包括边界)
			{
				if((x-x0)*(x-x0) + (y-y0)*(y-y0) > MaxDis)
				{
					MaxDis = (x-x0)*(x-x0) + (y-y0)*(y-y0);
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis  && x>xMax)
				{
					xMax = x;
					yMax = y;
				}
				else if((x-x0)*(x-x0) + (y-y0)*(y-y0) == MaxDis  && y > yMax)
				{
					xMax = x;
					yMax = y;
				}
			}
		}
	}

	//cout << xMax << " " << yMax << endl;
	printf("%d %d\n", xMax, yMax);
	printf("%d\n",18^22);
	return 0;
}