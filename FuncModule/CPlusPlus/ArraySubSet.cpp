/*
@ques：输出数组的的所有子集
@author:yangchun,chen
@date:3/29/2018
@iqiyi,shanghai
*/
#include<cstdio>

int a[10];

void print_subset(int n,int *b,int cur)  //确定第cur位选或者不选 
{
    if (cur==n)  //如果确定好了n位，打印结果 
    {
        printf("{ ");
        for (int i=0;i<n;i++)
            if (b[i]) printf("%d ",a[i]);
        printf("}\n");
    } 
    else
    {
        b[cur]=1;  //这一位选 
	printf("cur:%d-1\n",cur);
        print_subset(n,b,cur+1);  //递归下一位 
        b[cur]=0;  //这一位不选 
	printf("cur:%d-0\n",cur);
        print_subset(n,b,cur+1);  //递归下一位 
    }
}

int main()
{
    int n;
    int b[10]={};
    scanf("%d",&n);
    for (int i=0;i<n;i++) a[i]=i;
    print_subset(n,b,0);
    return 0;
}
