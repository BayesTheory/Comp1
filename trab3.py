
#numero 1

def absoluto(x):
'''Calcula e retorna o valor absoluto de x por x(não negativo);  int -> int'''
    if x<0:
        return -x
    return x




#numero 2
import math
'''Calcula e retorna raizes com a, b ,c (0,1,2);  float,float,float -> float'''
def equacoes(a,b,c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return "nenhuma raiz"
    elif delta == 0:
        return "Uma raiz" ((-b) / (2*a))
    else:
        rdelta = math.sqrt(delta)
        return "Duas raizes" ((-b + rdelta)/(2*a),(-b-rdelta)/(2*a))

a = 2
b = 4
c = -12

print(equacoes(a,b,c))



#numero 3
'''Calcula e retorna uma mensagem n vezes;  int -> string'''
import math

def vezes(n):
  return (n * " Feliz aniversario!! ")
n = 5
print(vezes(n))




#numero 4
''' Retorna string de uma data DD/MM/AAAA;  string -> string'''

a = str(input("DIA : "))
b = str(input("MÊS : "))
c = str(input("ANO : "))

def data(a,b,c):
  return 

print(a ,"/", b ,"/" ,c  )




#numero 5
'''Calcula e retorna funções  ((0 a 2) de (2 a 3.5) de (3.5 a 5) de 5....);  float,float,float -> float'''

def funcao(y):
    if y < 2:
        return y
    
    elif y >2 and y <=3.5:
        return 2
    
    elif y >3.5 and y <=5:
        return 3
    
    else:
        return ((y*y - 10*y) + 28)


y = 6
print(funcao(y))






#numero 6
'''Calcula e retorna salario com desconto do INSS  e IR;  int -> int'''

def inss(salario):
    if salario <= 2000:
        return salario * 0.05
    
    elif  salario > 2000 and  salario <=3000:
        return salario * 0.08

    elif  salario > 3000:
        return salario * 0.1

def ir(salario):
    if  salario <= 2500:
        return salario * 0.11
    
    elif  salario > 2500 and  salario <=5000:
        return salario * 0.15

    elif  salario > 5000:
        return salario * 0.22
    

def somadesc(salario):
    return salario -  ( ir(salario) + inss(salario)) 
    
salario = 5000

print(somadesc(salario))