#1
#Altera Frase
def altera_frase(frase, palavra, posicao):
     #Função que receba uma frase, uma palavra e uma posiçãoe retorne uma frase; string,int,string => string#
    frase = frase.split(' ')
    if(palavra in frase):
        indice = frase.index(palavra)
        frase[indice] = palavra.upper()
    else:
        frase.insert(posicao, palavra)

    frase = ' '.join(frase).lstrip()
    return frase


#2
#Falta Campeonato
def faltas(faltas_jogos):
    #A função deve retornar o total de faltas do campeonato. lista,String => int #
    faltas_totais = 0
    for jogo in faltas_jogos:
        faltas_totais += jogo[2][0] + jogo[2][1]
    return faltas_totais


#3
#Insere Ordenado
def insere(lista_numero, n):
    #Função que uma lista ordenada de números inteiros e um número inteiro n, inclua n na posição correta, ou seja, de tal maneira que a lista continue ordenada. lista(string) => lista#
    
    tamanho = len(lista_numero)
    
    if(n >= lista_numero[tamanho-1]):
        lista_numero.insert(tamanho, n)
    else:
        for i in range(0, len(lista_numero)):
            if(n <= lista_numero[i]):
                lista_numero.insert(i, n)
                break
    return lista_numero


#4
#Maiores
def maiores(lista, n):
    # dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n; list(int) => list #
    lista_maiores = []

    for i in lista:
        if(i > n):
            lista_maiores.append(i)

    lista_maiores.sort()

    return lista_maiores


#5
#Média da Turma
def media(lista):
    #retorne a média da turma e uma lista ordenada com as notas que ficaram acima da média; list => list#
    acima_media = []
    m = sum(lista)
    m = m / len(lista)

    for i in lista:
        if(i > m):
            acima_media.append(i)
    
    acima_media.sort()
    
    return m, acima_media


#6
#Ordenada?
def eh_ordenada(lista):
    #Se Função da lista está ordenada em ordem crescente, decrescente ou não ordenada.  lista => string , bolean #
    
    l = lista.copy()
    l.sort()

    if(l == lista):
        return (True, 'crescente')
    else:
        if(l[::-1] == lista):
            return (True, 'decrescente')
    
    return (False, 'desordenada')