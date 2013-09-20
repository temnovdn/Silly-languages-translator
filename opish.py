def opish(original):
    """(str) -> str

    Return original word translated to opish.

    >>>opish('cat')
    'copatop'
    >>>opish('bolt')
    'bopoloptop'
    >>>opish('abracadabra')
    'abopropacopadoparopa'
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

    return new_word
