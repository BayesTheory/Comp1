#1
#Matriz Quadrada
def ehquadrada(matriz):
    #Função para identificar se uma matriz é quadrada; List => Bolean
    for i in range(len(matriz)):
        if len (matriz[i]) != len(matriz):
            return False
    return True


#2
#Buscando na Matriz
def conta_numero(numero, matriz):
    #Função retorna quantas vezes aquele número aparece na matriz; Int,List =>int
    quantidade = 0
    for i in range(len(matriz)):
         quantidade += matriz[i].count(numero)
    return quantidade


#3
#Média da Matriz
def media(matriz):
    #Retorne seu resultado com somente duas casa decimais; List => Float
    quantidade = 0
    soma = 0
    for i in range(len(matriz)):
        quantidade += len(matriz[i])
        soma += sum(matriz[i])
        
    media = soma / quantidade
    media = round(media, 2)
    
    return media


#4
#Melhor Volta
def melhor_volta(corrida):
    #função deve retornar uma tupla informando De quem foi a melhor volta da prova, com qual tempo e em que volta; Lista => tupla
    corredor = 0
    melhor_volta = corrida[0].index(min(corrida[0]))

    for i in range(1, len(corrida)):
        v = min(corrida[i])
        if (v < corrida[corredor][melhor_volta]):
            corredor = i
            melhor_volta = corrida[i].index(v)
    return (corredor+1, corrida[corredor][melhor_volta], melhor_volta+1)


#5
#Busca de Funcionarios
def busca(setor, matriz):
    #função chamada busca que receba uma matriz etorna os dados de todos os funcionários; List => list
    encontrados = []

    for i in range(len(matriz)):
        if (matriz[i][2] == setor):
            encontrados.append(matriz[i][0:2] + matriz[i][3:4])

    return encontrados



#6
#Algoritmo de Busca
def  insercao(lista):  
    #Recebe uma lista como entrada e retorna essa lista ordenada pelo método de inserção; list => List
    for i in range(1, len(lista)): 
        x = lista[i] 
        j = i-1
        while j >=0 and x < lista[j] : 
                lista[j+1] = lista[j] 
                j -= 1
        lista[j+1] = x