def pig_latin(original):
    """(str) -> str

    Return original word, converted to Pig Latin.

    >>> pig_latin('yellow')
    'ellowyay'
    >>> pig_latin('egg')
    'way'
    >>> pig_latin('')
    Empty string input
    ''
    >>> pig_latin('123')
    Non-alphabetical string input
    ''
    """

    #Converted word willbe stored in new_word.
    new_word = ''

    #Check if string is empty
    if original == '':
        print("Empty string input")
    else:   
        #check if string is alphabetic
        if original.isalpha():
            #Conversion to Pig Latin
            if original.lower()[0] in 'aeiou':
                new_word = original + 'way'
            else:
                new_word = original.lower()[1:] + original.lower()[0] + 'ay'            
        else:
            print ("Non-alphabetical string input")

    return new_word
