/*
FileName: Valid_Anagram.cpp
Create Time:   2015/10/26
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference:  https://leetcode.com/problems/valid-anagram/  
Description: 
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
*/

class Solution {
public:
    bool isAnagram(string s, string t) {
        int Map[32] = {0};
        if(s.length() != t.length())
            return false;
        for(int i = 0; i < s.length(); i++)
            Map[s[i] - 'a']++;
        for(int i = 0; i < t.length(); i++)
            Map[t[i]- 'a']--;
        for(int i = 0; i < s.length(); i++)
        {
            if(Map[s[i]- 'a'] != 0)
                return false;
        }
        return true;
    } 
};