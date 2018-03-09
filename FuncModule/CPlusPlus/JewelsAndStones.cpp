/**
 * 
 @question:https://leetcode.com/problems/jewels-and-stones/description/
 @You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
 @author:yangchun,chen
 @date:20180309

*/
#include <iostream>
#include <string>
#include <set>
using namespace std;
//complex:o(n*n)
int numJewelsInStones(string J, string S) {
        int count = 0;
        for(int i = 0; i < J.length(); i++){
            for(int j = 0; j < S.length(); j++){
                if(J.at(i) == S.at(j)){
                    count++;
                }
            }
        }
        return count;        
    }
//complex:o(n+m)
int numJewelsInStones_hash(string J, string S) {
        int res = 0;
        set<char> setJ(J.begin(), J.end());
        for (char s : S) if (setJ.count(s)) res++;
        return res;
    }
int main(){
	string J = "sj2w";
	string S = "sjjjDKE";
	cout << "S:" << S << " J:" << J << endl;
	cout << "Has " << numJewelsInStones(J,S) << " jewels in stones!" << endl;
	cout << "Has " << numJewelsInStones_hash(J,S) << " jewels in stones!" << endl;
}
