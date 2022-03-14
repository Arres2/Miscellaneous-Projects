def is_valid_IP(strng):
    ls = strng.split(".")
    for elements in ls:
    
        if elements.isdigit() == True:
            ls[elements] = int(ls[elements])
            if ls[elements] > 0 and ls[elements] < 255:
                ls[elements] = str(ls[elements])
            else:
                return False  
        else:
            return False

        for item in elements:
            print(item)

    return print(ls)

is_valid_IP("222.222.222.222")