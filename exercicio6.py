turma = {}

def cons():
    op = int(input("1, turmas\n2, alunos\n3, aluno"))
    if(op == 1):
        print(turma)
    elif(op == 2):
        num = str(input("Qual o nome da turma :"))
        print(turma[num])
    elif(op == 3):
        num = str(input("Qual o nome da turma :"))
        matricula = str(input("Qual a matricula do aluno :"))
        print(turma[num][matricula])
def adicionarAlunoNotas():
    num = str(input("Qual a matricula do aluno :"))
    alunos = {}
    matricula = str(input("A matricula"))
    notas = []
    x = 'sim'
    while (x == 'sim'):
        nota = float(input("Digite a nota do aluno :"))
        nota.append(nota)
        x = str(input("Adicionar mais notas ?"))
    turma[num][matricula] = notas

def adicionarTurma():
    nomedaturma = str(input("Qual o nome da turma ?"))
    alunos = {}
    turmas[nomedaturma]= alunos
def calcularMedia(notas):
    soma = 0
    for y in notas :
        soma +=y
    

def media():
    soma = 0
    auxiliar = 0
    nomedaturma = str(input("Qual o nome da turma"))
    for i in turmas[nomedturma]:
        soma += calcularMedia(turmas[NT][i])
        auxiliar +=1
    return soma/auxiliar
def menu():
    continua = 'sim'
    while (continua == 'sim'):
        op = int(input("O que deseja realizar? \n1, Adicionar Turma\n2, Adicionaral Aluno e Notas\n3, Calcular média de um Aluno\n4 , Calcular média de uma Turma\n5, Terminar\n"))
        if(op == I) :
            AdicionarTurma()
        elif(opçao == II):
            AdicionarAlunosNotas()
        elif(opçao == III):
            turma= str(input("turma"))
            matricula = str(input("matricula"))
            print(calcularMedia(turmas[turm][mat]))
        elif(opçao == IV):
            print(mediaTurma())
        elif(opçao == 0):
            print(mediaTurma())
        elif(opçao == V):
        while (Continuar = 'Nao')

menu()
