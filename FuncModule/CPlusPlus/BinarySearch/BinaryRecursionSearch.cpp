/**
@author:yangchun,chen
@date:20180308
*/
#include"BinaryRecursionSearch.h"
int BinaryRecurSearch(int low, int high, int arr[],int val){
	if(low > high){
		return -1;
	}
	int mid = (low + high)/2;
	if(arr[mid] == val){
		return mid;
	}
	else if(arr[mid] > val){
		BinaryRecurSearch(low,mid-1,arr,val);
	}
	else{
		BinaryRecurSearch(mid+1,high,arr,val);
	}

}
