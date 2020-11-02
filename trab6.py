def novoContato(nome, telefone='', email='', instagram=''):
     '''Cria uma lista com informações;  string, string, string, string -> list'''
    return [nome, [telefone], email, instagram]

def atualizarContato(contato, indice, valor):
    '''Atualiza as informçãoes da lista;  list, int, string -> boolean'''
    if(indice in [0, 2, 3]):
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