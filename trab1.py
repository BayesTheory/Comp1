
#1 Base do Retangulo

def area(x,y):
	"""calcula a area do retangulo"""
	return y*x

print(area(5,7))
print(area(15,2))
print(area(500,700))
print(area(5,0))



#2 Base do Quadrado pela Aresta

def base(x):
	"""calcula a base do quadrado"""
	return (x * x) * 6



#3 Area da Coroa Circular

def area(r1,r2):
	"""calcula a area da Coroa"""
	return 3.14 * (r1 * r1 - (r2 * r2))

print(area(2,1))
print(area(15,5))
print(area(100,0))



#4 Media de dois numeros

def area(a1,a2):
	"""calcula a media dos numeros"""
	return a1 + a2 /2

a2	= float
a1	= float
print(area(-5,7))
print(area(2,-2))
print(area(5,5))
print(area(3.0,4.0))
print(area(3,4))



#5 Calculo a Abcissa  da equação

def area(a,b,c,x):
	"""calcula a Abcissa  da equação"""
	return a * x * x + b * x + c

a = int(input("A da sua função : "))
b = int(input("B da sua função : "))
c = int(input("C da sua função : "))
x = int(input("abcissa para obter a odenada correspondente : "))
print(area(a,b,c,x))



#6 Media ponderada 

def media(a1,b1,c1,d1):
	"""calcular a media ponderada dos Bimestres de uma escola valendo em ordem respectivamente (1,2,3,4)"""
	return ((a1 * 1) + (b1 * 2 ) + (c1 * 3) + (d1 * 4)) / (1+2+3+4)

a1 = float(input("Nota 1 Bimestre : "))
b1 = float(input("Nota 2 Bimestre : "))
c1 = float(input("Nota 3 Bimestre : "))
d1 = float(input("Nota 4 Bimestre : "))
print(media(a1,b1,c1,d1))



#7 PG Soma

def PG(q):
	"""PG soma : A soma de PG e 1/(1 − q) q  ́e a razao e 0 ≤ q < 1."""
	return (1 / q - 1) 
	"""Pode ser q esteja errada :/ """



#8 Conta com 10% do garçom

def conta(a1):
	"""calcula a Abcissa  da equação"""
	return ((a1 * 0.1)+ a1)
print(conta(100))



#9 Valor da conta de um restaurante e a porcentagem exigida

def conta(a1,a2):
	"""Calcula o Valor da conta de um restaurante e a porcentagem exigida pelo usuario"""
	return ((a1 * a2)+ a1)
a1 = float(input("Valor da conta"))
a2 = float(input("Porcentagem da gorjeta (VALORES COMO 0.1 PARA 10% OU 0.5 PARA 50%)"))
print(conta(a1,a2))




#10 Saldo inicial, o numero de meses e taxa de juros mensal

def conta(si,ju,me):
	"""Calculador de Juros dados pelo usuario"""
	return (si * (1 + ju * me) )
si = float(input("Saldo inicial : "))
ju = float(input("Juros : "))
me = float(input("(VALORES COMO 0.1 PARA 10% OU 0.5 PARA 50%) Meses : "))
print(conta(si,ju,me))



#11 distancia da conrrenteza
def conta(velco,velbar,lario):
	"""Calculador da correnteza"""
	return velco * (lario / velco)















