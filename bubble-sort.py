import os

sair = 'n'
vetor = []
i = 0
j = 0
while sair == 'n':
    print('*' * 21)
    print('BUBBLE SORT ALGORITMO')
    print('*' * 21)
    op = int(input('Digite 1 para carregar o vetor ou 2 para ordenar: '))
    if op == 1:
        vetor.append(int(input('Digite um numero de 1 a 10: ')))
    elif op == 2:
        print(vetor)
        print('Ordenando o vetor')
        tam = len(vetor) - 1
        while j < len(vetor) - 1:
            while i < tam:
                if vetor[i] > vetor[i + 1]:
                    aux = vetor[i]
                    vetor[i] = vetor[i + 1]
                    vetor[i + 1] = aux

                i+=1
            j += 1
            i = 0

        print('Vetor Ordenado')
        print(vetor)
    sair = str(input('Deseja sair s - sim, n - não: '))
    os.system('cls') or None