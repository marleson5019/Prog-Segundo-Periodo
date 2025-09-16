def main():
	'''Marlyson Rodrigues Souza 28/08/2025
	 O programa pega 2 números digitados pelo usuário, 
	 e caso ambos números sejam positivos, e o primeiro 
	 seja menor que o segundo, imprime a tabuada dos 
	 números no intervalo entre esses 2 números'''
    #Declaração de variáveis
	n1 = int()
	n2 = int()
	# Entrada de dados
	n1 = int(input())
	n2 = int(input())

	# Processamento de dados
	if n1 > 0 and n2 > 0:
		if n1 < n2:
			m = n1
			while m <= n2:
				for n in range(1, 11):
					print(f"{m} x {n} = {m * n}")
				print()
				m += 1
if __name__=="__main__":
	main()
