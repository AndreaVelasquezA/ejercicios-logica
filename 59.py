def main():
    p= 0
    n = 0
    pares = 0
    imp = 0
    mulltoch = 0
    while True:
        try:
            number = float(input("Number: "))
            if number < 0:
                n += 1
            else:
                p += 1
            if number % 2:
                pares += 1
            else:
                imp += 1
            if not number % 8:
                mulltoch += 1
        except ValueError:
            break
    print("positivos", p)
    print("negativos", n)
    print("pares", pares)
    print("impares", impares)
    print("multiplos de ocho", mulltoch)


