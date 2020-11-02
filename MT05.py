#1
#Filtra múltiplos
def filtraMultiplos(multiplos, num):
    #função chamada filtraMultiplos para filtrar os múltiplos de um número n.; lista(int) => int#
    m = []
    for i in range(0, len(multiplos)):
        if(multiplos[i] % num == 0):
            m.append(multiplos[i])
        i=i+1
    return m


#2
#Consoantes Maiusculas
def uppCons(texto):
   #receba como entrada uma frase e retorne a frase com todas as suas consoantes em maiúsculas; String => String#
    i=0
    texto = list(texto)
    while i<len(texto):
        if texto[i].upper() in 'BHCDFGJKLMNPQRSTVWXYÇZ':
            texto[i] = texto[i].upper()
        i=i+1
    texto = ''.join(texto)
    return texto


#3
#Posição da Letra
def  posLetra(string, letra, n):
  # recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra; String => Int#
    pos = -1
    qtd = 0

    for i in range(len(string)):
        if(string[i] == letra):
            qtd = qtd + 1
            if(qtd == n):
                pos = i
                break

    return pos

#4
#Repetidos
def repetidos(lista):
    #Receba como entrada uma lista de números, e retorne o número de vezes que um elemento da lista é igual ao elemento anterior; Lista(int) => int#
    qtd_repetidos = 0

    for i in range(1, len(lista)):
        if(lista[i-1] == lista[i]):
            qtd_repetidos += 1

    return qtd_repetidos


#5
#Fatorial
def fatorial(num):
    #dado um número, calcule o fatorial deste número; Int => int#
    i = 1
    for num in range(2, num + 1):
        i = i * num
    return(i)


#6
#Peça perdida
def faltante(quebra_cabeca):
    #dada uma lista com N − 1 inteiros numerados de 1 a N, descubra qual número inteiro deste intervalo está faltando.lista(int) => int#
    n = len(quebra_cabeca) + 1
    faltando = n
    quebra_cabeca.sort()
    
    for i in range(1, n):
        if(quebra_cabeca[i-1] != i):
            faltando = i
            break    
    return faltando