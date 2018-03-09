/**
 * 著名ELF hash算法
 * 
 *
 * */
#include <iostream>
#include <string>
using namespace std;
unsigned int ELFHash(char *key)  
{  
    unsigned int hash = 0;  
    unsigned int g = 0;  
  
    while (*key)  
    {  
        hash = (hash << 4) + (*key++);//hash左移4位，把当前字符ASCII存入hash低四位。   
        g=hash&0xf0000000L;  
        if (g)  
        {  
            //如果最高的四位不为0，则说明字符多余7个，现在正在存第7个字符，如果不处理，再加下一个字符时，第一个字符会被移出，因此要有如下处理。  
            //该处理，如果最高位为0，就会仅仅影响5-8位，否则会影响5-31位，因为C语言使用的算数移位  
            //因为1-4位刚刚存储了新加入到字符，所以不能>>28  
              
            hash ^= (g>> 24);  
              
            //上面这行代码并不会对X有影响，本身X和hash的高4位相同，下面这行代码&~即对28-31(高4位)位清零。  
              
            hash &= ~g;  
        }  
    }  
    //返回一个符号位为0的数，即丢弃最高位，以免函数外产生影响。(我们可以考虑，如果只有字符，符号位不可能为负)  
    return hash;  
}  
int main(){
	string a="abc",b="12rfs";
	cout << "hash(" << a << ")" << ELFHash((char*)a.c_str()) << endl << "hash(" << b << ")" << ELFHash((char*)b.c_str()) << endl;
	return 0;
}
