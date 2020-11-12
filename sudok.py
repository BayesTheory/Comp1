#Import os usado para deixar a parte visual melhor
import os

# Funções
def validar_celula(grade, linha, coluna):
  #Função que verifica a celula list, int, int -> bool
    if grade[linha][coluna] != 0:
        return False
    return True


def validar_linha(grade, linha, valor):
  #Função verifica a Linha; int, list -> bool
    if valor in grade[linha]:
        return False
    return True

    
def validar_coluna(grade, coluna, valor):
    #Função verifica a coluna ; list,int,int -> Bool
    for i in range(0, 9):
        if grade[i][coluna] == valor:
            return False
    return True

    
def validar_sub_grade(grade, linha, coluna, valor):
  #Função verifica a subgrade; int,int,int,list -> bool
    linha_inicio_grade = (linha // 3) * 3
    coluna_inicio_grade = (coluna // 3) * 3
    for i in range(linha_inicio_grade, linha_inicio_grade+3):
        for j in range(coluna_inicio_grade, coluna_inicio_grade+3):
            if grade[i][j] == valor:
                return False
    return True


def inserir_valor_grade(grade, linha, coluna, valor):
  #Função verifica usando a funçoes acima linha,coluna,grade e subgrade para o jogo funcionar corretamente; int, int,list, int -> bool
    if not validar_celula(grade, linha, coluna):
        print('\nCélula já preenchida.')
        return False
    if not validar_linha(grade, linha, valor):
        print('\nA linha já possui um valor igual.')
        return False
    if not validar_coluna(grade, coluna, valor):
        print('\nA coluna já possui um valor igual.')
        return False
    if not validar_sub_grade(grade, linha, coluna, valor):
        print('\nA sub-grade já possui um valor igual.')
        return False
    grade[linha][coluna] = valor
    return True


def verificar_vitoria(grade):
  #Função verifica se o usuario conseguiu ganhar o game; list -> Str
    vitoria = True
    for i in range(0, 9):
        if 0 in grade[i]:
            vitoria = False
            break
    return vitoria

    
def exibir_grade(grade):
  #Função usada para exibir a grade; list -> none
    print('     1 2 3   4 5 6   7 8 9')
    print('   ┍-----------------------┑')
    for i in range(0, 9):
        print(i+1, ' | ', end='')
        for j in range(0, 9):
            if grade[i][j] != 0:
                print(grade[i][j], end=' ')
            else:
                print('_', end=' ')
            if (j+1) % 3 == 0:
                print('| ', end='')
        print()
        if (i+1) % 3 == 0 and i < 8:
            print('   |-------+-------+-------|')
    print('   ┕-----------------------┙')  
    

def exibir_menu_principal():
  #Função usada para exibir o menu principal; list -> none
    print('==== Jogo Sudoku ====')
    print('\n1 - Novo Jogo')
    print('2 - Sair')
    

def iniciar_jogo(grade):
  #Função usada para iniciar o jogo; list -> none
    while True:
        os.system('cls || clear') # Limpar a tela
        print('==== Jogo Sudoku ====')
        print('\nSe quiser desistir e/ou iniciar um novo jogo, digite -1 no campo da linha.\n')
        exibir_grade(grade)
        print('\nInforme a posição e o valor para inserir na grade acima.')
        linha = int(input('\nDigite o número da linha: ')) - 1
        if linha == -2:
            break
        coluna = int(input('Digite o número da coluna: ')) - 1
        valor = int(input('Digite o valor de 1 a 9: '))
        if inserir_valor_grade(grade, linha, coluna, valor):
            print('\nValor inserido com sucesso.')
        if verificar_vitoria(grade):
            input('\nParabéns! Você venceu. Pressione ENTER para continuar...')
            break
        input('\nPressione ENTER para continuar...')

    return

def copia_grade(grade):
#Função usada para copiar uma grade(está assim com for pois usando somente copy estava copiando ainda as referencias dentro da subgrade) list -> list
    g = []
    for i in range(0, 9):
        g.append(list.copy(grade[i]))
    return g
    
def funcao_teste():
#Função serve para armazenar as respostas da grade2 ou seja para teste; none -> none
    grade2 = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
    grade = copia_grade(grade2)
    inserir_valor_grade(grade, 0, 2, 4)
    inserir_valor_grade(grade, 0, 3, 6)
    inserir_valor_grade(grade, 0, 5, 8)
    inserir_valor_grade(grade, 0, 6, 9)
    inserir_valor_grade(grade, 0, 7, 1)
    inserir_valor_grade(grade, 0, 8, 2)
    inserir_valor_grade(grade, 1, 1, 7)                 
    inserir_valor_grade(grade, 1, 2, 2)
    inserir_valor_grade(grade, 1, 6, 3)
    inserir_valor_grade(grade, 1, 7, 4)
    inserir_valor_grade(grade, 1, 8, 8)
    inserir_valor_grade(grade, 2, 0, 1)
    inserir_valor_grade(grade, 2, 3, 3)
    inserir_valor_grade(grade, 2, 4, 4)   
    inserir_valor_grade(grade, 2, 5, 2)                 
    inserir_valor_grade(grade, 2, 6, 5)
    inserir_valor_grade(grade, 2, 8, 7)
    inserir_valor_grade(grade, 3, 1, 5)
    inserir_valor_grade(grade, 3, 2, 9)   
    inserir_valor_grade(grade, 3, 3, 7)   
    inserir_valor_grade(grade, 3, 5, 1)                 
    inserir_valor_grade(grade, 3, 6, 4)
    inserir_valor_grade(grade, 3, 7, 2)
    inserir_valor_grade(grade, 4, 1, 2)
    inserir_valor_grade(grade, 4, 2, 6)
    inserir_valor_grade(grade, 4, 4, 5)     
    inserir_valor_grade(grade, 4, 6, 7)                 
    inserir_valor_grade(grade, 4, 7, 9)
    inserir_valor_grade(grade, 5, 1, 1)
    inserir_valor_grade(grade, 5, 2, 3)
    inserir_valor_grade(grade, 5, 3, 9)
    inserir_valor_grade(grade, 5, 5, 4)                 
    inserir_valor_grade(grade, 5, 6, 8)
    inserir_valor_grade(grade, 5, 7, 5)
    inserir_valor_grade(grade, 6, 0, 9)
    inserir_valor_grade(grade, 6, 2, 1)  
    inserir_valor_grade(grade, 6, 3, 5)                 
    inserir_valor_grade(grade, 6, 4, 3)
    inserir_valor_grade(grade, 6, 5, 7)
    inserir_valor_grade(grade, 6, 8, 4)
    inserir_valor_grade(grade, 7, 0, 2) 
    inserir_valor_grade(grade, 7, 1, 8)
    inserir_valor_grade(grade, 7, 2, 7)
    inserir_valor_grade(grade, 7, 6, 6)  
    inserir_valor_grade(grade, 7, 7, 3)                 
    inserir_valor_grade(grade, 8, 0, 3)
    inserir_valor_grade(grade, 8, 1, 4)
    inserir_valor_grade(grade, 8, 2, 5)
    inserir_valor_grade(grade, 8, 3, 2) 
    inserir_valor_grade(grade, 8, 5, 6)                 
    inserir_valor_grade(grade, 8, 6, 1)
    exibir_grade(grade)



# *extra* Se desejar tire os (#) comentario abaixo para usar o modo teste

#funcao_teste()
#input()


def main(): 
# Programa principal guardando as grades e a interface para o usuario; none->none   
    grade1 = [[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],
    [0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],
    [0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]]

    grade2 = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]

    grade3 = [[0,0,0,0,0,0,0,0,4],[6,8,0,1,0,4,0,2,0],[1,9,0,0,0,0,3,8,0],
    [2,7,0,9,0,0,6,0,1],[4,0,9,2,7,1,5,3,0],[3,0,0,0,4,8,2,0,0],
    [5,0,0,8,0,0,0,6,7],[0,0,0,4,6,0,0,0,3],[0,0,0,0,0,5,9,0,0]]

    grade4 = [[0,0,0,8,0,0,0,0,3],[0,0,8,0,5,4,2,6,0],[0,7,1,6,0,0,0,8,0],
    [4,2,0,0,7,0,9,5,0],[0,0,0,0,4,0,0,0,0],[0,0,0,0,0,9,7,3,0],
    [9,5,0,4,2,3,0,2,0],[0,3,6,0,0,0,0,0,0],[0,1,0,5,2,6,0,0,7]],

    grade5 = [[0,0,0,0,4,0,0,0,0],[0,0,2,1,0,0,5,6,0],[0,0,0,0,6,0,3,8,1],
    [7,0,0,0,3,0,8,0,5],[0,9,3,2,8,7,0,4,0],[0,6,1,0,0,0,2,0,3],
    [0,0,9,0,7,5,4,1,2],[0,0,8,0,0,6,9,0,0],[0,0,0,4,0,0,0,0,0]]

    while True:
        os.system('cls || clear') # Limpar a tela
        exibir_menu_principal()
        opt = input('\nOpção desejada: ')
        if opt == '1':
            n = int(input('\nDigite um número de 1 a 5 para escolher uma grade: '))
            if n == 1:
                grade = copia_grade(grade1)
            elif n == 2:
                grade = copia_grade(grade2)
            elif n == 3:
                grade = copia_grade(grade3)
            elif n == 4:
                grade = copia_grade(grade4)
            elif n == 5:
                grade = copia_grade(grade5)
            else:
                input('Opção inválida. Pressione ENTER para continuar...')
                break        
            iniciar_jogo(grade)
        elif opt == '2':
            break
        else:
            input('Opção inválida. Pressione ENTER para continuar...')
if __name__ == '__main__':
    main()
