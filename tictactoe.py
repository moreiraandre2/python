op = "j"
game = [[0,0,0],[0,0,0],[0,0,0]]
while op == "j":
        print("-" * 19)
        print("TIC TAC TOE - GAME")
        print("-" * 19)
        for row in game:
                print(row)
        l= int(input("Qual linha deseja jogar? 0 , 1 ou 2: "))
        c = int(input("Qual coluna deseja jogar? 0 , 1 ou 2: "))
        valor = int(input("O que deseja jogar? 0 ou 1: "))
        if l >= 0 or l >= 2:
                if c >= 0 or c >= 2:
                        if valor == 0 or valor == 1:
                                game[l][c] = valor
                        else:
                                print("Valor invalido")
                else:
                        print("Coluna Invalida")
        else:
            print("Linha Invalida")
            
        for row in game:
                print(row)
        
        

