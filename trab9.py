#Import os. "Biblioteca"usada para arrumar a interface grafica porque sem fica torno
import os

def novoContato(contatos, nome, telefone='', email='', instagram=''):
#função cria um novo contato com suas respectivas informações; int,string => bolean
    novo = [nome, [telefone], email, instagram]
    contatos.append(novo)
    return True

def atualizarContato(contatos, indice, valor):
# Atualiza o contato das informações; int => bolean
    if(indice in [0, 2, 3]):
        contatos[indice] = valor
    elif(indice == 1):
        if(valor in contatos[1]):
            contatos[1].remove(valor)
        else:
            contatos[1].append(valor)
    else:
        return False

    return True

def buscarContato(contatos, busca):
#Bucas o contato das Informações; string => lista
    encontrados = []
    for contato in contatos:
        if(busca.upper() in contato[0].upper()):
            encontrados.append(contato)
    return encontrados

def quemLigou(contatos, numero):
  #Função busca pelo numero a informação de quem ligou; String => list
    pessoa = 'Contato não salvo'
    for contato in contatos:
        if(numero in contato[1]):
            pessoa = contato
            break
    return pessoa

def exibirContatos(contatos):
  #Exibe os contatos;    => List
    if(contatos == []):
        print('Lista de contatos vazia.')
    else:
        for i in range(0, len(contatos)):
            print(i+1, '-', contatos[i][0], contatos[i][1], contatos[i][2], contatos[i][3])


#PARTE VISUAL *ignore se desejar*
menu = """#------------------------------------------------------#
#         C O N T A T I N H O S A P P                  #
#------------------------------------------------------#
#  OPÇÕES                                              #
#  1 – EXIBIR LISTA DE CONTATOS                        #
#  2 – CADASTRAR NOVO CONTATO                          #
#  3 – ATUALIZAR CONTATO                               #
#  4 – BUSCAR CONTATO                                  #
#  5 – QUEM LIGOU?                                     #
#  6 – SAIR                                            #
#------------------------------------------------------#"""

contatos = []

while True:
    os.system('cls || clear')
    print(menu)
    opt = input('DIGITE A OPÇÃO DESEJADA (1 A 5): ')
    if(opt == '1'):
        print()
        exibirContatos(contatos)
        input('\nPressione uma tecla para continuar...')
    elif(opt == "2"):
        nome = input('\nDigite o nome: ')
        telefone = input('Digite o telefone/celular: ')
        email = input ('Digite o email: ')
        instagram = input ('Digite o Instagram: ')
        if (novoContato(contatos, nome, telefone, email, instagram)):
            input('\nCadastro realizado!\n\nPressione uma tecla para continuar...')
        else:
            input('\nNão foi possível criar o novo contato.\n\nPressione uma tecla para continuar...')
    elif(opt == '3'):
        exibirContatos(contatos)
        contato = int(input('\nDigite o ID do contato a ser atualizado: ')) - 1
        if(contato not in range(-len(contatos), len(contatos))):
            print('\nID digitado inválido')
        else:
            indice = int(input('Digite a informação que deseja atualizar (1 - Nome, 2 - Telefone, 3 - Email, 4 - Instagram): ')) - 1
            valor = input('Digite o valor da informação: ')
            if (atualizarContato(contatos[contato], indice, valor)):
                print('\nAtualização realizada!')
            else:
                print('Não foi possível atualizar o contato.')
        input('\nPressione uma tecla para continuar...')
    elif(opt == '4'):
        busca = input('\nDigite o nome do contato que deseja buscar: ')
        encontrados = buscarContato(contatos, busca)
        if(encontrados != []):
            print()
            exibirContatos(encontrados)
        else:
            print('\nNenhum contato encontrado.')
        input('\nPressione uma tecla para continuar...')
    elif(opt == '5'):
        numero = input('\nDigite o número: ')
        print('\n', quemLigou(contatos, numero), end='')
        input('\n, Pressione uma tecla para continuar...')
    elif(opt == '6'):
        break
# Deu trabalho mas gostei do resultado na parte grafica
