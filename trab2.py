#numero1

def media(a , b, c):
	"""media"""
    return (a + b + c) / 3


def media_maior(a, b, c):
	"""maior numero - media"""
    maior = a
    if(maior < b):
        maior = b
    if(maior < c):
        maior = c
    return maior - media(a, b, c)


def media_menor(a, b, c):
	"""menor numero  + media"""
    menor = a
    if(menor > b):
        menor = b
    if(menor > c):
        menor = c
    return menor + media(a, b, c)





#numero 2

def delta(a , b, c ,):
	"""delta equação de segundo grau"""
    return b * b - 4 * a * c

def soma( a , b , c):
	"""raiz da soma"""
    return (- b + ((delta(a , b, c,)) ** (1/2))) / (2 * a)

def sub(a , b, c,):
	"""raiz da subração"""
   return (- b - ((delta(a , b, c,)) ** (1/2))) / (2 * a)





#numero 3 
def n_pa(a_1, a_n, r):
	"""numero de termos"""
    return ((a_n - a_1) / r) + 1

def soma_pa(a_1, a_n, n):
	"""soma da PA"""
    return ((a_1 + a_n) * n) / 2

a_1 = 2
a_n = 4
r = 2

n = n_pa(a_1, a_n, r)
soma = soma_pa(a_1, a_n, n)

print('A soma da PA é:', soma)




#4
def base(r):
	"""base do cilindro"""
	return 3.14 * (r * r)

def arealateral(r,h):
	"""area lateral do cilindro"""
    return  2 * 3.14 * (r * h)

def areatotal(r,h):
	"""area total"""
   return 2 * base(r) + arealateral(r,h)




#5
import math

def triangulo(c1, c2,):
	"""hipotenusa"""
    return math.sqrt(c1*c1 + c2*c2)

def distancia(x1, x2 ,y1 ,y2 ):
	"""distancia de coordenadas"""
    return math.sqrt((x1-x2)**2) + ((y1-y2)**2)

def perimetro(c1,c2):
	"""perimetro do triangulo"""
   return  triangulo(c1,c2) + c1 + c2 

def quadrado(q1,q2):
	"""quadrado do seno e cosseno"""
    return  math.sin(math.pow(q1 , 2)) + math.cos(math.pow(q2 , 2)) 

def circulo(c):
	"""circuferencia"""
    return math.pi * 2 * c 

c1 = 2
c2 = 4
print(triangulo(c1, c2,))
print(perimetro(c1, c2,))

c = 3
print(circulo(c))

q1 = 60
q2= 90
print(quadrado(q1,q2))

x1 = 2
x2 = 10
y1 = 5
y2 = 7
print(distancia(x1, x2 ,y1 ,y2 ))


#6
import math

def areasetor(r, a = 360):
	"""́Area de um setor circular ou Area do circulo inteiro"""
    return (a * r * r * math.pi)/360
#6.1
import math

def areasetor(r, a = None):
	"""́Area de um setor circular ou Area do circulo inteiro.2"""
    if a == None:
        return (r * r * math.pi)
    return (a * r * r * math.pi)/360




#7
def troco(dinheiro ,preço):
	"""Quanto ganha de troco"""
    return (dinheiro % preço)

dinheiro = 20
preço = 11

print(troco(dinheiro ,preço))

#7b

def imc(peso ,altura):
	"""IMC"""
    return peso / (altura * altura)

peso = 125
altura = 195

print(imc(peso ,altura))

#7c
import math

def a(x): 
"""Passageiros maximo de um carro"""  
 return math.ceil(x / 5)

x = float(input("Passageiros : "))
print(a(x))




#8
import math

def circulo(c):
	"""Circuferencia"""
    return math.pi * 2 * c 

def corrida(c , x) :
	"""Circuferencia dividido pelas voltas"""
	return circulo(c) * x

c = 20
x = 8

print( circulo(c))
print(corrida(c , x))




#9
import math

def bolo(a_xicara,b_ovos,c_colher):
"""2 xıcaras 3 ovos e 5 colheres """
    return math.ceil(a_xicara / 2) 
    math.ceil(b_ovos / 5)
    math.ceil(c_colher/ 3) 

a_xicara = float(input("Xicaras : "))
b_ovos = float(input("Ovos: "))
c_colher = float(input("Colheres de Leite : "))

print(bolo(a_xicara,b_ovos,c_colher))


#Otima lista professor :)