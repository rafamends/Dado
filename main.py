from random import randint
 
robot=randint(1,6)
escolha=1
acertos=0
jogadas=0
 
while escolha!=0:
    escolha=int(input('Digite 0 para sair ou escolha um número entre 1-6: '))
    if escolha in [1,2,3,4,5,6]:
        jogadas+=1
        if escolha==robot:
            print('Acertou!')
            acertos = acertos + 1
        else:
            print('Errou!')
    else:
        print('Escolha inválida. Acabou!')
        break
 
print(f'Número de jogadas: {jogadas}')        
print(f'Números de acertos: {acertos}')
