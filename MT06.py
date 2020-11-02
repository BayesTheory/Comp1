#1
#Soma de Numeros Impares
def soma_impar(n):
    #função que retorne a soma dos n primeiros números ímpares, onde n é um inteiro passado como parâmetro: int => int#
    soma = 0
    for i in range(1, n*2+1, 2):
        soma += i
    return soma



#2
#Soma Fatorial
def soma_fatorial():
    #função que calcule a soma dos fatoriais dos números inteiros de 1 a 10.:   => Int#
    soma_f = 0
    for i in range(1, 11):
        f = 1
        for j in range(1, i+1):
            f = f*j
        soma_f += f
    
    return soma_f


#3
#Divisores
def divisores(n):
	#Função que conte quantos divisores um número tem. Este número será passado como entrada.
    cont_div = 0
    for i in range(1, n+1):
        if(n % i == 0):
            cont_div += 1
    
    return cont_div


#4
#Números primos
def primo(num):
	#Função que dado um número inteiro positivo, verifique se este número é primo ou não. 
    p = True
    for i in range(2, num//2):
        if (num % i == 0):
            p = False
            break

    return p


#5
#Soma H
def soma_h(n):
	#Faça uma função chamada **soma_h** para calcular e retornar o valor H com N termos onde N é inteiro e dado com entrada.
    soma = 0
    for i in range(1,n+1):
        soma += 1/i
    soma = round(soma, 2)

    return soma


#6
#Soma Esquesita
def soma():
    soma_f = 0
    for i in range(1, 11):
        f = 1
        for j in range(1, i+1):
            f = f*j
        if(i % 2 == 0):
            soma_f -= (11-i)/f
        else:
            soma_f += (11-i)/f
    soma_f = round(soma_f, 2)

    return soma_f


#7
#Lingua do P
def lingua_p(palavra):
    #receba como parâmetro uma palavra (em português) e retorne esta mesma palavra traduzida: sring => string#
    d = 1
    palavra = palavra.lower()
    palavra_p = list(palavra)
    for i in range(0, len(palavra)):
        if((palavra[i] not in 'bcdfghjklmnpqrstvwxyz')):
            palavra_p.insert(i+d, 'p'+palavra[i])
            d += 1
    palavra_p = ''.join(palavra_p)
    return palavra_p
