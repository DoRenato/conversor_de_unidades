from temperaturas import (
    converter_temperatura, temp_entrada_texto, tipo_temp_saida_texto,
    valor_temp_texto, tipos_temperaturas
)

from distancias import(
    unidades_de_medida, unidade_entrada_texto, unidade_saida_texto,
    converter_unidade
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
        while True:
            try:
                temp_entrada=int(input(f'{temp_entrada_texto}'))
                if tipos_temperaturas.get(temp_entrada):
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
        nova_temperatura=round(converter_temperatura(temp_entrada, tipo_temp_saida, valor_temp),3)
        print(f"\n{valor_temp} {tipos_temperaturas[temp_entrada]} = {nova_temperatura} {tipos_temperaturas[tipo_temp_saida]} ")
    
    elif unidade==2:
        while True:
            try:
                unidade_entrada=int(input(f'{unidade_entrada_texto}'))
                if unidades_de_medida.get(unidade_entrada):
                    break
            except ValueError:
                print(valor_invalido_texto)
                continue
            print(valor_invalido_texto)
        while True:
            try:
                unidade_saida=int(input(f'{unidade_saida_texto}'))
                if unidades_de_medida.get(unidade_saida):
                    break
            except ValueError:
                print(valor_invalido_texto)
                continue
            print(valor_invalido_texto)
        while True:
            try:
                valor_unidade=float(input('Digite o valor a ser convertido: '))
                break
            except ValueError:
                print("\n##### Entrada inválida! Por favor, insira um número inteiro ou decimal. #####")
        nova_distancia=round(converter_unidade(unidade_entrada, unidade_saida, valor_unidade),3)
        print(f"\n{valor_unidade} {unidades_de_medida[unidade_entrada]} = {nova_distancia} {unidades_de_medida[unidade_saida]} ")
        
    elif unidade==0:
        break
    else:
        print("Valor Inválido, tente novamente.")