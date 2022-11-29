'''
1 - Criar uma função recursiva (que retorne ela mesma) para armazenar N
termos da sequência de Fibonacci em uma lista. N é definido pelo usuário. Ao
encontrar os termos, imprimir a lista e finalizar a função.
'''

listaSF = []
stop = 0
def fibonacci(stop, a, b, aux):
    global listaSF #Variavel global dentro da função
    listaSF.append(a)
    a, b = b, a + b #acumula os valores para determinar os proximos numeros da sequencia
    #O proximo termo é sempre a soma dos dois termos anteriores
    aux +=1
    if stop == aux:
        print(listaSF)
        return 0
    else:
        return fibonacci(stop, a, b, aux) #chama a propria função até que stop == aux
    
while stop < 1:
    stop = int(input('Digite a quantidade de termos: '))


fibonacci(stop, a= 1, b= 1, aux= 0)

