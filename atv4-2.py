'''Marlyson Rodrigues Souza 27/11/2025
a) Crie uma função que preenche uma lista de notas/pesos float. 
Esta função recebe como parâmetro a quantidade de notas/pesos a 
serem armazenadas nesta lista. Esta função retorna a lista preenchida.

b) Crie uma função que recebe como parâmetro duas listas de 
valores float. A primeira lista contém as notas em diversas 
disciplinas e a segunda lista contém os pesos das notas da 
primeira lista. Calcule e retorne a média ponderada destas notas.

c) Crie uma função que preenche uma lista de dados dos alunos 
de uma turma (lista de lista). O dados de cada aluno são:

Nome - string

Lista de notas - lista

Esta função recebe como parâmetro dois valores inteiros, o 
primeiro é a quantidade de alunos na turma e o segundo é a 
quantidade de disciplinas que os alunos da turma cursam.

Esta função retorna a lista de listas, ou seja, a turma.

d) Faça uma função que receba a lista de listas (turma) e uma 
lista de pesos das disciplinas e imprima um relatório contendo 
o nome do aluno e seu coeficiente de rendimento ( média das 
disciplinas cursadas ) com o formato a seguir:

AAAAA CR=99.99

BBBBB CR=99.99

e) Faça o programa principal que leia a quantidade de alunos da 
turma, a quantidade de disciplinas cursadas pelos alunos e os 
pesos das disciplinas (usando a função a) ). A partir da leitura 
destes dados, invoque corretamente as funções acima. '''

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
def preenche_relatorio(turma, pesos):
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
    pesos = preenche_lista(qtd_disciplinas)
    #Processamento
    turma = preenche_turma(qtd_alunos, qtd_disciplinas)
    #Saída de dados
    preenche_relatorio(turma, pesos)
#Chama função main
if __name__ == "__main__":
	main()
