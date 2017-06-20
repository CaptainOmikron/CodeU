#include <iostream>
#include <string>
#include <algorithm>
#include <assert.h>
/*
This program checks if two strings are
permutations of each other.
*/
using namespace std;

bool permutation(string s1, string s2) {
	/* Input handling: 
	Test cases imply that there should be no distinction
	between upper and lower case letters. 
	So the next two lines transform both strings to 
	lower case only. Note that this leaves special 
	Characters unchanged */
	transform(s1.begin(), s1.end(), s1.begin(), tolower);
	transform(s2.begin(), s2.end(), s2.begin(), tolower);

	// Have to be the same size:
	if (s1.size() != s2.size()) {
		return false;
	}
	/* Have to have the same letters:
	Idea: Go through every character in s1, find it in
	s2 and remove it there. That way s2 should be 
	an empty string anfterwards if and only if s1 and s2 
	have the same characters. 
	Concerning COMPLEXITY:
	Let N be the length of s1 (and thereby also of s2 - I 
	just checked that they have the same length):
	Then the following "double loop" will obviously be 
	O(N^2), which isn't great. 
	I know that Python offers an efficient function to 
	look up weather a string contains a letter or not, 
	which could be used to make this code faster, but to 
	my knowledge c++ handles strings differently - I 
	could be wrong. 
	*/
	for (int i1 = 0; i1 < s1.size(); i1++){
		for (int i2 = 0; i2 < s2.size(); i2++){
			if (s1[i1] == s2[i2]) {
				s2.erase(i2, 1);
			}
		}
	}
	if (s2 == "") {
		return true;
	}
	return false;
}

int main() {
}
