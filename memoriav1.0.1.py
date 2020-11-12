#modulo para randomizar 
import random
#modulo de interface
import os

# Funções
def iniciar_jogo():
#Função usada para iniciar o jogo; None -> None
    global memoria, descoberto
    valores = random.sample([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8], 16)
    memoria = [valores[0:4], valores[4:8], valores[8:12], valores[12:16]]
    descoberto = [[False, False, False, False],
                  [False, False, False, False],
                  [False, False, False, False],
                  [False, False, False, False]]
    return

def exibir_jogo():
#Função usada para exibir o jogo; None -> None
    for i in range(0, 4):
        for j in range(0, 4):
            if descoberto[i][j]:
                print(memoria[i][j], end=' ')
            else:
                print('*', end=' ')
        print()
        
    
def revelar_posicao(l1, c1):
#Função feita para revelar posições; int,int -> bool
    if descoberto[l1][c1] == False:
        descoberto[l1][c1] = True
        return True
    return False


def checar_posicoes(l1, c1, l2, c2):
#Função para chegar as posições; int,int,int - > bool 
    if memoria[l1][c1] == memoria[l2][c2]:
        print('\nParabéns! Você acertou!')
        return True
    else:
        print('\nVocê errou. Tente novamente.')
        esconder_posicoes(l1, c1, l2, c2)
        return False
    
    
def esconder_posicoes(l1, c1, l2, c2):
#Função para esconder as posições; int,int,int,int -> none
    descoberto[l1][c1] = False
    descoberto[l2][c2] = False
    return


def checar_vitoria():
#Função para chegar vitoria; none -> none
    for i in range(0, 4):
        if False in descoberto[i]:
            return False
    return True

iniciar_jogo()
jogadas = 0

def main():
# Programa Principal onde fica a interface para o usuario inputar;none -> none
    while True:
        os.system('cls || clear')
        
        r = list(range(0, 4))
        exibir_jogo()
        while True:
            pos1 = list(input('\nEscolha a primeira posição [x,y]: '))
            l1 = int(pos1[1])
            c1 = int(pos1[3])
            print()
            if l1 not in r or c1 not in r:
                input('Posição inválida. Pessione ENTER para tentar novamente...')
            elif not revelar_posicao(l1, c1):
                input('Posição inválida. Pessione ENTER para tentar novamente...')
            else:
                break
            
        exibir_jogo()
        
        while True:
            pos2 = list(input('\nEscolha a segunda posição [x,y]: '))
            print()
            l2 = int(pos2[1])
            c2 = int(pos2[3])
            if l2 not in r or c2 not in r:
                input('Posição inválida. Pessione ENTER para tentar novamente...')
            elif not revelar_posicao(l2, c2):
                input('Posição inválida ou já escolhida. Pessione ENTER para tentar novamente...')
            else:
                break
        iniciar_jogo()
        jogadas = 0

        jogadas += 1
        exibir_jogo()
        checar_posicoes(l1, c1, l2, c2)
        if checar_vitoria():
            print('\nParabéns! Você conseguiu descobrir todas as casas em', jogadas, 'jogadas!')
            break
        input('\nPessione ENTER para continuar...')

if __name__ == '__main__':
    main()