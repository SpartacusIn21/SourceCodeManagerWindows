#include"BubbleSorting.h"
#include<iostream>
#include<cstdlib>
#include"MergeSorting.h"
using namespace std;
extern linklist *head;
int main()
{
	//√∞≈›≈≈–Ú
	int Array[] = {3,4,5,1,2,-1,7};
	CreateList(Array, sizeof(Array)/sizeof(Array[0]));
	BubbleSortList(head);
	ShowList(head->next);

	//πÈ≤¢≈≈–Ú
	int i;
	SqList L = {{0,49,38,65,97,76,13,27}, LENGTH};
	MergeSort(L);
	for(i=1; i <= L.length; i++)
		cout << L.r[i] << " ";
	cout << endl;
	
	return 0;

}