
try:
    numeroEntrada = int(input("Listar N números primos: "))
except:
    print("O número deve ser inteiro")
    exit()
numeroIniciar = 1
listaPrimo = []
while True:
    if numeroEntrada <= 0:
        print("O número inserido deve ser maior que zero")
        break
    if numeroIniciar > 1:
        for i in range(2, numeroIniciar):
            if (numeroIniciar % i) == 0:
                break
        else:
            listaPrimo.append(numeroIniciar)
    if (len(listaPrimo) == numeroEntrada):
        print(listaPrimo)
        break
    else:
        numeroIniciar = numeroIniciar + 1
        continue