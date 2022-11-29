"""
Exercícios:
1) Foi realizada uma pesquisa de algumas características e gostos de quatro
habitantes incluindo: nome, sexo, esporte favorito (Natação, Futebol, Volêi,
Tênis) e idade. Com esses dados faça:
- Função que armazene os dados em uma lista. Dica: Use dicionários dentro da
lista.
- Calcule a idade média de homens que gostam de natação. Caso não haja
homens que gostam de natação chame uma função e imprima um aviso de que
não há homens que gostam de natação.

"""
def cadastro():
    list = []
    for i in range(4):
        dicionario = dict(nome = input('Digite seu nome: '), 
                        sexo = input('Digite M para masculino e F para feminino: '),
                        esporte = input('Escolha entre natação, futebol, voltei e tenis: '),
                        idade = int(input('Digite a sua idade: ')))
        
        list.append(dicionario)
    return list
    
def aviso():
    print('Não tem homens que gostam de natação')
    
lista = cadastro()
cont = 0
soma = 0

for i in range(4):
    if lista[i]['sexo'] == 'M' and lista[i]['esporte'] == 'natação':
        soma = soma + lista[i]['idade']
        
        cont += 1
if cont == 0:
    aviso()
else:
    media = soma / cont
    print(f'A idade media de homens que fazem natação é {media}')

