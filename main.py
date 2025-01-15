from temperaturas import (
    converter_temperatura, temp_entrada_texto, tipo_temp_saida_texto,
    valor_temp_texto, tipos_temperaturas
)

from distancias import(
    unidades_de_medida, unidade_entrada_texto, unidade_saida_texto,
    converter_unidade, unidade_valor_texto
)

from pesos import(
    unidades_pesos, peso_entrada_texto, peso_saida_texto,
    converter_peso, peso_valor_texto
)

# from tempo import(
#     unidades_tempo, tempo_entrada_texto, tempo_saida_texto,
#     converter_tempo, tempo_valor_texto
# )

# from velocidade import(
#     unidades_velocidade, unidade_entrada_texto, unidade_saida_texto,
#     converter_velocidade, unidade_valor_texto
# )


def menu_conversao(tipo_conversao, menu_dict, entrada_texto, saida_texto, valor_texto):
    valor_invalido_texto="\n##### Valor informado invalido. #####"  
    while True:
        try:
            entrada=int(input(f'{entrada_texto}'))
            if menu_dict.get(entrada):
                break
        except ValueError:
            print(valor_invalido_texto)
            continue
        print(valor_invalido_texto)
    while True:
        try:
            saida=int(input(f'{saida_texto}'))
            if menu_dict.get(saida):
                break
        except ValueError:
            print(valor_invalido_texto)
            continue
        print(valor_invalido_texto)
    while True:
        try:
            valor=float(input(f'{valor_texto}'))
            break
        except ValueError:
            print("\n##### Entrada inválida! Por favor, insira um número inteiro ou decimal. #####")
    if tipo_conversao==1:
        novo_valor=round(converter_temperatura(entrada, saida, valor),3)
        print(f"\n{valor} {menu_dict[entrada]} = {novo_valor} {menu_dict[saida]} ")
    if tipo_conversao==2:
        novo_valor=round(converter_unidade(entrada, saida, valor),3)
        print(f"\n{valor} {menu_dict[entrada]} = {novo_valor} {menu_dict[saida]} ")
    if tipo_conversao==3:
        novo_valor=round(converter_peso(entrada, saida, valor),3)
        print(f"\n{valor} {menu_dict[entrada]} = {novo_valor} {menu_dict[saida]} ")
    # if tipo_conversao==4:
    #     novo_valor=round(converter_tempo(entrada, saida, valor),3)
    #     print(f"\n{valor} {menu_dict[entrada]} = {novo_valor} {menu_dict[saida]} ")
    # if tipo_conversao==5:
    #     novo_valor=round(converter_velocidade(entrada, saida, valor),3)
    #     print(f"\n{valor} {menu_dict[entrada]} = {novo_valor} {menu_dict[saida]} ")


bem_vindo_texto="""
Olá, seja bem-vindo ao Conversor de Unidades. Qual tipo de conversão você deseja fazer?
    1) Conversão de Temperaturas
    2) Conversão de Distancia
    3) Conversão de Peso
    4) Conversão de Tempo
    5) Conversão de Velocidade
    0) Fechar Programa
Escolha uma opção digitando o número correspondente: """  

while True:
    tipo_conversao=int(input(f'{bem_vindo_texto}'))
    if tipo_conversao==1:
        nova_temperatura=menu_conversao(tipo_conversao, tipos_temperaturas, temp_entrada_texto, tipo_temp_saida_texto, valor_temp_texto)
    elif tipo_conversao==2:
        nova_distancia=menu_conversao(tipo_conversao, unidades_de_medida, unidade_entrada_texto, unidade_saida_texto, unidade_valor_texto)
    elif tipo_conversao==3:
        novo_peso=menu_conversao(tipo_conversao, unidades_pesos, peso_entrada_texto, peso_saida_texto, peso_valor_texto)      
    elif tipo_conversao==0:
        break
    else:
        print("Valor Inválido, tente novamente.")