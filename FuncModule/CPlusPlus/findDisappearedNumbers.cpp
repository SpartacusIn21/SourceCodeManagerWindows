/*
 @ques:Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

 Find all the elements of [1, n] inclusive that do not appear in this array.

 Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
@author:shujie,wang
@date:3/31/2018
@pudong,shanghai
 */
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
class Solution {
	public:
	vector<int> findDisappearedNumbers(vector<int>& nums) {
		//初始化一个数组为0
		vector<int> result(nums.size(),0);
		//遍历数组如果值存在在输出数组相应位置存1
		for(auto &item:nums){
			result[item-1] = 1;
		}
		nums.clear();
		//遍历结果将为0的存储到输出vector中
		for(int i = 0; i < result.size();i++){
			if(result[i] == 0){
				nums.push_back(i+1);
			}
		}
		return nums;
	}
};

int main(){
	int Arr[6] = {4,3,2,6,1,1};
	vector<int> vec(Arr,Arr+6);
	Solution s;
	vector<int> result = s.findDisappearedNumbers(vec);
	for(auto &item:result){
		cout << item << " " ;
	}
	cout << endl;
	return 0;
}
