from random import randint
from time import sleep
print('\033[1;32m============== TREINO MATEMATICO ===================\033[m')
op=0
t=1
esp=52
n=str(input('Digite seu Nome: '))
print('\033[1;32m=\033[m' * esp)
while op!=5:
    print('''\033[1;34mESCOLHA ABAIXO UMA DAS OPERAÇÕES MATEMATICAS
    [1] (+) SOMA 
    [2] (-) SUBITRAIR
    [3] (*) MULTIPLICAR
    [4] Sair do Programa''')
    funcao=str(input('Digite a Opção :\033[m'))
    print('\033[1;32m=\033[m' * esp)
    while funcao not in '1234':
            print('''\033[1;34mESCOLHA ABAIXO UMA DAS OPERAÇÕES MATEMATICAS
            [1] (+) SOMA 
            [2] (-) SUBITRAIR
            [3] (*) MULTIPLICAR
            [4] Sair do Programa''')
            funcao = str(input('Digite a Opção :\033[m'))

    if funcao=='1':
        n1 = randint(1, 1000)
        n2 = randint(1, 1000)
        print('De valor dessa soma {} + {} ? {}'.format(n1,n2,n))
        print('\033[1;32m=\033[m' * esp)
        rs = n1 + n2
    elif funcao=='2':
        n1 = randint(1, 1000)
        n2 = randint(1, 1000)
        if n1 < n2:
            print('De valor dessa subitração {} - {} ? {}'.format(n2, n1, n))
            print('\033[1;32m=\033[m' * esp)
            rs = n2 - n1
        else:
            print('De valor dessa subitração {} - {} ? {}'.format(n1, n2, n))
            print('\033[1;32m=\033[m' * esp)
            rs = n1 - n2
    elif funcao == '3':
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        print('De valor dessa multiplicação {} x {} ? {}'.format(n1, n2, n))
        print('\033[1;32m=\033[m' * esp)
        rs = n1 * n2
    elif funcao == '4':
        op=5
        sleep(0.5)
        print('    Obrigado por usar o nosso programa {}\n '
              '             Volte sempre!!!!'.format(n))
        sleep(1)
        exit()
    res=int(input('\033[1;33mDigite o resultado tentativa numero {} para {}:\033[m'.format(t,n)))
    print('\033[1;32m=\033[m' * esp)
    while res !=rs:
        t=t+1
        res = int(input('\033[1;31m{} tentativa para {} ,Digite o resultado :\033[m'.format(t,n)))
        print('\033[1;32m=\033[m' * esp)

    if funcao=='1':
        print('{} voçe preciso de {} tentativa para acerta o\n'
              'resultado da soma entre {} e {} = {}'.format(n,t,n1,n2,rs))
        print('\033[1;32m=\033[m' * esp)
    elif funcao=='2':
        print('{} voçe preciso de {} tentativa para acerta o\n'
              'resultado da subitração entre {} e {} = {}'.format(n,t,n1,n2,rs))
        print('\033[1;32m=\033[m' * esp)
    elif funcao == '3':
        print('{} voçe preciso de {} tentativa para acerta o\n'
              'resultado da multiplicação entre {} e {} = {}'.format(n,t,n1,n2,rs))
        print('\033[1;32m=\033[m' * esp)