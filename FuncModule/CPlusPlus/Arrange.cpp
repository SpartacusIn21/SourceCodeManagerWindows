/*
FileName: Arrange.cpp
Create Time:   2015/09/05
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference: 
Description: （1）计算没有相同值排在相邻位置的排列种类；
*/
/* 
  通常我们希望检查n个不同元素的所有排列方式来确定一个最佳的排序。比如a,b,c的排列方式有abc,acb,bac,bca,cab,cba六种。
  由于采用非递归的c++函数来输出排列方式很困难，所以采用递归是一种比较不错的方法。
  其核心是：将每个元素放到n个元素组成的队列最前方，然后对剩余元素进行全排列，依次递归下去。
  比如：
  a b c
  首先将a放到最前方（跟第一个元素交换），然后排列b c，然后将a放回本来位置 
   结果 a b c； a c b
  其次将b放到最前方（跟第一个元素交换），然后排列a c，然后将b放回
   结果 b a c； b c a
   。。。
  如果是4个元素，就将元素依次放到第一个元素的位置，后面的排序类似前面的3元素排序。
*/
int COUNT = 0;//在调用perm函数的地方需要将COUNT初始化为零
void SWAP(int *a,int *b) //交换数据
{
 int temp;
 temp = *a;
 *a = *b;
 *b = temp;
}
bool check(int *list, int n){//排除排列中存在值相同的排在相邻位置的情况
	 for(int i =0; i < n-1 ; i++){
		if(abs(list[i] - list[i+1]) % 13 == 0){
			return false;
		}
	 }
	 return true;
}
int perm(int *list, int i, int n)//递归实现全排列
{
	 int j/*无用,temp*/;
	 if(i == n /*&& check(list, n)*/)//必须没有相邻的数值相同的才算数
	 {
		for(j = 0; j < n; j++)
		{
		cout<<list[j];
		cout<<" ";
		}
		COUNT++;
		cout<<endl; //加
	 }
	 else
	 {
		  for(j = i; j < n; j++)
		  {
			   SWAP(list+i,list+j); //SWAP(list+i,list+j,temp);
			   perm(list,i+1,n);
			   SWAP(list+i,list+j); //SWAP(list+i,list+j,temp);
		  }
	 }
	 return COUNT;
}