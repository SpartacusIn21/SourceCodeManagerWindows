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

#ifndef _MERGESORTING_H_
#define _MERGESORTING_H_
#define MAXSIZE 1024
#define LENGTH 8
typedef struct
{
	int r[MAXSIZE + 1];
	int length;
}SqList;
void Merge(SqList SR, SqList &TR, int i, int m, int n);
void MSort(SqList SR, SqList &TR1, int s, int t);
void MergeSort(SqList &L);

#endif