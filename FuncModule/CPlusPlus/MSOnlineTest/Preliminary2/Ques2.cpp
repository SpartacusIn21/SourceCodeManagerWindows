/*
题3
描述
Given a sequence {an}, how many non-empty sub-sequence of it is a prefix of fibonacci sequence.

A sub-sequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

The fibonacci sequence is defined as below:

F1 = 1, F2 = 1

Fn = Fn-1 + Fn-2, n>=3

输入
One line with an integer n.

Second line with n integers, indicating the sequence {an}.

For 30% of the data, n<=10.

For 60% of the data, n<=1000.

For 100% of the data, n<=1000000, 0<=ai<=100000.

输出
One line with an integer, indicating the answer modulo 1,000,000,007.

样例提示
The 7 sub-sequences are:

{a2}

{a3}

{a2, a3}

{a2, a3, a4}

{a2, a3, a5}

{a2, a3, a4, a6}

{a2, a3, a5, a6}



样例输入
6
2 1 1 2 2 3
样例输出
7
*/
//


#include <iostream>
#include<string>
using namespace std;
int count = 0;//统计子集数目
bool isFib(int *Array,int len)
{	
	if(len <= 0)
	{
		return false;
	}
	else if(len == 1 && Array[0] == 1)
	{
		return true;
	}
	else if(len == 2 && Array[0] == 1 && Array[1] == 1)
	{
		return true;
	}
	else
	{
		for(int i = 2; i < len ; i++)
		{
			if(Array[i] != Array[i-1] + Array[i-2] || Array[i] == 0)
				return false;
		}
		return true;
	}
}
void trail(int a[],short int b[],int k,int n)
{
	int j;
	if (k<n)
	{
		trail(a,b,k+1,n);
		b[k]=1-b[k];
		trail(a,b,k+1,n);
	}
	else
	{
		int temp[10000] = {0};
		int tempcount = 0;
		for (j=0;j<n;j++)
		{

			if (b[j])
			{
				temp[tempcount] = b[j];
				tempcount++;
			}
		}
		if(isFib(temp, tempcount))//如果满足要求
		{
			count++;
		}
	}

}
int Ques2(void)
{
	int n = 0;
	cin >> n;//输入n
	int *Fibonacci = new int[n];
	short int b[10000] = {0};
	int IndexF1 = 0,IndexF2=0;//用于记录数列的前两个位置
	int temp = 0;
	while(temp < n)
	{
		cin >> Fibonacci[temp];
		temp ++;
	}
	trail(Fibonacci,b,0,n);
	cout << count / 3 << endl;
	return 0; 
}
