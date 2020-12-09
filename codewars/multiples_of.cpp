/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

Courtesy of projecteuler.net
*/

#include <iostream>

using namespace std;

int main(){
	int n=0, total=0;
	cout << "Enter the number: " << endl;
	cin >> n;
	if(n <= 0){
		cout << '0' << endl;
		return 0;
	}
	else{
		for(int i = 0 ; i < n ; i++){
			if(i % 3 == 0 && i % 5 != 0){
				total += i;
			}
			else if(i % 3 != 0 && i % 5 == 0){
				total += i;
			}
			else if(i % 3 == 0 && i % 5 == 0){
				total += i;
			}
		}
	}
	cout << "total: " << total << endl;
	return 0;
}
