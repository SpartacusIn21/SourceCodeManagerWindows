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
#include<stdio.h>
#include<stdlib.h>
#include"BubbleSorting.h"
linklist *head = NULL;//将该行代码放到.h文件中就会编译不通过，why?
linklist* CreateList(int*arr, int len)//由数组创建单链表，首结点未存数据
{
	int data;
	linklist *pCurrent, *rear;
	head = (linklist*)malloc(sizeof(linklist));
	rear = head;

	int count = 0;
	while(count<len)
	{
		pCurrent = (linklist*)malloc(sizeof(linklist));
		pCurrent -> data = arr[count];
		rear -> next = pCurrent;
		rear = pCurrent;
		count++;
	}
	rear -> next = NULL;
	return head;
}

void ShowList(linklist *p)//打印单链表
{
	while(p)
	{
		printf("%d ", p->data);
		p = p->next;
	}
	printf("\n");

}

void BubbleSortList(linklist *p)//链表冒泡排序
{
	linklist *_temp = p ->next;
	linklist *_node = p ->next;
	int temp;
	for(;_temp->next;_temp = _temp -> next)//纯粹控制排序趟数的,n-1趟
	{
		for(_node = p->next; _node->next; _node = _node ->next)//这其实就是最平常的冒泡排序算法写法，只是由于是链表的缘故，不太方便写成循环次数为n + n-1 + ... + 1 = n*(n+1)/2趟(对应比较次数为n-1+n-2+...+1 = n*(n-1)/2)，这里循环次数为n*n,比较次数为(n-1)*n
		{
			if(_node->data > _node ->next->data)//改变大小号就能改变排序结果升降序顺序
			{
				temp = _node->data;
				_node->data =_node->next->data;
				_node->next->data = temp;
			}
		
		}
	}

}