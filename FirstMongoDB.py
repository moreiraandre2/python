from pymongo import MongoClient

con = MongoClient('mongodb://localhost:27017')
db = con.customers


def addDados(_id,nome,email,cpf,curso):
    aluno_id = db.customers.insert_one({"_id":_id,"nome":nome,"email":email,"cpf":cpf,"curso":""}).inserted_id
    print("ID aluno add: " + aluno_id)

def addCurso(_id,curso,hr):
    curso_id = db.curso.insert_one({"_id":_id,"curso":curso,"horas":hr}).inserted_id
    print("ID curso add: " + curso_id)
    
if __name__ == '__main__':

        op = "i"
        while op != "s":
                op = str(input("Escolha sua opção: \n c - cadastrar  \n l - listar \n v - vincular curso/aluno \n r - remover \n s - sair: "))
                if op == "c":
                        opCad = str(input("\nc - curso \na - aluno: "))
                        if opCad == "a":
                                _id = str(input("Digite o aluno ID: "))
                                nome = str(input("Digite o nome do aluno: "))
                                email = str(input("Digite o email do aluno: "))
                                cpf = str(input("Digite o CPF do aluno: "))
                                addDados(_id,nome,email,cpf,"")
                        elif opCad == "c":
                                cod = str(input("Digite codigo do curso: "))
                                curso = str(input("Digite nome do curso: "))
                                hr = str(input("Digite horas do curso: "))
                                addCurso(cod,curso,hr)
                        else:
                                print("opcao invalida") 

                elif op == "v":
                        id_aluno = str(input("Digite ID do aluno: "))
                        id_curso = str(input("Digite ID do curso: "))
                        if db.customers.find_one({"_id":id_aluno}):
                            if db.curso.find_one({"_id": id_curso}):
                                curso = db.curso.find_one({"_id": id_curso})
                                db.customers.update_one({"_id": id_aluno}, {"$set": {"curso":curso["curso"]}})
                            else:
                                print("ID curso não encontrado")
                        else:
                            print("ID aluno não encontrado")
                              
                elif op == "l":
                        opList = str(input("\nca - curs/aluno \nc - curso \na - aluno: "))
                        if opList == "a":
                                for a in db.customers.find():
                                        print(a)
                        elif opList == "c":
                                for b in db.curso.find():
                                        print(b)
                        else:
                                print("opcao invalida")
                
                elif op == "r":
                        opRm = str(input("\na - aluno \nc - curso \n ac - aluno/curso: "))
                        if opRm == "a":
                                id_aluno = str(input("Digite ID do aluno: "))
                                if db.customers.find_one({"_id": id_aluno}):
                                        print(db.customers.find_one({"_id": id_aluno}))
                                        confirm = str(input("Deseja remover? (s - sim)/(n - nao): "))
                                        if confirm == "s":
                                                db.customers.delete_one({"_id": id_aluno})
                                                print("Aluno Removido!")
                                        elif confirm == "n":
                                                print("Remocao cancelada")
                                        else:
                                                print("Opcao invalida")
                                else:
                                        print("ID aluno não encontrado")
                        if opRm == "c":
                                id_curso = str(input("Digite ID do curso: "))
                                if db.curso.find_one({"_id": id_curso}):
                                        print(db.curso.find_one({"_id": id_curso}))
                                        confirm = str(input("Deseja remover? (s - sim)/(n - nao): "))
                                        if confirm == "s":
                                                db.curso.delete_one({"_id": id_curso})
                                                print("Curso Removido!")
                                        elif confirm == "n":
                                                print("Remocao cancelada")
                                        else:
                                                print("Opcao invalida")
                                else:
                                        print("ID curso não encontrado")
                        
                        if opRm == "ac":
                                id_aluno = str(input("Digite ID do aluno: "))
                                if db.customers.find_one({"_id": id_aluno}):
                                        print(db.customers.find_one({"_id": id_aluno}))
                                        confirm = str(input("Deseja remover curso? (s - sim)/(n - nao): "))
                                        if confirm == "s":
                                                db.customers.update_one({"_id": id_aluno}, {"$set": {"curso":""}})
                                                print("Curso Removido o aluno!")
                                        elif confirm == "n":
                                                print("Remocao cancelada")
                                        else:
                                                print("Opcao invalida")
                                else:
                                        print("ID aluno não encontrado")
                        
                        else:
                                print("opcao invalida")