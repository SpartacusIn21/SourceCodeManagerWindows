/*
@ques:Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.
@url:https://leetcode.com/problems/kth-largest-element-in-an-array/description/
@author:yangchun,chen
@date:3/29/2018
@iqiyi,shanghai 
*/
class Solution {
public:
    //一次快速排序，选取中间位置pos,pos左边的都比pos小，pos右边的都比pos大,根据这个特性如果pos跟k相等，就代表k值找到了
    int QuickSelect(vector<int>& nums, int low, int high){
        int index;
        index = nums[low];
        while(low < high){
            while(low < high && nums[high] <= index){//如果是Top K小，改成nums[high] >= index
                high--;
            }
            if(low < high){
                nums[low++] = nums[high];
            }
            while(low < high && nums[low] > index){//如果是Top K小，改成nums[low] < index
                low++;
            }
            if(low < high){
                nums[high--] = nums[low];
            }
            nums[low] = index;
        }
        return low;
    }
    //判断k的位置跟当前快排选择的part的位置是否一致，不一致再递归调用
    int kth(vector<int> &nums, int k, int low, int high){
        int part = QuickSelect(nums,low,high);
        if (part == k) 
            return nums[part];//如果是Top K元素值，返回nums[0:part]
        else if(part+1 > k)
            return kth(nums,k,low,part-1);
        else
            return kth(nums,k,part+1,high);
    }
    int findKthLargest(vector<int>& nums, int k) {
        return kth(nums,k-1,0,nums.size()-1);//k-1是因为元素从0开始
    }
};
