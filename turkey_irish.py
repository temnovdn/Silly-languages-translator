def turkey_irish(original):
    """(str) -> str

    Return original word translated to Turkey Irish.
    Return emtu string if input string is empty.

    >>> turkey_irish("This is a fine day!")
    'Thabis abis aba fabinabe dabay!'
    >>>turkey_irish('')
    ''
    """



    #Check if string is empty
    if original == '':
        print("Empty string input")
        return ''
    else:
        #Converted word will be stored in new_word.
        new_word = ''
        first_letter = original[0]
        #Conversion to Turkey Irish
        for char in original:
            if char in """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ""":
                if char in 'aeiou':
                    new_word = new_word + 'ab' + char
                elif char in 'AEIOU':
                    new_word = new_word +'Ab' + char.lower()
                else:
                    new_word = new_word + char
            else:
                new_word = new_word + char
        

    return new_word
