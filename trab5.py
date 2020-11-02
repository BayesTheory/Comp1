#;numero 1
def zodiaco(ano_nasc,):
  "Calcula e retorna a o nome do animal pela data de nascimento ; int -> str "
  animais = ['macaco', 'galo', 'cão', 'porco', 'rato', 'boi', 'tigre', 'coelho', 'dragão', 'serpente','cavalo', 'carneiro'] 
  x = (ano_nasc % 12) 
  return animais[x]
 

