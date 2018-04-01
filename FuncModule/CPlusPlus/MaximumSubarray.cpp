/*
 *@ques:Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

 For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
 the contiguous subarray [4,-1,2,1] has the largest sum = 6.
 @url:https://leetcode.com/problems/maximum-subarray/description/
 @author:yangchun,chen
 @date:4/1/2018
 * */
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
	public:
	int maxSubArray(vector<int>& nums) {
		vector <int> dp = nums;
		//将最大值和动态规划数组先赋值为第一位
		int max = nums[0];
		dp[0] = nums[0];
		//遍历数组，将数组当前位置的值与动态规划数组前一位相加，如果前一位值大于0，就相加再存到当前位置，否则只保留当前位置的值，在遍历过程中每次与max值比较
		for(int i = 1; i < nums.size(); i++){
			dp[i] = nums[i] + (dp[i-1] > 0 ? dp[i-1] : 0);
			max = std::max(max,dp[i]);
		}
		return max;
	}
};
int main(){
	int arr[2] = {-1,-2};
	vector<int> vec(arr,arr+2);
	Solution s;
	int result = s.maxSubArray(vec);
	cout << result << endl;
	return 1;
}
