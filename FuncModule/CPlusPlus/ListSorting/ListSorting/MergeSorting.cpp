/*
FileName: BubbleSorting.h
Create Time:   2015/09/04
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference:  《程序员面试宝典》——13.2.9 如何进行单链表排序
Description: （1）单链表的归并排序算法；
*/
#include<iostream>
#include"MergeSorting.h"
using namespace std;
void Merge(SqList SR, SqList &TR, int i, int m, int n)
{
	int j,k;
	for(j = m+1,k=i; i<=m&&j<=n; ++k)
	{
		if(SR.r[i] <= TR.r[j])
		{
			TR.r[k] = SR.r[i++];
		}
		else
		{
			TR.r[k] = SR.r[j++];
		}
		
	}
	while(i <= m)
			TR.r[k++] = SR.r[i++];
	while(j <=n)
		TR.r[k++] = SR.r[j++];
}

void MSort(SqList SR, SqList &TR1, int s, int t)
{
	int m;
	SqList TR2;
	if(s == t)//这里输入有两个SqList是为了把其中一个用来当做数组存储变量
		TR1.r[s] = SR.r[t];
	else
	{
		m = (s+t)/2;
		MSort(SR, TR2, s, m);
		MSort(SR, TR2, m+1, t);
		Merge(TR2, TR1, s, m, t);
	}

}
void MergeSort(SqList &L)
{
	MSort(L, L ,1, L.length);
}