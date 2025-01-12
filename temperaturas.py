tipo_temp_atual_texto="""
Qual o tipo de temperatura de origem?
    1) Celsius
    2) Fahrenheit
    3) Kelvin
Digite apenas o número correspondente: """
tipo_temp_saida_texto="""
Agora qual o tipo de temperatura que você busca?
    1) Celsius
    2) Fahrenheit
    3) Kelvin
Digite apenas o número correspondente: """
valor_temp_texto="""
Informe o valor da temperatura (Apenas o numero inteiro ou decimal): """


def validar_tipo_temp(tipo: int) -> bool:
    return 1 <= tipo <= 3 # Valida se o tipo de temperatura está entre 1 e 3.

def converter_temperatura(temp_atual, temp_saida, valor):
    #1 Celsius
    #2 Fahrenheit
    #3 Kelvin
    fahrenheit_para_celsius=(valor-32)*(5/9)
    kelvin_para_celsius=valor-273.15
    if temp_atual==temp_saida:
        return valor
    elif temp_atual==1:
        if temp_saida==2:
            fahrenheit=valor*(5/9)+32
            return fahrenheit
        else:
            kelvin=valor+273.15
            return kelvin
    elif temp_atual==2:
        if temp_saida==1:
            return fahrenheit_para_celsius
        else:
            kelvin=fahrenheit_para_celsius+273.15
            return kelvin
    elif temp_atual==3:
        if temp_saida==1:
            return kelvin_para_celsius
        else:
            fahrenheit=kelvin_para_celsius*(9/5)+32
            return fahrenheit