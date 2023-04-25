def validar_mes(mes):

    try:
        num_mes = int(mes)
        if (num_mes < 1 or num_mes > 12):
            raise ValueError("mes de estar entre 01 e 12")
        return True
    except ValueError:
        return False

def incluir_mes():

    mes = input("informe o mês (MM):  ")
    if validar_mes(mes):
        return mes
    
    else:
        print("Por Favor! Digite um mês no formato (MM)")
        mes = input("informe o mês (MM):  ")

        
def validar_salario(valor):
    try:
        valor_teste = float(valor)
        return True
    except ValueError:
        return False

        


def informe_valor():
    valor = input("informe o salario R$:  ")
    if validar_salario(valor):
        return valor
    else:
        print("Por favor infomre um numero no formato 100.50")  



def receita ():
     
    lista = []
    continua = "S"  

    while (continua == "S"):

        temp = []
        mes = str(incluir_mes())
        valor = str(informe_valor())
        temp.append(mes)
        temp.append(valor)

        lista = str(temp[0]) + ',' + str(temp[1])
        print(lista, end ="\n")      
                
        print(lista)

        temp.clear()

        continua = input(str("informar outro mês? S-Sim ou N-Não:  ").upper())
        print(continua)

    


    
        with open ("receita.txt", "a+") as arquivo:
            arquivo.write(lista)
            arquivo.write("\n")
        
            


    
        
                        
        
receita()
