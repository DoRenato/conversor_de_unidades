def opcoes_selecao(tipo_opcao, dict_opcoes=None, tipo_conversao=None):
    conversoes={
        1:'Temperatura',
        2:'Distancia',
        3:'Peso',
        4:'Tempo',
        5:'Velocidade'
    }
    if tipo_opcao=='texto_valor':
        return 'Digite o valor a ser convertido: '
    opcao_numero=1
    texto=f'\nQual o/a {conversoes[tipo_conversao]} de {tipo_opcao}?\n'
    for key in dict_opcoes:
        texto+=f'    {key}) {dict_opcoes[key]}\n'
        opcao_numero+=1
    texto+='Digite apenas o valor correspondente: '
    return texto