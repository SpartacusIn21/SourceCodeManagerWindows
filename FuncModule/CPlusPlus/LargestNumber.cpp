/*
@ques:Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
@author:yangchun,chen
@date:3/29/2018
@pudong,shanghai
*/
#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
//答案错误，会使得121和12的组合错误
//class Solution {
//public:
//    int CalLen(int val){
//        int len = 0;
//        if(!val){
//            return 1;
//        }
//        while(val){
//            val /= 10;
//            len++;
//        }
//        return len;
//    }
//    string largestNumber(vector<int>& nums) {
//	//只有一位时直接返回即可
//	if(nums.size() == 1){
//		return std::to_string(nums[0]);
//	}
//        vector<int> vals_len;
//        int result_len = 0;
//        //统计每个整数长度和总的长度
//        for(auto &item:nums){
//            int temp = CalLen(item);
//	    cout << "temp:" << temp << endl;
//            result_len += temp;
//            vals_len.push_back(temp);
//        }
//	cout << "result_len:" << result_len << endl;
//        //将每位整数都右侧添0到总长度
//        for(auto i = 0; i < nums.size(); i++){
//            nums[i] = nums[i]*pow(10,result_len - vals_len[i]);
//	    cout << result_len-vals_len[i] << endl;
//	    cout << "num:" << nums[i] << endl;
//        }
//        //对数据整体排序,排序前先保留原vector
//	vector<int> nums_backup = nums;
//        std::sort(nums.begin(),nums.end(),std::greater<int>());
//        string strResult;
//        //在还原成原有数据并组成字符串
//        for(auto i = 0; i < nums.size(); i++){
//            cout << "result:" << endl;
//	    cout << result_len-vals_len[find(nums_backup.begin(),nums_backup.end(),nums[i]) - nums_backup.begin()] << endl;
//	    cout << (int)nums[i]/pow(10,result_len-vals_len[i]) << endl;
//            strResult = strResult.append(std::to_string((int)(nums[i]/pow(10,result_len-vals_len[find(nums_backup.begin(),nums_backup.end(),nums[i]) - nums_backup.begin()] ))));
//        }
//        return strResult; 
//    }
//};
class Solution {
	    public:
		string largestNumber(vector<int>& nums) {
		string strLargestNumber;
		vector<string> str_nums;
		//将数字转换成字符
		for(auto &item:nums){
			str_nums.push_back(std::to_string(item));
		}
		//添加自定义函数进行字符串的比较，其实所有能用到排序思想的代码都可以转成排序，直接利用sort的自定义函数，或者是在排序算法中修改排序简单的比较大小为子定义规则
		std::sort(str_nums.begin(),str_nums.end(),[](string s1,string s2){return s1+s2>s2+s1;});
		for(auto &item:str_nums){
			strLargestNumber.append(item);
		}
		//如果首位是0，说明有多个0
		if(strLargestNumber[0] == '0'){
			return "0";
		}
		return strLargestNumber;
	}
};

int main(){
	Solution s;
	int arr[] = {121,12};
	vector<int> vec(arr,arr+2);
	string result = s.largestNumber(vec);
	cout << result << endl;

}
