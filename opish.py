def opish(original):
    """(str) -> str

    Return original string translated to opish.
    Return emtpy string if original is empty.
    
    >>> opish("This is a fine day!")
    'Tophopisop isop a fopinope dopayop!'
    >>> opish('')
    Empty string input
    ''
    """



    #Check if string is empty
    if original == '':
        print("Empty string input")
        return ''
    else:
        #Converted word will be stored in new_word.
        new_word = ''
        #Conversion to Opish
        for char in original:
            if char in 'aeiouAEIOU':
                new_word = new_word + char
            else:
                #Check if there's non-alphabetic symbols in sentence
                if char in """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ""":
                    new_word = new_word + char + 'op'
                else:
                    new_word = new_word + char
        
    return new_word
