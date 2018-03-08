/**
@著名ELFhash算法，用于生成hash字符串
@date:20180308
*/
#include<iostream>
#include<string>
using namespace std;
unsigned int ELFHash(char *str)  
{  
    unsigned int hash = 0;  
    unsigned int x = 0;  
  
    while (*str)  
    {  
        hash = (hash << 4) + (*str++);//hash左移4位，把当前字符ASCII存入hash低四位。   
        if ((x = hash & 0xF0000000L) != 0)  
        {  
            //如果最高的四位不为0，则说明字符多余7个，现在正在存第7个字符，如果不处理，再加下一个字符时，第一个字符会被移出，因此要有如下处理。  
            //该处理，如果最高位为0，就会仅仅影响5-8位，否则会影响5-31位，因为C语言使用的算数移位  
            //因为1-4位刚刚存储了新加入到字符，所以不能>>28  
            hash ^= (x >> 24);  
            //上面这行代码并不会对X有影响，本身X和hash的高4位相同，下面这行代码&~即对28-31(高4位)位清零。  
            hash &= ~x;  
        }  
    }  
    //返回一个符号位为0的数，即丢弃最高位，以免函数外产生影响。(我们可以考虑，如果只有字符，符号位不可能为负)  
    return (hash & 0x7FFFFFFF);  
}  
int main(){
	string a="ab",b="123",c="1",d="fdjfdf";
	cout << "hash(" << a << ")=" << ELFHash((char*)a.c_str()) << " hash(" << b  << ")=" << ELFHash((char*)b.c_str()) << " hash("  << c << ")="<< ELFHash((char*)c.c_str()) << " hash(" << d << ")=" << ELFHash((char*)d.c_str()) << endl;
	return 0;
}
