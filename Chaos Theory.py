def main():
    print("Este programa es para demostrar el efecto del caos")
    x, y = float(input("Inserte dos número entre el 0 y el 1: ")),float(input(""))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(x, y)
main()
