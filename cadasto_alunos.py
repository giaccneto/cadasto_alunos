alunos = []

def criar_aluno():
    print("Insira os dado do aluno corretamente.")
    nome = input("Digite o nome do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    cpf = input("Digite o CPF do aluno, ex:(000.000.000-00): ")
    data_nasc = input("DIgite a data de nascimento, ex:(dd/mm/yyyy): ")

    aluno = {
        'nome': nome,
        'telefone': telefone,
        'cpf': cpf,
        'data_nasc': data_nasc,
        'notas': [] 
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso.")


def lancar_notas():
    nome = input("Digite o nome do aluno para lançamento de nota: ")
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            nota = float(input("Digite a nota (de 0 a 10): "))
            if 0 <= nota <= 10:
                aluno['notas'].append(nota)
            else:
                print("A nota deve ser de 0 a 10. ")
        else:
            print("Aluno não encontrado! ")


#def excluir_notas():

def calc_notas():
    nome = input("Digite o nome do aluno para lançamento de nota: ")
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            media = sum(aluno['notas']) / len(aluno['notas'])
            print(media)

def listar_alunos():
    for aluno in alunos:
        print(aluno)


def menu():
     while True:
        print("BEM VINDO AO CADASTRO DE ALUNOS.")
        print("\n1 - Cadastrar aluno: ")
        print("\n2 - Lançar notas: ")
        print("\n3 - Excluir notas: ")
        print("\n4 - Calcular média: ")
        print("\n5 - Listar alunos: ")
        print("\n6 - Sair ")

        opcao = input("\nDigite o numero da opção desejada: " ).lower()

   
        if opcao.lower() == '1':
            criar_aluno()
        elif opcao.lower() == '2':
            lancar_notas()
        elif opcao.lower() == '3':
            excluir_notas()
        elif opcao.lower() == '4':
            calc_notas()
        elif opcao.lower() == '5':
            listar_alunos()
            
        elif opcao.lower() == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção mão encontrada, digite um numero valido: ")


if __name__ == "__main__":
    menu()