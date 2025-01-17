from funcoes import opcoes_selecao
from temperaturas import converter_temperatura, tipos_temperaturas
from distancias import converter_unidade, unidades_de_medida
from pesos import converter_peso, unidades_pesos
from tempo import converter_tempo, unidades_tempo
# from velocidade import converter_velocidade, unidades_velocidade



def mostrar_resultado(tipo_conversao, menu_dict, un_entrada, un_saida, valor_incial, resultado):
    if tipo_conversao!=4:
        print(f"\n{valor_incial} {menu_dict[un_entrada]} = {resultado} {menu_dict[un_saida]}")
    else:
        if un_saida==2: # Minutos
            print(f"\n{valor_incial} {menu_dict[un_entrada]} = {resultado[0]}min {resultado[1]}seg ")
        if un_saida==3: # Horas
            print(f"\n{valor_incial} {menu_dict[un_entrada]} = {resultado[0]}h {resultado[1]}min {resultado[2]}seg")
    
    
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
            if tipo_conversao==4:
                valor=int(input(f'{valor_texto}'))
            else:
                valor=float(input(f'{valor_texto}'))
            break
        except ValueError:
            if tipo_conversao==4:
                print("\n##### Entrada inválida! Por favor, insira um número inteiro apenas. #####")
            else:
                print("\n##### Entrada inválida! Por favor, insira um número inteiro ou decimal. #####")
    if tipo_conversao==1:
        novo_valor=round(converter_temperatura(entrada, saida, valor),3)
        mostrar_resultado(tipo_conversao, menu_dict, entrada, saida, valor, novo_valor)
    if tipo_conversao==2:
        novo_valor=round(converter_unidade(entrada, saida, valor),3)
        mostrar_resultado(tipo_conversao, menu_dict, entrada, saida, valor, novo_valor)
    if tipo_conversao==3:
        novo_valor=round(converter_peso(entrada, saida, valor),3)
        mostrar_resultado(tipo_conversao, menu_dict, entrada, saida, valor, novo_valor)
    if tipo_conversao==4:
        novo_valor=converter_tempo(entrada, saida, valor)
        mostrar_resultado(tipo_conversao, menu_dict, entrada, saida, valor, novo_valor)
    # if tipo_conversao==5:
    #     novo_valor=round(converter_velocidade(entrada, saida, valor),3)
    #     mostrar_resultado(tipo_conversao, menu_dict, entrada, saida, valor, novo_valor)


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
    texto_valor=opcoes_selecao('texto_valor')
    if tipo_conversao==1:
        texto_entrada=opcoes_selecao('entrada',tipos_temperaturas,tipo_conversao)
        texto_saida=opcoes_selecao('saida', tipos_temperaturas,tipo_conversao)
        nova_temperatura=menu_conversao(tipo_conversao, tipos_temperaturas, texto_entrada, texto_saida, texto_valor)
    elif tipo_conversao==2:
        texto_entrada=opcoes_selecao('entrada',unidades_de_medida,tipo_conversao)
        texto_saida=opcoes_selecao('saida', unidades_de_medida,tipo_conversao)
        nova_distancia=menu_conversao(tipo_conversao, tipos_temperaturas, texto_entrada, texto_saida, texto_valor)
    elif tipo_conversao==3:
        texto_entrada=opcoes_selecao('entrada',unidades_pesos,tipo_conversao)
        texto_saida=opcoes_selecao('saida', unidades_pesos,tipo_conversao)
        novo_peso=menu_conversao(tipo_conversao, unidades_pesos, texto_entrada, texto_saida, texto_valor)
    elif tipo_conversao==4:
        texto_entrada=opcoes_selecao('entrada',unidades_tempo,tipo_conversao)
        texto_saida=opcoes_selecao('saida', unidades_tempo,tipo_conversao)
        novo_tempo=menu_conversao(tipo_conversao, unidades_tempo, texto_entrada, texto_saida, texto_valor)
    # elif tipo_conversao==5:
    #     texto_entrada=opcoes_selecao('entrada',unidades_velocidade,tipo_conversao)
    #     texto_saida=opcoes_selecao('saida', unidades_velocidade,tipo_conversao)
    #     nova_velocidade=menu_conversao(tipo_conversao, unidades_velocidade, texto_entrada, texto_saida, texto_valor)         
    elif tipo_conversao==0:
        break
    else:
        print("Valor Inválido, tente novamente.")