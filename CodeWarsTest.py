dictionary = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5 , "g":6, "h":7, "i":8, "j":9}
dictionary2 = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f" , 6:"g", 7:"h", 8:"i", 9:"j"}
def create_phone_number():
    print("Enter a phone number")
    pn = input()
    x = dictionary2.get(pn)
    print(x)
create_phone_number()