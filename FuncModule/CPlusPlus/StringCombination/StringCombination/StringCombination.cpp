#include<stdio.h>
#include<string.h>

void CombineRecursiveImpl(const char* str, char* begin, char* end)//这个得好好研究下，指针运用的比较神奇
{
	if(*str == 0)//满足str为空时
	{
		*end = 0;
		if(begin != end)//当不为空时输出字符
			printf("%s ", begin);
		return;
	}
	CombineRecursiveImpl(str+1, begin, end);
	*end = *str;
	CombineRecursiveImpl(str+1, begin, end+1);
}

void CombineRecursive(const char str[])
{
	if(str == NULL)
		return;
	const int MAXLENGTH = 64;
	char result[MAXLENGTH];
	CombineRecursiveImpl(str, result, result);
}

int main()
{
	CombineRecursive("abc");
	printf("\n");
	return 0;	
}