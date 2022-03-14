def evaporator(content, evap_per_day, threshold):
    p = evap_per_day * content / 100
    threshold = threshold * content /100
    print(threshold, p)
    n = int()
    while threshold != content:
        content -= p
        print(content)
        n += 1
        print(n)

evaporator(120,10,5)