# Função que cria um novo contato
def novoContato(contatos, nome, telefone='', email='', instagram=''):
    novo = [nome, [telefone], email, instagram]
    contatos.append(novo)
    return True

def atualizarContato(contato, indice, valor):
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

def buscarContato(contatos, busca):
    encontrados = []
    for contato in contatos:
        if(busca.upper() in contato[0].upper()):
            encontrados.append(contato)
    return encontrados


# Programa principal

contatos = []
print(novoContato(contatos, 'Samuel Cardoso da Costa', '21999844216', 'samuel.costa96@gmail.com', '@costa_samuka'))

print(atualizarContato(contatos[0], 0, 'Sammuel da Costa Cardoso'))
print(atualizarContato(contatos[0], 1, '21998258943'))
print(atualizarContato(contatos[0], 2, 'sammuel.costa96@gmail.com'))
print(atualizarContato(contatos[0], 3, 'costa.sammuka'))
#print(contatos)

print(atualizarContato(contatos[0], 1, '21998258943'))
#print(contatos)

print(atualizarContato(contatos[0], 4, 'sammuel96'))
#print(contatos)

print(novoContato(contatos, 'Bianca Pereira dos Santos', '84992746588', 'bia81pereira@outlook.com', '@b.iancasantox'))
#print(contatos)

print(buscarContato(contatos, 're'))