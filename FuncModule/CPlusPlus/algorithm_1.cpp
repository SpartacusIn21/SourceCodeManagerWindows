/*
@que:田忌赛马，每人的马数量为奇数，任何一匹马的速度都不相同；请写出一个方法，判断在某一组输入的情况下，田忌有没有可能赢。比如田忌马的速度分别为(30,37,38)，齐王马的速度分别为(31,35,41)
@author:yangchun,chen
@date:3/26/2018
@iqiyi,shanghai
*/
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int arr1[] = {32,22,13};
int arr2[] = {23,25,78};
vector<int>v1(arr1,arr1+3);
vector<int>v2(arr2,arr2+3);
bool tianjisaima(vector<int>& v1/*田忌*/, vector<int>& v2/*齐王*/){
	std::sort(v1.begin(),v1.end(),greater<int>());
	std::sort(v2.begin(),v2.end(),greater<int>());	

}
int main(){
	//对田忌和齐王的马都按从大到小排序
	tianjisaima(v1,v2);
	for(auto &i:v1){
		cout << i << " ";
	}
	cout << endl;
	for(auto &i:v2){
		cout << i << " ";
	}
	cout << endl;
	//遍历两个vector，当田忌的速度大于齐王的，就统计加1，然后往右移动一个位置，否则只移动齐王的马的位置，直到所有的遍历结束
	int count = 0;
	int i=0,j=0;
	while(i<v1.size() && j<v2.size()){
		if(v1[i]<v2[j]){
			j++;	
		}	
		else{
			i++;
			j++;
			count++;
		}
	}
	cout << "count:" << count << endl;
	if(count >= (v1.size()/2+1)){
		cout << "great!" << endl;
	}
	else{
		cout << "ops!" << endl;
	}
}
