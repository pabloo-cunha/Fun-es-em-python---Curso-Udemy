"""
Funções sem paramentros
"""
"""
O que são Funções?
- São blocos de código que irão executar uma tarefa especifica, podendo ser reutilizavel.
- Tem por papel organizar, diminuir seu programa e facilitar alteração e gerenciamento.
- São declaradas após os comentários iniciais e imports(se houver)
- Já estudamos algumas funções:
a)print()
b)input()
c)type()

como declarar?
def nome(parametros ou não):
    #Processo

Nessa aula, vamos focar em sem parametros:
def nome():
    #Processo
    
#Sempre faça o nome da função começar com letras minusculas e se for nome compos, separe por underline(_)
Ex.:
a)
def test_phrase():
    print('Estou na função')
    
test_phrase() #Sempre com parenteses!

b)Posso chamar a função onde eu quiser
def test_phrase():
    print('Estou na função')
    
for i in range(0,3):
    test_phrase()
    
Obs: Podemos criar uma variavel tipo função

def test_phrase():
    print('Estou na função')
    
frase = test_phrase #Na variavel a função não recebe ()
print(type(frase))
frase()
#Quando utiliza parenteses, chama a execução da função, sem parentes chama apenas o objeto função.

Há duas classificações em funções:
1) Função com retorno e sem retorno:
- O retorno é utilizado para justamente retornar alguma operação/variavel de dentro da função
- Para isso utiliza-se a palavra para return
- Podemos ter mais de um return na função
Ex:
#Função SEM RETORNO:
def operacao():
    contador = 60 #Isso é uma variavel Local
    contador += 2
    print(f'Contador = {contador}')
    
operacao() #Quando não há return dentro da função retorna None

#Função com Retorno
def operacao():
    contador = 60 #Isso é uma variavel Local
    contador += 2
    print(f'Contador = {contador}')
    return 
    
print(operacao()) #Agora o valor retornado foi de 62
Obs.: Assim que a função reconhece a palavra return, ela finaliza automaticamente 
def operacao():
    contador = 59 #Isso é uma variavel Local
    if contador < 60:
        contador += 2
        return contador
    print(f'Contador = {contador}')
    return contador
    
print(operacao()) #Agora o valor retornado foi de 62

2)Funções recursivas e não recursivas:
O que é recursividade?
- Aquilo que se repete indefinidamente. Em programação, uma função recursiva é aquele que retorna ela mesmo.

#Função Não Recursiva (Não retorna ela mesmo, executada apenas 1 vez)
Ex:
def celsiu_kelvin():
    celsius = int(input('Digite o valor em Cersius: '))
    kelvin = celsius + 273
    return kelvin

print(celsiu_kelvin())

#Função Recursiva
def celsiu_kelvin():
    celsius = int(input('Digite o valor em Cersius: '))
    kelvin = celsius + 273
    print(f'Kevin: {kelvin}')
    sair = input('Deseja sair? ')
    if sair == 'sim':
        return 'acabou!'
    else:
        return(celsiu_kelvin())
  
print(celsiu_kelvin())

Obs.: Lembre-se SEMPRE de uma condição de parada na recursividade. Caso contratio, cairá em um loop infinito.
Vantagem de usar recursão: Torna o codigo mais limpo e gera sequencia facilmente.
Desvantagem de usar recursão: A logica pode ser mais complexa e tambem usar mais memoria.


"""
def celsiu_kelvin():
    celsius = int(input('Digite o valor em Cersius: '))
    kelvin = celsius + 273
    print(f'Kevin: {kelvin}')
    sair = input('Deseja sair? ')
    if sair == 'sim':
        return 'acabou!'
    else:
        return(celsiu_kelvin())
  
print(celsiu_kelvin())

    