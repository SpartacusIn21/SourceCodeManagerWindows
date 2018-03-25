/*
@ques:Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
@url:https://leetcode.com/problems/sum-of-two-integers/description/
@author:shujie,wang
@date:3/25/2018
@pudong district,shanghai
*/
class Solution {
public:
    int getSum(int a, int b) {
	//异或后，再加上相与的结果左移作为进位，循环往复
        while(a&b){
            int temp = a;
            a = (temp & b)<<1;
            b = temp ^ b;
        }
        return a|b;
    }
};

