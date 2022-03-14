text = input("Enter some text: ")

def transform(word):
    x = 0
    for l in word:
        x +=  ord(l)-97
    return x

def biggest_word(text):

    di = dict()
    count = text.rsplit(" ")
    for word in count:
        di[word] = di.get(word, transform(word)) 
    
    max_key = max(di, key=di.get)
    return print(max_key)


biggest_word(text)