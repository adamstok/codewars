/* 
Description:
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).


Examples:
to_camel_case("the-stealth-warrior") // returns "theStealthWarrior"
to_camel_case("The_Stealth_Warrior") // returns "TheStealthWarrior"

*/

#include <string>
#include <iostream>

using namespace std;

int main(){
	string input,output, c;
	char next_c;
	cout << "Enter the string: \n";
	cin >> input;
	for(int i = 0; i < input.length(); i++){	
		c = input[i];
		next_c = input[i+1];
		bool check = (c == "-" || c == "_");
		if(check){
			output += toupper(next_c);
			i++;
		}
		else{
			output += c;
		}
	}
	cout << output << "\n";
	return 0;
}
