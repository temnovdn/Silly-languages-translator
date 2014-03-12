# This code translates sentence from English to Pig Latin.
       
def pig_latin(original):
    """pig_latin(str) -> str

    Return original string, converted to Pig Latin.
    Return empty string if original is empty.
    Return original string if it's not alphabetical.

    >>> pig_latin('yellow')
    'ellowyay'
    >>> pig_latin('egg')
    'eggway'
    >>> pig_latin('')
    Empty string input
    ''
    >>> pig_latin('Mary')
    'Arymay'
    >>> pig_latin('Annie')
    'Annieway'
    """

    new_word = ''
    
    #Check if string is empty
    if original == '':
        return ''
    else:
        #Converted word will be stored in new_word.
        new_word = ''
        first_letter = original[0]
        #Check if original string contains only one letter
        if len(original) > 1:
            second_letter = original[1]
        else:
            second_letter = ''
        #check if string is alphabetic
        if original.isalpha():
            #Conversion to Pig Latin
            if original[0] in 'aeiouAEIOU':
                new_word = original + 'way'
            else:
                if original[0].islower():
                    new_word = original[1:] + first_letter + 'ay'
                else:
                    new_word = second_letter.upper() + original[2:] + first_letter.lower() + 'ay'
        else:
            return original

    return new_word

def sentence_pig_latin(sentence):
    """sentence_pig_latin(str) -> str

    Return the sentence, converted to pig latin.
    
    >>> sentence_pig_latin("Quick brown fox jumps over a lazy dog.")
    'Uickqay rownbay oxfay umpsjay overway away azylay ogday.'
    >>> sentence_pig_latin("You are like football, are you?")
    'Ouyay areway ikelay ootballfay, areway ouyay?'
    """
    words = sentence.split()
    i = 0
    
    while i < len(words):
        if words[i][-1] in """:;,""":
            words.insert(i+1,words[i][-1])
            words[i] = words[i][:-1]
            i = i + 2
        else:
            i = i + 1
    
    index = 0
    
    while index < len(words):
        word = words[index]
        words[index] = pig_latin(word)
        index = index + 1

    return ' '.join(words)
