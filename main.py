from temperaturas import (
    tipo_temp_atual_texto,
    tipo_temp_saida_texto,
    valor_temp_texto,
    converter_temperatura
)


bem_vindo_texto="""
Olá, seja bem-vindo ao Conversor de Unidades. Qual tipo de conversão você deseja fazer?
    1) Conversão de Temperaturas
    2) Conversão de Distancia
    3) Conversão de Peso
    4) Conversão de Tempo
    5) Conversão de Velocidade
    0) Fechar Programa
Escolha uma opção digitando o número correspondente: """

valor_invalido_texto="\n##### Valor informado invalido. #####"            


while True:
    unidade=int(input(f'{bem_vindo_texto}'))
    if unidade==1:
        tipos_temperaturas={
            1:"Celsius",
            2:"Fahrenheit",
            3:"Kelvin"
        }
        while True:
            try:
                tipo_temp_atual=int(input(f'{tipo_temp_atual_texto}'))
                if tipos_temperaturas.get(tipo_temp_atual):
                    break
            except ValueError:
                print(valor_invalido_texto)
                continue
            print(valor_invalido_texto)
        while True:
            try:
                tipo_temp_saida=int(input(f'{tipo_temp_saida_texto}'))
                if tipos_temperaturas.get(tipo_temp_saida):
                    break
            except ValueError:
                print(valor_invalido_texto)
                continue
            print(valor_invalido_texto)
        while True:
            try:
                valor_temp=float(input(f'{valor_temp_texto}'))
                break
            except ValueError:
                print("\n##### Entrada inválida! Por favor, insira um número inteiro ou decimal. #####")
        nova_temperatura=round(converter_temperatura(tipo_temp_atual, tipo_temp_saida, valor_temp),3)
        print(f"\n{valor_temp} {tipos_temperaturas[tipo_temp_atual]} = {nova_temperatura} {tipos_temperaturas[tipo_temp_saida]} ")
        
    elif unidade==0:
        break
    else:
        print("Valor Inválido, tente novamente.")