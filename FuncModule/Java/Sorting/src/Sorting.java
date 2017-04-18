/*
* 所有排序算法
*冒泡排序（bubble sort） — O(n^2）——已学
*鸡尾酒排序(Cocktail sort，双向的冒泡排序) — O(n^2）
*插入排序（insertion sort）— O(n^2)——已学
*桶排序（bucket sort）— O(n); 需要 O(k) 额外空间——不错，需学习
*计数排序(counting sort) — O(n+k); 需要 O(n+k) 额外空间——不错，需学习
*合并排序（merge sort）— O(nlog n); 需要 O(n) 额外空间——不错，需学习
*原地合并排序— O(n^2)
*二叉排序树排序 （Binary tree sort） — O(nlog n)期望时间； O(n^2)最坏时间； 需要 O(n) 额外空间
*鸽巢排序(Pigeonhole sort) — O(n+k); 需要 O(k) 额外空间
*基数排序（radix sort）— O(n·k); 需要 O(n) 额外空间
*Gnome 排序— O(n^2)
*图书馆排序— O(nlog n) with high probability，需要 （1+ε)n额外空间
*/
/*
 * @Date: 4-24-2015
 * @author Yangchun, Chen
 * 排序算法
 * （1）Selection_Sorting：选择排序
 * （2）Bubble_Sorting：冒泡排序
 * （3）Insert_Sorting：插入排序
 */
public class Sorting {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		int [] intArray1 = {1, 23, 45, 32, 0, 100, 3, 5, 33};
		int [] intArray2 = {1, 23, 45, 32, 0, 100, 3, 5, 33};
		int [] intArray3 = {38, 65, 97, 76, 13, 27, 49};
		int [] intArray4 = {38, 65, 97, 76, 13, 27, 49};
		int [] intArray5 = {38, 65, 97, 76, 13, 27, 49};
		int [] intArray6 = {38, 65, 97, 76, 13, 27, 49};
		
		System.out.print("选择排序:");	
		System.out.println();//回车换行
		Selection_Sorting(intArray1);
		System.out.println();//回车换行
		System.out.println();//回车换行
		
		System.out.print("冒泡排序:");
		System.out.println();//回车换行
		Bubble_Sorting(intArray2);
		System.out.println();//回车换行
		System.out.println();//回车换行
		
		System.out.print("插入排序:");
		System.out.println();//回车换行
		Insert_Sorting(intArray3);
		System.out.println();//回车换行
		System.out.println();//回车换行
		
		System.out.print("快速排序:");//非常重要，因为效率高被频繁使用	
		System.out.println();//回车换行
		System.out.print("排序前的数组元素");
		for(int a:intArray4){//遍历数组
			System.out.print(a + " ");		
		}
		Quick_Sorting(intArray4, 0, intArray4.length-1);
		System.out.println();//回车换行
		System.out.print("排序后的数组元素");
		for(int a:intArray4){//遍历数组
			System.out.print(a + " ");		
		}
		System.out.println();//回车换行
		System.out.println();//回车换行
		
		System.out.print("归并排序:");//非常重要，被众多公司频繁使用
		System.out.println();//回车换行
		System.out.print("排序前的数组元素");
		for(int a:intArray5){//遍历数组
			System.out.print(a + " ");		
		}
		System.out.println();//回车换行
		Merge_Sorting(intArray5, 0, intArray5.length - 1);
		System.out.print("排序后的数组元素");
		for(int a:intArray5){//遍历数组
			System.out.print(a + " ");	
		}
		System.out.println();//回车换行
		System.out.println();//回车换行
		
