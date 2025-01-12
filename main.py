from funcoes import converter_temperatura

bem_vindo_texto="""
Olá, seja bem-vindo ao Conversor de Unidades. Qual tipo de conversão você deseja fazer?
    1) Conversão de Temperaturas
    2) Conversão de Distancia
    3) Conversão de Peso
    4) Conversão de Tempo
    5) Conversão de Velocidade
    0) Fechar Programa
Escolha uma opção digitando o número correspondente: """

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
                print("\n##### Valor informado invalido. #####")
                continue
            print("\n##### Valor informado invalido. #####")
        while True:
            try:
                tipo_temp_saida=int(input(f'{tipo_temp_saida_texto}'))
                if tipos_temperaturas.get(tipo_temp_saida):
                    break
            except ValueError:
                print("\n##### Valor informado invalido. #####")
                continue
            print("\n##### Valor informado invalido. #####")
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