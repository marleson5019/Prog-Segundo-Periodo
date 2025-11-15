#Declaração de variáveis
notas = []
pesos = []
turma = []
qtd_alunos = 0
qtd_disciplinas = 0

#Função (a)
def preenche_lista(qtd_disciplinas:int) ->list:
    lista = []
    for i in range(qtd_disciplinas):
        valor = float(input())
        lista.append(valor)
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

#Função (c) — CORRIGIDA
def preenche_turma(qtd_alunos:int, qtd_disciplinas:int) ->list:
    turma = []

    # primeiro ler os nomes
    for i in range(qtd_alunos):
        nome = input()
        turma.append([nome, []])

    # agora ler as notas aluno por aluno
    for a in range(qtd_alunos):
        for d in range(qtd_disciplinas):
            nota = float(input())
            turma[a][1].append(nota)

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
    qtd_alunos = int(input())
    qtd_disciplinas = int(input())
    print()

    pesos = preenche_lista(qtd_disciplinas)
    print()

    turma = preenche_turma(qtd_alunos, qtd_disciplinas)
    print()

    print("\n--- RELATÓRIO ---")
    relatorio(turma, pesos)

if __name__ == "__main__":
    main()
