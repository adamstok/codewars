/*
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
*/


let snipping = function(text){
    let outp = [];
    let splitted = text.split(' ');
    for (let i = 0; i < splitted.length; i++){
        if (splitted[i].length < 5){
            outp.push(splitted[i]);
        } else {
            let new_word = splitted[i].split('').reverse().join('');
            outp.push(new_word);
        }
    }
    console.log(outp.join(' '));
    return outp.join(' ');
}

snipping('hello World abcdefghijk');
