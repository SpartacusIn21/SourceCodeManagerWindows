/**
 *
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 @author:yangchun,chen
 @date:20180308
 @Loc:IQIYI innovation building of Shanghai. 
 *
 */
#include <iostream>
using namespace std;
struct ListNode{
	int val;
	ListNode *next;
	ListNode(int x):val(x),next(NULL){}
};
ListNode *ReverseLinkedList(ListNode* head){
	if(head == NULL || head->next == NULL){
            return head;
        }
	//翻转链表需要三个指针，否则串不起来
        ListNode *p = head->next,*q = head->next;
	//将链表头next指向空
        head->next = NULL;
	//遍历并将链表翻转
        while(p->next != NULL){
			p = p->next;
            q-> next = head;
            head = q;
            q = p;
        }
        q->next = head;
	//两个节点的时候避免自己指向自己
        if(p != q){
            p->next = q;
        }
        return p;
}
 
int main(){
	ListNode list[3] = {1,2,3};
	list[0].next = &list[1];
	list[1].next = &list[2];
	list[2].next = NULL;
	ListNode *p = ReverseLinkedList(list);
	while(p){
		cout << p->val << endl;
		p = p->next;
	}
	return 0;
}
