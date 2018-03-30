/*
@ques:给定a,b,c,d,...,k个有序数组，合并成一个有序数组
@author:yangchun,chen
@date:3/30/2018
@pudong,shanghai
*/
#include<iostream>
using namespace std;
#define N 10
#define NUM 4 
int idx=1;
int arr_len = 1;
int InputArr[NUM][N] = {0};
int result[NUM*N] = {0};//a-k个数组 
//方法1 单个合并完再跟下一个合并
//将数组a和b合并存放到结果数组result中
void MergeTwoArray(int *a, int len_a,int *b, int len_b){
    	int i = 0,j=0;
    	int temp[N*NUM] = {0};
	//合并两个数组
    	while(i < len_a && j < len_b){
    	    if(a[i] > b[j]){
    	        temp[i+j] = b[j];
    	        j++;
    	    }
    	    else{
    	        temp[i+j] = a[i];
    	        i++;
    	    }
    	}
	//将数组剩余元素添加到temp结果中
    	while(i < len_a){
    	    temp[i+j] = a[i];
    	    i++;
    	}
    	while(j < len_b){
    	    temp[i+j] = b[j];
    	    j++;
    	}
	//arr_len存放当前temp数组中数据的长度，idx表示遍历了第几个数组
    	arr_len = (++idx)*N;
	//将temp结果拷贝复制给result数组
    	memcpy(result,temp,arr_len*sizeof(int));
	for(int i = 0; i < NUM*N; i++){
		cout << temp[i] << " ";
	}
	cout << endl << arr_len << endl;
	//如果所有数组都遍历完了，就退出
    	if(idx == NUM){
    	    return;
    	}
	//将当前结果result作为第一个参数，下一个数组作为第二个参数，再递归调用函数
    	MergeTwoArray(result,arr_len,InputArr[idx],N);
}

int main(){
    	for(auto i = 0; i < N; i++){
		InputArr[0][i] = i;
    	}
    	for(auto i = -10; i < -10+N; i++){
		InputArr[1][i+N] = i;
    	}
    	for(auto i = 12; i < 12+N; i++){
		InputArr[2][i-12] = i;
    	}
    	for(auto i = 7; i < 7+N; i++){
		InputArr[3][i-7] = i;
    	}
    	memset(result,0,NUM*N);
    	//
	cout << "input:" << endl;
	for(int i = 0; i < NUM; i++){
		for(int j = 0; j < N; j++){
			cout << InputArr[i][j] << " ";
		}
	}
	cout << endl;
    	MergeTwoArray(InputArr[0],N,InputArr[1],N);
	cout << "result:" << endl;
	for(int i = 0; i < NUM*N; i++){
		cout << result[i] << " ";
	}
	cout << endl;
    	return 0;
}

