def opish(original):
    """(str) -> str, int

    Return original word translated to opish.
    Return emtpy string if original is empty.
    Return -1 if original is non-alphabetical

    >>>opish('cat')
    'copatop'
    >>>opish('bolt')
    'bopoloptop'
    >>>opish('abracadabra')
    'abopropacopadoparopa'
    >>> opish('123')
    Non-alphabetical string input
    -1
    >>> opish('')
    Empty string input
    ''
    """

    #Converted word will be stored in new_word.
    new_word = ''

    #Check if string is empty
    if original == '':
        print("Empty string input")
    else:   
        #check if string is alphabetic
        if original.isalpha():
            #Conversion to Opish
            for char in original:
                if char in 'aeiouAEIOU':
                    new_word = new_word + char
                else:
                    new_word = new_word + char + 'op'
        else:
            print ("Non-alphabetical string input")
            return -1

    return new_word
