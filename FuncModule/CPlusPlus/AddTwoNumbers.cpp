/*
@ques:You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
@author:yangchun,chen
@date:3/25/2018
@pudong district,shanghai
*/
 // Definition for singly-linked list.
  struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
	//如果l1或l2为空，直接返回
        if(l1 == NULL){
            return l2;
        }
        if(l2 == NULL){
            return l1;
        }            
	//存储链表投指针到head
        ListNode *head = l1;
	//存储两位数字相加的十位和个位
        int dec = 0,unit = 0;
	//遍历l1和l2，对应节点的值相加，并向前进位,直到next为空
        while(l1 != NULL && l2 != NULL){
            int temp = l1->val + dec + l2->val;
            dec = temp / 10;
            unit = temp %10;
            l1->val = unit;
            if(l1->next !=NULL && l2->next != NULL){
                l1 = l1->next;
                l2 = l2->next;
            }
            else{
                break;
            }
        }
	//将l1指向下个节点，这样就只需对l1进行操作了
        if(l1->next == NULL){
            l1->next = l2->next;
        }
	//遍历l1，遍历节点的值需加上之前l1和l2节点的进位值
        while(l1->next != NULL){
            int temp = l1->next->val + dec;
            dec = temp / 10;
            unit = temp % 10;
            l1->next->val = unit;
            l1 = l1->next;
        }
	//如果遍历到了l1链表尾，还是有进位，需要新建一个节点存储进位值
        if(dec > 0){
            ListNode *newnode = new ListNode(dec);
            l1->next = newnode;
        }
        return head;
    }
};
