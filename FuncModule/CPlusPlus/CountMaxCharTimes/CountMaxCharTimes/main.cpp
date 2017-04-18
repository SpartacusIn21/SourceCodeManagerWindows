/*
FileName: CountMaxCharTimes
Create Time:   2015/09/18
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区西70宿舍12044
Reference:  
Description: （1）寻找输入的字符串中出现次数最多的字符以及出现的次数；
*/
#include<iostream>
#include<string>
#include<map>
#include<algorithm>
using namespace std;

//方法1：使用map机制
map<char,int> Map_char_int;
void CountTimesofChar(string Input)
{
	int len = Input.size();
	for(int i = 0; i < len; i++)//将字符串利用map进行映射
	{
		Map_char_int[Input[i]]++;
	}
	map<char,int>::iterator Max = Map_char_int.begin();//用于存储出现次数最多的iterator变量
	(*Max).second = 0;
	for(map<char,int>::iterator item = Map_char_int.begin(); item != Map_char_int.end(); item++)//遍历Map，寻找出现次数最多的字符
	{
		if((*item).second > (*Max).second)//*item取的是key值，而(*item).second取的才是value值
		{
			Max = item;
		}
	}
	cout << (*Max).first << ":" << (*Max).second << endl;//输出字符串中出现次数最多的字符以及次数
}


//方法2：使用最常用方法，更便捷
void CountTimesofStr(string Input)
{
	int TimesofChar[26] = {0};//用于存储各个字符出现的次数
	int len = Input.size();
	int index=0, MaxTimes=0;//用于统计出现最大次数字符在数据TimesofChar中的位置及次数
	for(int i = 0; i < len; i++)
	{
		TimesofChar[Input[i]-'a']++; 
	}
	for(int i = 0; i < 26; i++)
	{
		if(TimesofChar[i] > MaxTimes)
		{
			index = i;
			MaxTimes = TimesofChar[i];
		}
	}
	cout << char(index + 'a') << ":" << MaxTimes << endl;

}
int main()
{
	cout << "Input a string:" << endl;
	string Input;
	//方法1
	//getline(cin, Input);
	//CountTimesofChar(Input);
	//方法2
	getline(cin, Input);
	CountTimesofStr(Input);
	return 0;
}
