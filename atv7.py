def main():
	#Declaração de Variáveis
	num1 = int()
	num2 = int()
	contador = int(0)
	resto = int(0)
	#Atribuição de Variáveis
	num1=int(input())
	num2=int(input())
	#Processamento de dados
	if num1>0 and num2>0:
		n = int(num1)
		m = int(num2)
		
		while n>=m:
			contador=contador+1
			n=n-m
		resto=n	
		#Saída de Dados
		print(f"N={num1:.0f} M={num2:.0f} Q={contador:.0f} R={resto:.0f}")
		
	else:
		print("DADOS INVALIDOS")
if __name__=="__main__":
	main()
