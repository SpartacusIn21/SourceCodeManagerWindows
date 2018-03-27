/*
@que:A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
@url:https://leetcode.com/problems/self-dividing-numbers/description/
@author:yangchun,chen
@date:3/27/2018
@pudong,shanghai
*/
class Solution {
public:
    bool Devisible(const int &val){
        int temp = val;
        bool result = true;
        while(temp){
	    //获取余数
            int remainder = temp % 10;
            if((remainder == 0) ||
              (val % remainder != 0)){
                result = false;
                break;
            }
	    //往右移位
            temp /= 10;
        }
        return result;
    }
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> arr;
        for(int index = left; index <= right; index++){
                if(Devisible(index)){
                    arr.push_back(index);
                }
            
        }
        return arr;
    }
};
