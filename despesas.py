def despesas ():
    continua = "S"
    lista = []


    def informar_despesa ():
        with open ("despesa.txt", "a") as arquivo:
            arquivo.write(lista)
            arquivo.write("\n")
           


    while (continua == "S"):
        temp = []
        temp.append(input("informe o mês:  ").upper())
        temp.append(input("informe os valor dos despesas R$: "))

        lista = str(temp[0]) + ',' + str(temp[1])
        print(lista, end ="\n")

        informar_despesa()

        temp.clear()

        continua = input(str("informar outro mês: ").upper())
            
    print(lista)

despesas()