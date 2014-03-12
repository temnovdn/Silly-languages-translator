#This translator will translate provided sentence to Opish, Turkey Irish or
#Pig Latin.

import pig_latin
import opish
import turkey_irish

i = 1

while i > 0:
    sentence = input("Please type the sentence to translate: ")
    print("Please select output language:")
    print("1 Opish\n2 Turkey Irish\n3 Pig Latin")

    select_done = False
    select = input("Input 1,2 or 3 here: ")
    
    if select == '1':
        select_
        new_sentence = opish.opish(sentence)
        print(new_sentence)
    elif select == '2':
        new_sentence = turkey_irish.turkey_irish(sentence)
        print(new_sentence)
    elif select == '3':
        new_sentence = pig_latin.sentence_pig_latin(sentence)
        print(new_sentence)
    else:
        print('Please input 1, 2, or 3')  
