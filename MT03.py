
#1
#Quantidade de Palavras
def quant_palavras(frase):
    """Dada uma frase, retorne o número de palavras da frase;; Str -> int """
    return len(frase.split(" "))


#2
#Conta Frases
def conta_frases(frases):
    
    """Dada varias frases, retorne o número de frases dos textos;; Str -> int """
    
    frases=frases.replace('!', '.')
    
    frases=frases.replace('?', '.')    
    
    frases=frases.replace('…', '.')
    
    return (len(frases.split('. ')))


#3
#Intercalando Listas
def intercala(lista1, lista2):
    """Função gera uma lista L3 que é formada intercalando os elementos de L1 e L2. string => String"""
    n = len(lista1)
    lista3 = []
    
    for i in range(n):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    
    return lista3


#4
#Retira Pontuação
def retira_pontuacao(frase):
    """ Função que dada uma frase, retorne a frase sem pontuação  string => string"""
    frase = frase.replace("-", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    return frase


#5
# De Frente para Trás
def retira_pontuacao(frase):
    """Função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.string => string"""
    frase = frase.replace("-", " ")
    frase = frase.replace("!", "")
    frase = frase.replace(",", "")
    frase = frase.replace(".", "")
    frase = frase.replace("?", "")
    frase = frase.replace(":", "")
    frase = frase.replace(";", "")
    return frase

def inverte(frase):
    frase = frase.lower()
    frase = retira_pontuacao(frase)
    frase = frase.split(" ")
    frase = frase[::-1]
    frase = ' '.join(frase)
    return frase



#6
#Pirâmide de Números
def piramide_num(base, topo):
    """ Construa uma Função de uma pirâmide de números inteiros, dados dois números ; Int Int => string"""
    piramide = [] 
    passo = 1
    
    if base > topo:
        passo = -1
        
    piramide = str(list(range(base, topo, passo)) + list(range(topo, base - passo, 0 - passo)))

    return piramide

 #7
 #Colchão
 def colchao(medidas,H,L):
    "medidas é uma lista com os tamanhos inteiros A, B e C, e H e L são os tamanhos inteiros da altura e largura da porta; int,int,int,int,int => Bolean"
    medidas.sort()
    porta = [H, L]
    porta.sort()

    if(medidas[0] <= porta[0] and medidas[1] <= porta[1]):
        return 'True'
    else:
        return 'False'