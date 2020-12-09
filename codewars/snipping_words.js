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
