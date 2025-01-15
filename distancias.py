def converter_em_metros(entrada, valor):
    if entrada==1:
        mm2m=valor/1000
        return mm2m
    elif entrada==2:
        cm2m=valor/100
        return cm2m
    elif entrada==4:
        km2m=valor*1000
        return km2m
    elif entrada==5:
        mi2m=valor*1609.34
        return mi2m
    elif entrada==6:
        in2m=valor*25.4/1000
        return in2m
    

def converter_unidade(entrada, saida, valor_inicial):
    if entrada==saida:
        return valor_inicial
    if entrada!=3:
        valor=converter_em_metros(entrada, valor_inicial)
        if saida==3:
            return valor
    else:
        valor=valor_inicial
    if saida==1:
        m2mm=valor*1000
        return m2mm
    elif saida==2:
        m2cm=valor*100
        return m2cm
    elif saida==4:
        m2km=valor/1000
        return m2km
    elif saida==5:
        m2mi=valor/1609
        return m2mi
    elif saida==6:
        m2in=valor*39.37
        return m2in


unidades_de_medida={
    1: "Milímetros",
    2: "Centímetros",
    3: "Metros",
    4: "Quilômetros",
    5: "Milhas",
    6: "Polegadas"
}

unidade_entrada_texto="""
Qual a unidade de entrada?
    1) Milímetros
    2) Centímetros
    3) Metros
    4) Quilômetros
    5) Milhas
    6) Polegadas
Digite apenas o número correspondente: """

unidade_saida_texto="""
Qual a unidade de saida?
    1) Milímetros
    2) Centímetros
    3) Metros
    4) Quilômetros
    5) Milhas
    6) Polegadas
Digite apenas o número correspondente: """

unidade_valor_texto='Digite o valor a ser convertido: '