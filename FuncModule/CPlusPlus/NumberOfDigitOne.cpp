/*
FileName: NumberOfDigitOne.cpp
Create Time:   2015/09/15
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference: https://leetcode.com/problems/number-of-digit-one/
Description: （1）统计小于等于n的所有非负整数中数字1出现的次数；
*/

class Solution {
public:
        
int countDigitOne(int n) {
    int ones = 0;
    for (long long m = 1; m <= n; m *= 10)
        ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n%m + 1);//神算法
    return ones;
}
// Explanation

// Let me use variables a and b to make the explanation a bit nicer.

// int countDigitOne(int n) {
//     int ones = 0;
//     for (long long m = 1; m <= n; m *= 10) {
//         int a = n/m, b = n%m;
//         ones += (a + 8) / 10 * m + (a % 10 == 1) * (b + 1);
//     }
//     return ones;
// }
// Go through the digit positions by using position multiplier m with values 1, 10, 100, 1000, etc.

// For each position, split the decimal representation into two parts, for example split n=3141592 into a=31415 and b=92 when we're at m=100 for analyzing the hundreds-digit. And then we know that the hundreds-digit of n is 1 for prefixes "" to "3141", i.e., 3142 times. Each of those times is a streak, though. Because it's the hundreds-digit, each streak is 100 long. So (a / 10 + 1) * 100 times(乘以100是因为个位十位有0~99共100种情况), the hundreds-digit is 1.

// Consider the thousands-digit, i.e., when m=1000. Then a=3141 and b=592. The thousands-digit is 1 for prefixes "" to "314", so 315 times. And each time is a streak of 1000 numbers. However, since the thousands-digit is a 1, the very last streak isn't 1000 numbers but only 593 numbers(依次以200,2000,20000为界来区分), for the suffixes "000" to "592". So (a / 10 * 1000) + (b + 1) times, the thousands-digit is 1.

// The case distincton between the current digit/position being 0, 1 and >=2 can easily be done in one expression. With (a + 8) / 10 you get the number of full streaks, and a % 10 == 1 tells you whether to add a partial streak.
        
};