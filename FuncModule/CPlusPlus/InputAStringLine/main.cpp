/*
FileName: BinaryTree.cpp
Create Time:   2015/09/16
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference:  
Description: （1）主要测试在控制台应用程序中如何输入一整行的字符串数据，这个在微软实习生招聘以及华为正式招聘机考的时候都出问题，切记，血的教训；
			 （2）将输入的字符串的首字母变为大写，如果本来就是大写或者是数字，就保持不变。
*/


//#define METHOD1
//#define METHOD2
#define METHOD3


#if defined METHOD1

#include<stdio.h>
#include<string.h>
void ToB(char* Input)
{
	int len = strlen(Input) + 1;
	char *temp = " ";
	for(int i = 0; i < len; i++)
	{
		if(i == 0)
		{
			Input[i] = Input[i] - 32;
		}
		else if(Input[i-1] == ' ' && (Input[i] >= 'a' && Input[i] <= 'z'))
		{

			Input[i] = Input[i] - 32;
		}
		else
		{
			Input[i] = Input[i];
		}
	}

}

int main()
{
	char Input[100] = {0};
	char Output[1000] = {0};
	gets(Input);
	ToB(Input);
	printf("%s ", Input);
	return 0;
}

#elif defined METHOD2

#include<iostream>
#include<string>
using namespace std;
void ToB(string &Input)
{
	int len = Input.size();
	for(int i = 0; i < len; i++)
	{
		if(i == 0)
		{
			Input[i] = Input[i] - 32;
		}
		else if(Input[i-1] == ' ' && (Input[i] >= 'a' && Input[i] <= 'z'))
		{

			Input[i] = Input[i] - 32;
		}
		else
		{
			Input[i] = Input[i];
		}
	}

}

int main()
{
	string Input;
	getline(cin,Input);
	ToB(Input);
	cout << Input << endl;
 	return 0;
}

#elif defined METHOD3

#include<iostream>
#include<string>
using namespace std;
void ToB(char *Input)
{
	int len = strlen(Input);
	for(int i = 0; i < len; i++)
	{
		if(i == 0)
		{
			Input[i] = Input[i] - 32;
		}
		else if(Input[i-1] == ' ' && (Input[i] >= 'a' && Input[i] <= 'z'))
		{

			Input[i] = Input[i] - 32;
		}
		else
		{
			Input[i] = Input[i];
		}
	}

}

int main()
{
	char Input[1000];
	cin.getline(Input, 1000);
	ToB(Input);
	cout << Input << endl;
	return 0;
}

#endif