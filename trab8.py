#1
import math

def soma(n):
    #funçao que, dado n, calcule a soma da s ́erie at ́e o termo n. Float => Float
    s = 0
    for i in range(0, n):
        s += ((-1)**i)/(2*i+1)

    return s

def letra_b():
    #Função que calcule a soma desta serie de modo que |sn−pi/4| < 0, 01. Float => tupla
    x = math.pi/4
    erro = 1
    i = 0
    s = 0
    while (erro >= 0.01):
        i += 1
        s = soma(i)
        erro = math.fabs(s - x)
    return (i, s)


#2

def novoContato(contatos, nome, telefone='', email='', instagram=''):
#função cria um novo contato com suas respectivas informações; int,string => bolean
    novo = [nome, [telefone], email, instagram]
    contatos.append(novo)
    return True

def atualizarContato(contato, indice, valor):
# Atualiza o contato das informações; int => bolean
    if(indice in [0, 2, 3]):
        contato[indice] = valor
    elif(indice == 1):
        if(valor in contato[1]):
            contato[1].remove(valor)
        else:
            contato[1].append(valor)
    else:
        return False

    return True

def buscarContato(contatos, busca):
#Bucas o contato das Informações; string => lista
    encontrados = []
    for contato in contatos:
        if(busca.upper() in contato[0].upper()):
            encontrados.append(contato)
    return encontrados