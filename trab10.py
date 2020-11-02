#1
def series_repetidas(lista_dados):
    x = 0
    anterior_igual = False
    
    for i in range(1, len(lista_dados)):
        if lista_dados[i-1] == lista_dados[i] and not anterior_igual:
            x += 1
            anterior_igual = True
        elif lista_dados[i-1] != lista_dados[i]:
            anterior_igual = False
        
    return x

lista = [4, 5, 4, 2, 1, 4, 4, 1, 1, 3, 5, 1, 2, 3, 1]
lista2 = [3, 5, 4, 3, 3, 1, 3, 1, 1, 1, 1, 2, 5, 1, 6]
print(series_repetidas(lista))



#2
def codigo1a4(i,a,b,c):

 if a > b :
   return "ERROR: B menor que A"
 
 elif i == 1:
   return ((a + b)* c) / 2
 
 elif i == 2:
   return a*a,b*b,c*c

 elif i == 3:
   return (a+b+c)/3

 elif i == 4:
    x = list(range(a, b, c))
    x = sum(x)
    return x

i = int(input('Diga o numero da função a ser executada: '))
a = int(input("Valor de A  "))
b = int(input("Valor de B "))
c = int(input("Valor de C "))
print(codigo1a4(i,a,b,c))

print(' Com I sendo :', i, ', A:', a, ', B:', b, 'e C', c, '\nResultando:', codigo1a4(i, a, b, c))



#3
def busca(setor, matriz):
    encontrados = []

    for i in range(len(matriz)):
        if (matriz[i][2] == setor):
            encontrados.append(matriz[i][0:2] + matriz[i][3:4])

    return encontrados

setor = str(input('Diga o Setor: '))
matriz = list(input("Diga a Matriz: "))

print(busca(setor, matriz))