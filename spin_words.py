def spin_words(sentence): 
    reversed = ""
    sentence = sentence.split(" ")
    for word in sentence:
        if len(word)>=5:
            for letters in range(len(word),0,-1):
                reversed += word[letters-1] 
            sentence[sentence.index(word)] = reversed
    return " ".join(sentence)