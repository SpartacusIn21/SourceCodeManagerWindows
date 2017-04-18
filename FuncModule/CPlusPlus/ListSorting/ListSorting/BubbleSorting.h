/*
FileName: BubbleSorting.h
Create Time:   2015/09/04
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference:  《程序员面试宝典》——13.2.9 如何进行单链表排序
Description: （1）单链表的冒泡排序算法；
*/

#ifndef _BUBBLESORTING_H_
#define _BUBBLESORTING_H_
#include<stdio.h>
typedef struct node
{
	int data;
	struct node *next;
}linklist;
linklist* CreateList(int *arr, int len);
void ShowList(linklist *p);
void BubbleSortList(linklist *p);
#endif