'''a) Faça uma função que receba duas strings e retorne uma string com os caracteres em comum entre as duas strings de entrada, com as restrições que os caracteres da string de saída devem:

- estar na ordem em que aparecem na primeira string

- não podem haver caracteres repetidos

Exemplos:
STRING1=HOJE EH FERIADO STRING2=AMANHA TAMBEM E FERIADO CARACTERES COMUNS=HOE FRIAD
STRING1=MELANCIA STRING2=GOIABA CARACTERES COMUNS=AI
STRING1=MATEMATICA HISTORIA INGLES STRING2=MATEMATICA HISTORIA INGLES CARACTERES COMUNS=MATEIC HSORNGLS
a) Faça o programa principal que leia diversos pares de strings e para cada par lido, imprima as duas strings lidas e os caracteres em comuns entre as duas strings lidas.
Considere que a entrada de dados encerra quando o usuário informar alguma string vazia na entrada de dados.
Marlyson Rodrigues Souza 02/12/2025'''
#Declaração de variáveis
string1 = ""
string2 = ""
resultado = ""

#Função para encontrar caracteres comuns
def caracteres_comuns(string1, string2):
    #Inicialização de variáveis
    resultado = ""

    #Processamento
    for c in string1:
        if c in string2 and c not in resultado:
            resultado += c
    return resultado

#Função principal
def main():
    #Entrada de dados inicial
    string1 = input()
    string2 = input()

    while string1 != "" and string2 != "":
        #Processamento
        resultado = caracteres_comuns(string1, string2)

        #Saída de dados
        print(f"STRING1={string1} STRING2={string2} CARACTERES COMUNS={resultado}")

        #Entrada de dados novamente
        string1 = input()
        string2 = input()

if __name__ == "__main__":
    main()
