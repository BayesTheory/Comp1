#1
#String recursiva
# str -> str
def recursiva(x):
    x = x
    s = len(x)//2
    return x[0:s] + x[:] + x[s:]



#2
#concatenação
# str, str -> str
def concatenacao(a , b):
    return a + b + b + a


#3
#Número de dias
# str, str -> int
def diff_datas(data1,data2):
    dia1 = int(data1[0:2])
    mes1 = int(data1[3:5])
    ano1 = int(data1[6:10])
    
    dia2 = int(data2[0:2])
    mes2 = int(data2[3:5])
    ano2 = int(data2[6:10])
    
    diatotal1 = dia1 + mes1 * 30 + ano1 * 365
    diatotal2 = dia2 + mes2 * 30 + ano2 * 365

    if diatotal1 > diatotal2:        
        return diatotal1 - diatotal2    
    elif diatotal1 < diatotal2:        
        return diatotal2 - diatotal1


#4
#Substituição
# string, int, int -> string
def substitui(s, x, i):
    s = list(s)
    s[i] = x
    s = ''.join(s)
    return s


#5
#Hashtag
# str-> str
def hashtag (x):
    x = x
    s = len(x)//2
    return '#' + x[0:s] + '#' + x[s:] + '#'


#6
#Filtragem
def filtra_pares(t):
    t = list(t)
    pares = []
    for i in t:
        if(i % 2 == 0):
            pares.append(i)
    return tuple(pares)


#7
#Detectando Colisões de Tuplas
def colisao(ret1, ret2):
    x = [[0,0],[0,0]]
    y = [[0,0],[0,0]]
    
    x[0][0], y[0][0], x[0][1], y[0][1] = ret1
    x[1][0], y[1][0], x[1][1], y[1][1] = ret2
    
    if (x[0][1] < x[1][0]) or (x[1][1] < x[0][0]) or (y[0][1] < y[1][0]) or (y[1][1] < y[0][0]) or (x[0][0] > x[1][1]) or (x[1][0] > x[0][1]) or (y[0][0] > y[1][1]) or (y[1][0] > y[0][1]):
        return False
    else:
        return True

