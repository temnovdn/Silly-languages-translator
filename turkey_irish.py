def turkey_irish(original):
    """

    Return original word translated to Turkey Irish.
    Return empty string if original is empty.
    Return -1 if original is non-alphabetical

    >>>turkey_irish('cat')
    'cabat'
    >>>turkey_irish('bolt')
    'babolt'
    >>>turkey_irish('abracadabra')
    'ababrabacabadababraba'
    >>>turkey_irish('Mary')
    'Mabary'
    >>>turkey_irish('Annie')
    'Abannabiabe'
    >>>turkey_irish('123')
    'Non-alphabetical string input'
    ''
    """

    #Converted word will be stored in new_word.
    new_word = ''
    first_letter = original[0]

    #Check if string is empty
    if original == '':
        print("Empty string input")
    else:   
        #check if string is alphabetic
        if original.isalpha():
            #Conversion to Turkey Irish
            for char in original:
                if char in 'aeiou':
                    new_word = new_word + 'ab' + char
                elif char in 'AEIOU':
                    new_word = new_word +'Ab' + char.lower()
                else:
                    new_word = new_word + char
        else:
            print ("Non-alphabetical string input")
            return -1

    return new_word
