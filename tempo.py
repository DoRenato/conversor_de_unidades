def converter_em_segundos(entrada, valor):
    if entrada==2:
        min2seg=valor*60
        return min2seg
    elif entrada==3:
        hr2seg=valor*60**2
        return hr2seg
    

def converter_tempo(entrada, saida, valor_inicial):
    if entrada==saida:
        return valor_inicial
    if entrada!=1:
        valor=converter_em_segundos(entrada, valor_inicial)
        if saida==1:
            return valor
    else:
        valor=valor_inicial
    if saida==2:
        min=valor//60
        seg=valor%60
        return [int(min), int(seg)]
    if saida==3:
        hr=valor//3600
        resto_hr=valor%3600
        min=resto_hr//60
        seg=resto_hr%60
        return [int(hr), int(min), int(seg)]


unidades_tempo={
    1: "Segundos",
    2: "Minutos",
    3: "Horas"
}