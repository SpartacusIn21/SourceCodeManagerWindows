/*
@que:写一个生成微信红包的算法，输入值是钱数、红包个数，输出一个数组。
@author:yangchun,chen
@date:3/27/2018
@iqiyi,shanghai
*/
#include<iostream>
#include<vector>
#include<time.h>
#include <numeric>
#include <stdlib.h>
using namespace std;
float accumulate(vector<float>::iterator iter_begin, vector<float>::iterator iter_end){
	float sum = 0;
	for(vector<float>::iterator item = iter_begin; item != iter_end; item++){
		sum += *item;	
	}
	return sum;
}
const vector<float> wechat_redpacket(const float& money, const int&num){
	vector<float> money_arr;
	srand((unsigned)time(NULL));
	//产生1-100的随机数,最小抢到的是0.01元
	int num_cnt = num;
	while(num_cnt--){
		money_arr.push_back(rand()%1000 + 1);
	}
	//统计num个随机数的和
	int sum = accumulate(money_arr.begin(), money_arr.end());
	//将每个随机数占和的比例乘以红包额度就是抢到的红包，最后一个红包为剩余的额度
	float used_money = 0;
	for(vector<float>::iterator item=money_arr.begin(); item!=money_arr.end();item++){
		if(item != money_arr.end()-1){
			*item = money * (*item * 1.0/sum);
			used_money += *item;
		}
		else{
			*item = money - used_money;
		}
	}
	return money_arr;	
}
int main(){
	int money,num;
	cout << "Please input money:" << endl;
	cin >> money;
	cout << "Please input num:" << endl;
	cin >> num;
	const vector<float> readpacket_list = wechat_redpacket(money,num);
	cout << "wechat red packet result list:" << endl;
	for(auto &item:readpacket_list ){
		cout << item << " ";
		cout << endl;
	}
	
}
