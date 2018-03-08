/**
@author:yangchun,chen
@date:2018.3.7
@算法要求：（1）必须采用顺序存储结构（已排序）；（2）必须按关键字大小有序排列。
*/
#include "BinarySearch.h"
using namespace std;
int BinarySearch(int num[], int arrSize,int number){
	if(num == NULL || arrSize == 0){
		return -1;	
	}
	int start,end,mid;
	start = 0;
	end = arrSize - 1;
	while(start <= end){
		mid = (start + end) / 2;
		if(num[mid] == number){
			return mid;
		}
		else if(num[mid] > number){
			end = mid - 1;	
		}
		else{
			start = mid + 1;
		}
	}
	return -1;
}
