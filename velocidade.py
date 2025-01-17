from funcoes import opcoes_selecao


def converter_em_metros_por_segundo(entrada, valor):
    if entrada==2:
        kmh2mps=valor/3.6
        return kmh2mps
    if entrada==3:
        mph2mps=valor*0.44704
        return mph2mps
    

def converter_velocidade(entrada, saida, valor_inicial):
    if entrada==saida:
        return valor_inicial
    if entrada!=1:
        valor=converter_em_metros_por_segundo(entrada, valor_inicial)
        if saida==1:
            return valor
    else:
        valor=valor_inicial
    if saida==2:
        mps2kmh=valor*3.6
        return mps2kmh
    if saida==3:
        mps2mph=valor/0.44704
        return mps2mph
    

unidades_velocidade={
    1: "Metros por Segundo (M/s)",
    2: "Quilômetros por hora (Km/h)",
    3: "Milhas por hora (Mph)"
}
    