pig_latin(original):
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
    >>> pig_latin('Mary')
    'Arymay'
    >>> pig_latin('Annie')
    'Annieway'
    """

    #Converted word willbe stored in new_word.
    new_word = ''
    first_letter = original[0]
    second_letter = original[1]

    #Check if string is empty
    if original == '':
        print("Empty string input")
    else:   
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
            print ("Non-alphabetical string input")

    return new_word
