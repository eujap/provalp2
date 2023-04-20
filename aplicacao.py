receita = input("qual receita ")
despesa = input("qual despesa ")
resultado = ""


def meta_aplicacao ():
    
    meta = float(receita) * float(0.10)
    print(meta)
    res_aplicacao = float(receita)-float(despesa)
    print(res_aplicacao)

    if res_aplicacao <= meta :
        resultado = "meta atingida"
    else:
        resultado = "meta não atingida"


meta_aplicacao()
print(resultado)
