'''a) Crie uma função que preenche uma lista com a contagem das notas possíveis de uma prova com questões de múltipla escolha. Esta prova de múltipla escolha pode ter N questões e cada questão vale 1 ponto. Esta função recebe como parâmetro a quantidade N de questões, a quantidade P de pessoas inscritas no concurso, lê as notas dos candidatos inscritos no concurso, ou seja, um valor inteiro que varia de 0 a N. Esta função retorna a lista de contagem de notas possíveis preenchida.

b) Crie uma função que recebe como parâmetro a lista de notas possíveis e imprima as nota conforme o modelo a seguir:

NOTA 0 FREQUENCIA ABSOLUTA=99 FREQUENCIA RELATIVA=99.99%

.

.

.

NOTA N FREQUENCIA ABSOLUTA=99 FREQUENCIA RELATIVA=99.99%

c) Faça o programa principal que invoque:

- Leia a quantidade de questões do concurso

- Leia a quantidade participantes do concurso

- E invoque corretamente as funções a) e b)

Marlyson Rodrigues Souza 02/12/2025'''
#Declaração de variáveis
n = 0
p = 0
contagem = []
nota = 0
i = 0

#Entrada de dados / Processamento
def preencher_contagem(n, p):
    #Inicialização de variáveis
    contagem = [0] * (n + 1)

    #Entrada de dados
    for i in range(p):
        nota = int(input())
        if 0 <= nota <= n:
            contagem[nota] += 1
        #Processamento (valores fora de 0..n são ignorados sem mensagens)

    #Saída de dados (retorno da lista)
    return contagem

#Processamento / Saída de dados
def imprimir_frequencias(contagem, p):
    for i in range(len(contagem)):
        freq_abs = contagem[i]
        freq_rel = (freq_abs / p) * 100 if p > 0 else 0
        print(f"NOTA {i} FREQUENCIA ABSOLUTA={freq_abs} FREQUENCIA RELATIVA={freq_rel:.2f}%")

#Entrada de dados / Processamento / Saída de dados
def main():
    #Entrada de dados
    n = int(input())
    p = int(input())

    #Processamento
    contagem = preencher_contagem(n, p)

    #Saída de dados
    imprimir_frequencias(contagem, p)

#Invocação condicional
if __name__ == "__main__":
    main()
