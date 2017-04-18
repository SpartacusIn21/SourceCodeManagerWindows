/*
FileName: RotateList.cpp
Create Time:   2015/09/04
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference:  https://leetcode.com/problems/rotate-list/
Description: （1）List翻转末尾K个节点到首端；
*/
/*
例程：
For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
*/



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        //这里定义三个指针即可，p指针指向前k个Node的头，q指向前k个Node的尾，然后将head指向q->next,然后l指向list倒数第二个指针，接下来将p->next=p,q->next=NULL即可。
        if(head == NULL || k == 0)//如果为空或者K=0直接返回head即可
            return head;
		//统计List节点数
        int NodeNums = 1;
        ListNode* tempNode = head;
		while((tempNode = tempNode->next) != NULL)
        {
            NodeNums++;
        }
		//计算截断的节点位置，这个需要好好理清思路
        int count = NodeNums - k - 1;//公式1
        if((count < 0) && (k % NodeNums == 0))//当count<0且k能整除List节点数时，说明不需要做出改变
        {
            return head;
        }
        else if((count < 0) && (k % NodeNums != 0))//当count<0且k不能整除List节点数时，需要计算统计截断位置
        {
            count = NodeNums - k % NodeNums-1;//公式2——其实跟公式1是一样的
        }
		//将后端K个节点提到List前端来
        ListNode* p=head,*q=head,*l=head;
        while(count>0)
        {
            q = q->next;
            count--;
        }
        l = head = q->next;
        while(l->next != NULL)
        {
            l = l ->next;
        }
        l -> next = p;
        q -> next = NULL;
        return head;
        
    }
};