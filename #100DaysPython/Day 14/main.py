def is_isogram(string):
    new_word = ""
    repeated_words = ""
    
    for words in string.lower():
        if len(string) == 0:
            pass
        elif words in new_word:
            repeated_words += words
        else:
            new_word += words
        
    if len(repeated_words) >= 1:
        print(True)
    else:
        print(False)
        
is_isogram("Dermatoglyphics")

