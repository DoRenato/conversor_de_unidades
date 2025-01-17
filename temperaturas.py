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
            fahrenheit=valor*(9/5)+32
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


tipos_temperaturas={
    1:"Celsius",
    2:"Fahrenheit",
    3:"Kelvin"
}