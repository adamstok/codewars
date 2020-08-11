"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples:
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    return ' '.join([x[1:]+x[0]+'ay' if x.isalnum() else x for x in text.split(' ')])


assert pig_it("latin is cool") ==  "atinlay siay oolcay"
assert pig_it("This is my string") =="hisTay siay ymay tringsay"

