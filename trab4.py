#1
def SIGA(nome,n1,n2,n3):

	"Calcula e retorna a media das notas junto com o resultado e nome; int, int -> string"

  nf = (n1 + n2 + n3)/3

  if nf >= 7.0 :
    return  (nome, nf, 'Aprovado', 'parabens')
  elif nf >= 5.0:
    return (nome, nf, 'Aprovado')
  elif nf < 5.0:
    return (nome, nf, 'Reprovado')




#2
import math

def quadrante(angulos, graus):

	"Calcula o angulo e retorna o quadrante ; float, bolean -> int"

    if(graus == False):
        angulos = angulos * (math.pi / 180)

    if(angulos > 360):
        angulos = angulos - ((angulos//360) * 360)

    if (angulos <= 90):
        return 1
    elif (angulos <= 180):
        return 2
    elif (angulos <= 270):
        return 3
    elif (angulos < 360):
        return 4

