def addDados(nome,email,cpf):
    dados = {'nome': nome,'email':email,'cpf':cpf}
    return dados

def addCurso(cod,curso,hr):
    dados = {'cod': cod,'curso':curso,'hr':hr}
    return dados

def addCursoAluno(c,a):
    dados = {'curso': c,'aluno':a}
    return dados
    
if __name__ == '__main__':
        op = "i"
        lista = []
        listac = []
        listav = []

        while op != "s":
                op = str(input("Escolha sua opção: \n c - cadastrar  \n l - listar \n v - vincular curso/aluno \n s - sair: "))
                if op == "c":
                        opCad = str(input("\nc - curso \na - aluno: "))
                        if opCad == "a":
                                nome = str(input("Digite seu nome: "))
                                email = str(input("Digite seu email: "))
                                cpf = str(input("Digite seu CPF: "))
                                lista.append(addDados(nome,email,cpf))
                        elif opCad == "c":
                                cod = str(input("Digite codigo do curso: "))
                                curso = str(input("Digite nome do curso: "))
                                hr = str(input("Digite horas do curso: "))
                                listac.append(addCurso(cod,curso,hr))
                        else:
                                print("opcao invalida")
                elif op == "v":
                        c = int(input("codigo curso: "))
                        a = int(input("codigo aluno: "))
                        listav.append(addCursoAluno(listac[c],lista[a]))
                elif op == "l":
                        opList = str(input("\nca - curs/aluno \nc - curso \na - aluno: "))
                        if opList == "a":
                                for a in lista:
                                        print(a)
                        elif opList == "c":
                                for b in listac:
                                        print(b)
                        elif opList == "ca":
                                for c in listav:
                                        print(c)
                        else:
                                print("opcao invalida")
