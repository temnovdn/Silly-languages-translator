def sentence_to_words(original):
    """

    Return list of words and punctuation marks from original string.
    Return -1 if string is empty.
    
    >>> sentence_to_words('This is a fine day!')
    ['This','is','a','fine','day','!']
    >>> sentence_to_words("You're like football, are you?")
    ["You're",'like','football',',','are','you','?']
    >>> sentence_to_words('')
    -1
    """

    words = []
    word = ''
    
    for char in original:
        word = word + char
        if word[-1] in """ '""":
            words.append(word[:-1])
            word = ''
        elif word[-1] in """!&();:",.?""":
            words.append(word[:-1])
            words.append(word[-1])
            word = ''

    return words[:]

def words_to_sentence(words):
    """(list) -> str

    Return given list of strings as a sentence.

    >>>words_to_sentence(["You", "'re", 'like', 'football', ',', '', 'are', 'you', '?'])
    "You 're like football, are you?"
    """

    sentence = ''
    for index in range(0,len(words)):
        word = words[index]
        if index != len(words) - 1:
            if words[index + 1] == ' ' or words [index + 1] == '' or words[index + 1] in """?.,":';-)(!""":
                    sentence = sentence + words[index]
            else:
                    sentence = sentence + words[index] + ' '
        else:   
            sentence = sentence + words[index]
    

    return sentence

        
def pig_latin(original):
    """(str) -> str

    Return original string, converted to Pig Latin.
    Return empty string if original is empty.
    Return original string if it's not alphabetical.

    >>> pig_latin('yellow')
    'ellowyay'
    >>> pig_latin('egg')
    'way'
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
        print("Empty string input")
    else:
        #Converted word willbe stored in new_word.
        new_word = ''
        first_letter = original[0]
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
    """(str) -> str

    Return the sentence, converted to pig latin.

    """
    words = sentence_to_words(sentence)
    index = 0
    
    
    while index < len(words):
        word = words[index]
        words[index] = pig_latin(word)
        index = index + 1

    return words_to_sentence(words)