		System.out.print("希尔排序:");//非常重要，被众多公司频繁使用
		System.out.println();//回车换行
		System.out.print("排序前的数组元素");
		for(int a:intArray6){//遍历数组
			System.out.print(a + " ");		
		}
		System.out.println();//回车换行
		Shell_Sorting(intArray5, intArray5.length);
		System.out.print("排序后的数组元素");
		for(int a:intArray5){//遍历数组
			System.out.print(a + " ");	
		}
		System.out.println();//回车换行
		System.out.println();//回车换行
	}
	public static void Selection_Sorting(int[] Array){//选择排序法（因为通过第二层遍历的时候每次都选择最小的或者最大的数据）	
		int keyvalue;
		int index;
		int temp;
		System.out.print("排序前的数组元素");
		for(int a:Array){//遍历数组
			System.out.print(a + " ");		
		}
		System.out.println();//回车换行
		for(int i = 0; i < Array.length; i++){
			index = i;
			keyvalue = Array[i];
			for(int j = i; j < Array.length; j++){//遍历一次选择最小的数据
				if(Array[j] < keyvalue){//如果比keyvalue小，就更新index和keyvalue
					index = j;
					keyvalue = Array[j];
				}				
			}
			temp = Array[i];//交换遍历的最小值跟i位置的值
			Array[i] = Array[index];
			Array[index] = temp;
		}		
		System.out.print("排序后的数组元素");
		for(int a:Array){//遍历数组
			System.out.print(a + " ");		
		}
	}
	public static void Bubble_Sorting(int [] Array){//冒泡排序
				
		System.out.print("排序前的数组元素");
		for(int a:Array){//遍历数组
			System.out.print(a + " ");		
		}
		System.out.println();//回车换行
		for(int i = 0; i < Array.length; i++){		
			for(int j = 0; j < Array.length - i - 1; j++){
				if(Array[j] > Array[j+1]){
					Array[j] = Array[j] ^ Array[j+1];
					Array[j+1] = Array[j] ^ Array[j+1];
					Array[j] = Array[j] ^ Array[j+1];										
				}
			}
		}
		System.out.print("排序后的数组元素");
		for(int a:Array){//遍历数组
			System.out.print(a + " ");		
		}
	}
	public static void Insert_Sorting(int [] Array){//插入排序
		int i,j;
		int temp;
		System.out.print("排序前的数组元素");
		for(int a:Array){//遍历数组
			System.out.print(a + " ");		
		}
		System.out.println();//回车换行
		for(i = 1; i < Array.length; i++){
			temp = Array[i];
			for(j = i - 1; j >= 0; j--){
				if(temp < Array[j]){
					Array[j+1]= Array[j];//这个相当于将大的元素往高位移
				}
				else
					break;
			}
			Array[j+1] = temp;//在对应位置上插入新加入的元素Array[i]
		}
		System.out.print("排序后的数组元素");
		for(int a:Array){//遍历数组
			System.out.print(a + " ");		
		}
	}
	public static void Quick_Sorting(int [] Array, int low, int high){//快速排序，参考《程序员面试宝典》	
		int i, j;
		int index;
		if(low>= high)
			return;
		/*************一趟排序，根据index=array[i]的大小，以index为界限， 将区间分为小于index的区间和大于index的区间****************/
		i = low;
		j = high;
		index = Array[i];//存储Array[i]到index变量
		while(i < j){//分区，根据i和j来将待排序数据分成两区间，其中j所在区间大于i所在区间
			while(i < j&& Array[j] >= index)//保证前面部分值都小于j所指向元素，然后依次递减j
				j--;
			if(i < j)
				Array[i++] = Array[j];//满足该条件说明Array[j] < index，那么就将j所指向的元素放到i对应的区间中去
			while(i < j&& Array[i] < index)//然后对比i所指向元素是否小于index，将i指针往j指针靠拢
				i++;
			if(i < j)
				Array[j--] = Array[i];//满足该条件说明 Array[i] >= index，将i所指向的元素替换到j指针所指向位置
		}
		Array[i] = index;
		/****************************************************************************************************/
		Quick_Sorting(Array, low, i - 1);//注意high的值
		Quick_Sorting(Array, i+1, high);//注意low的值		
	}
	
	public static void Merge(int [] Array, int p, int q, int r){//归并排序——合并，参考《程序员面试宝典》
		int i,j,k,n1,n2;
		n1 = q - p + 1;
		n2 = r - q;
		int []L = new int[n1];
		int []R = new int[n2];
		/**********将两子表的值拷贝到数组L和R中*********/
		for(i = 0,k = p; i<n1; i++, k++){
			L[i] = Array[k];		
		}
		for(i = 0,k = q+1; i<n2; i++, k++){
			R[i] = Array[k];		
		}
		/****************************************/
		
		/**********比较两子表L、R大小，按大小顺序回赋给array数组*********/
		for(k = p, i=0, j=0; i<n1 && j<n2; k++){
			if(L[i]>R[j]){//这是降序排列，改为<为升序排列
				Array[k] = L[i];
				i++;
			}
			else{
				Array[k] = R[j];
				j++;
			}
		}
		if(i<n1){//满足i<n1说明上面for循环是由于j>=n2导致终止的，说明L中剩余的值都小于R中元素，直接按顺序复制给array就行(按这种算法， L和R中的元素都是有序的)
			for(j=i; j<n1; j++, k++){
				Array[k]=L[j];
			}
		}
		if(j<n2){//同上
			for(i=j; i<n2; i++, k++){
				Array[k]=R[i];
			}
		}
		/**********************************************/
	}
	public static void Merge_Sorting(int [] Array, int p, int r){//归并排序——递归划分子表、合并
		if(p<r){		
			int q = (p + r)/2;
			Merge_Sorting(Array, p, q);//递归划分子表，直到为单个元素为止	
			Merge_Sorting(Array, q+1, r);//递归划分子表，直到为单个元素为止	
			Merge(Array, p, q, r);	//合并半子表		
			
		}
	}
	
	public static void Shell_Sorting(int [] array, int length){//希尔排序，简单明了,给力
		int i,j;
		int h;
		int temp;
		for(h=length/2; h>0; h=h/2){//这里h为数组长度依次除2向上取整
			for(i=h; i<length; i++){//直接插入排序
				temp = array[i];//赋值i位置值给temp
				for(j=i-h; j>=0; j-=h){//如果temp(i位置对应数组数据)比j=i-h*n(n为整数)小，就交换temp和j处的数据，否则继续下一次循环
					if(temp<array[j]){//这里<号排出来的是升序，改为>变成降序
						array[j+h] = array[j];
					}
					else{
						break;
					}
				}
				array[j+h] = temp;//回赋temp值给相应的j+h位置
			}
		}
	}
	
	
}
