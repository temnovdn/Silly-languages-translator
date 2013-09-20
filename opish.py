def opish(original):
    """(str) -> str

    Return original string translated to opish.
    Return emtpy string if original is empty.
    
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
        #Conversion to Opish
        for char in original:
            if char in 'aeiouAEIOU':
                new_word = new_word + char
            else:
                #Check if there's non-alphabetic symbols in sentence
                if char not in """~!@#$%^&*()_+-=:"|;'\<>?,./1234567890 """:
                    new_word = new_word + char + 'op'
                else:
                    new_word = new_word + char
        
    return new_word
