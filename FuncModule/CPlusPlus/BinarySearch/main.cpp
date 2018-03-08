#include <iostream>
#include "BinarySearch.h"
#include "BinaryRecursionSearch.h"
using namespace std;
int main(){
	int A[] = {1,2,3,4,5,6};
	int index = BinarySearch(A,6,3);
	cout << "Binary search index is:" << index << "\n";
	index = BinaryRecurSearch(0,5,A,3);
	cout << "Binary recursion search index is:" << index << "\n";
	return 0;
}
