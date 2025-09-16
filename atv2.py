#Declaração de Variável
valor = float()
#Entrada de dados
valor=float(input())
#Validação de Dados e Saída de Dados
if valor > 0:
	print("NUM=%.2f"%valor,"POSITIVO")
elif valor < 0:
	print("NUM=%.2f"%valor,"NEGATIVO")
else:
	print("NUM=%.2f"%valor,"NULO")