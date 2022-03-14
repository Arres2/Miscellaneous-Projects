def solution(number):
    lst = list(range(number))
    for n in lst:
        if n/5 or n/3 is not float():
            lst.append(n)
    print(lst)


#NO CORRER, ESTO ROMPE COMPUTADORAS