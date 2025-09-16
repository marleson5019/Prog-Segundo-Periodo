#Declaração de Variáveis
peso = float()
altura = float()
imc = float()
#Entrada de Dados
peso = float(input())
altura = float(input())
#Processamento de dados
imc = peso/(altura**2)
#Saída de Dados
print("PESO=%.2f ALTURA=%.2f IMC=%.2f"%(peso, altura, imc))