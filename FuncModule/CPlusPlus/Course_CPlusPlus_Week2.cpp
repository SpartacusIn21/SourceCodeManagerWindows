/*
FileName: Course_CPlusPlus_Week2.cpp
Create Time:   2015/10/09
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference: https://www.coursera.org/learn/cpp-chengxu-sheji/programming/CpvBs/bian-cheng-zuo-ye-c-chu-tan 
Description: （1）简单的学生信息处理程序；(2)如何正确的使用geline函数读取以某个分隔符分开的不同类型的一行数据;
*/
/*
简单的学生信息处理程序实现

来源: POJ (Coursera声明：在POJ上完成的习题将不会计入Coursera的最后成绩。)

注意： 总时间限制: 1000ms 内存限制: 65536kB

描述

在一个学生信息处理程序中，要求实现一个代表学生的类，并且所有成员变量都应该是私有的。

（注：评测系统无法自动判断变量是否私有。我们会在结束之后统一对作业进行检查，请同学们严格按照题目要求完成，否则可能会影响作业成绩。）

输入

姓名，年龄，学号，第一学年平均成绩，第二学年平均成绩，第三学年平均成绩，第四学年平均成绩。

其中姓名、学号为字符串，不含空格和逗号；年龄为正整数；成绩为非负整数。

各部分内容之间均用单个英文逗号","隔开，无多余空格。

输出

一行，按顺序输出：姓名，年龄，学号，四年平均成绩（向下取整）。

各部分内容之间均用单个英文逗号","隔开，无多余空格。

样例输入

Tom,18,7817,80,80,90,70
样例输出

Tom,18,7817,80
*/

#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
class student
{
private:
	char Name[20];
	char StudentID[20];
	unsigned int Age;
	unsigned int Score[4];
public:
	student(const char *name, const char *studentid, unsigned int age, unsigned int *score) :Age(age)
	{
		strcpy_s(Name, name);
		strcpy_s(StudentID, studentid);
		memcpy(Score, score, 4 * sizeof(unsigned int));
	}
	void Print()
	{
		cout << Name << "," << Age << "," << StudentID << "," << (int)((Score[0] + Score[1] + Score[2] + Score[3]) / 4) << endl;
	}
};
int main()
{
	char Name[20];
	char StudentID[20];
	unsigned int Age;
	unsigned int Score[4];
	string str;
	getline(cin, str, ',');//这里的getline使用一个循环读取str并依此赋值给一个string数组也是可以的，尤其在输入数据量比较大的情况下
	strcpy_s(Name, str.c_str());//不能使用Name(Name为指针变量) = str.c_str();因为这样是指针赋值，下次str的值改变后会影响已经赋值过的变量
	getline(cin, str, ',');
	Age = atoi(str.c_str());
	getline(cin, str, ',');
	strcpy_s(StudentID, str.c_str());
	getline(cin, str, ',');
	Score[0] = atoi(str.c_str());
	getline(cin, str, ',');
	Score[1] = atoi(str.c_str());
	getline(cin, str, ',');
	Score[2] = atoi(str.c_str());
	getline(cin, str);//因为最后一个没有的分隔符是回车符，所以这里使用默认的即可
	Score[3] = atoi(str.c_str());
	student Tim(Name, StudentID, Age, Score);
	Tim.Print();
	return 0;
}