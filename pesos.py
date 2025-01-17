def converter_em_gramas(entrada, valor):
    if entrada==2:
        kg2g=valor*1000
        return kg2g
    elif entrada==3:
        ton2g=valor*1000000
        return ton2g
    

def converter_peso(entrada, saida, valor_inicial):
    if entrada==saida:
        return valor_inicial
    if entrada!=1:
        valor=converter_em_gramas(entrada, valor_inicial)
        if saida==1:
            return valor
    else:
        valor=valor_inicial
    if saida==2:
        g2kg=valor/1000
        return g2kg
    if saida==3:
        g2ton=valor/1000000
        return g2ton


unidades_pesos={
    1: "Gramas",
    2: "Quilos",
    3: "Toneladas"
}