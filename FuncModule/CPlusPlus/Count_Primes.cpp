//法1：效率高
#include<iostream>
#include<math.h>
#include<stdlib.h>
using namespace std;
int countPrimes(int n){
	if(n <= 2) return 0;
	if(n == 3) return 1;
	bool *prime = (bool *)malloc(sizeof(bool)*n);
	int i = 0, j = 0;
	int count = n-2;
	int rt = sqrt(n);
	for(int j =0; j < n; j++){//用于辨别prime[j]是不是素数，素数时为true，不是素数时为false

			prime[j] = 1;
	}

	for( i = 2; i <=rt; i++){//大循环，因为第二个循环是i的平方开始的，所以这里要取到rt=sqrt(n)就行了


		if(prime[i]){//如果prime[i]为false，i不是素数，之前已经计算过，就不用再次计算



					for(j = i *i; j < n; j+=i){//使j=i*i开始，然后依次加上i，这样循环一遍就将prime中i*i,i*i+i,i*i+2*i...排除掉，并将count减1

						if(prime[j]){//如果prime[j]为false，j不是素数，之前已经计算过，就不用再次计算

								prime[j]=0;//j不是素数，将prime[j]置0
								count--;//排除掉j
						}
					}
		}
	}
free(prime);
	return count;
}
int main(){

		cout << "Input Number:" << endl;
		int N;
		cin >> N;
		int Count =	countPrimes(N);
		cout << Count << endl;
}

//法2：效率低
/* #include<iostream>
#include<math.h>
using namespace std;
//Solution 1
int CountPrimeNumbers(int n){//计算小于n的素数个数
	unsigned	int count = 0;//用于统计素数个数
	bool flag = false;
	int m = 0;
	for(int i = 2; i < n; i++){
		flag = true;
		m = floor(sqrt((float)i));
		for(int j = 2; j <= m; j++){
			if(i %  j == 0){
				flag = false;	
				break;
			}
		}
		if(flag == true){
			
				count++;
		}
		
	}
	cout << "Prime Numbers:" << count << endl;
	
}
int main(){
		cout << "Input Number:" << endl;
	int Number;//输入的数字，然后计算小于该数共有多少素数
	cin >> Number;
	CountPrimeNumbers(Number);	
} */


