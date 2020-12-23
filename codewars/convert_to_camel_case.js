/*    Complete the method/function so that it converts dash/underscore delimited words
    * into camel casing. The first word within the output should be capitalized only if
    * the original word was capitalized (known as Upper Camel Case, also often referred 
    * to as Pascal case).
    *
    * toCamelCase("the-stealth-warrior") // returns "theStealthWarrior"
    * toCamelCase("The_Stealth_Warrior") // returns "TheStealthWarrior"
    *
    *   */

function toCamelCase(str) {
    let splitted = [...str];
    for (let i = 0; i < splitted.length; i++){
        if(splitted[i] == '-' || splitted[i] == '_'){
            splitted[i + 1] = splitted[i + 1].toUpperCase();
            splitted[i] = '';
        }
    }
    return splitted.join('');
}

console.log(toCamelCase(''));
console.log(toCamelCase('the-stealth_warrior'));
console.log(toCamelCase('The_see-w'));
console.log(toCamelCase('A_B-c'));

