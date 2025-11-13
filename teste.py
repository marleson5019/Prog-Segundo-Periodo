#Declaração de variáveis
notas = []
pesos = []
turma = []
qtd_alunos = 0
qtd_disciplinas = 0

#Função (a)
def preenche_lista(qtd_disciplinas:int) ->list:
    #Inicialização de variáveis
    lista = []
    #Entrada de dados
    for i in range(qtd_disciplinas):
        valor = float(input())
        lista.append(valor)
    #Saída de dados
    return lista

#Função (b)
def media_ponderada(notas, pesos):
    soma = 0
    soma_pesos = 0
    for i in range(len(notas)):
        soma += notas[i] * pesos[i]
        soma_pesos += pesos[i]
    media = soma / soma_pesos
    return media

#Função (c)
def preenche_turma(qtd_alunos:int, qtd_disciplinas:int) ->list:
    turma = []
    for i in range(qtd_alunos):
        nome = input()
        notas = preenche_lista(qtd_disciplinas)
        aluno = [nome, notas]
        turma.append(aluno)
    return turma

#Função (d)
def relatorio(turma, pesos):
    for aluno in turma:
        nome = aluno[0]
        notas = aluno[1]
        cr = media_ponderada(notas, pesos)
        print(nome, "CR={:.2f}".format(cr))

#Função principal
def main():
    #Entrada de dados
    qtd_alunos = int(input())
    qtd_disciplinas = int(input())
    print()
    pesos = preenche_lista(qtd_disciplinas)
    print()

    #Processamento
    turma = preenche_turma(qtd_alunos, qtd_disciplinas)
    print()

    #Saída de dados
    print("\n--- RELATÓRIO ---")
    relatorio(turma, pesos)

#Invocação da função main
if __name__ == "__main__":
    main()
