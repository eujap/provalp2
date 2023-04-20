def receita ():
    continua = []
    lista = []


    def informar_rendimento ():
        with open ("receita.txt", "a") as arquivo:
            arquivo.write(lista)
            arquivo.write("\n")
            arquivo.close


    while (continua != "N"):
        temp = []
        temp.append(input("informe o mês:  ").upper())
        temp.append(input("informe os valor dos rendimentos R$: "))

        lista = str(temp[0]) + ',' + str(temp[1])
        print(lista, end ="\n")

        informar_rendimento()

        temp.clear()

        continua = input(str("informar outro mês: ").upper())
            
    print(lista)


