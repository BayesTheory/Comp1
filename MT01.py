#Futebol OBI

def classificacao(Cv, Ce, Cs, Fv, Fe, Fs):
    Cp = (Cv * 3) + Ce
    Fp = (Fv * 3) + Fe
    
    if Cp > Fp:
        resultado = 'Cormengo'
    elif Fp > Cp:
        resultado = 'Flaminthians'
    elif Cp == Fp:
        if Cs > Fs:
            resultado = 'Cormengo'
        elif Fs > Cs:
            resultado = 'Flaminthians'
        elif Cs == Fs:
            resultado = 'Empate'
    return resultado
 
 
#Avião
   
def avioes(c, p_compr, p_compet):
      if (c * p_compet <= p_compr):
        return 'Suficiente'
      else :
        return 'Insuficiente'
  
  
#Positivo, Negativo ou Zero?
 
def PosNegZero(x):
    
    if(x > 0 ):
        
        return str( x ) +" e positivo"
    
    elif(x == 0) :
        
        return str( x ) +" e zero"
    
    else:
        return str( x ) +" e negativo" 
        