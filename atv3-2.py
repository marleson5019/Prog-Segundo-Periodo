'''Este Programa em python le diversos numeros e classifica-os em primo'''
#Função de calcular primo
def is_primo (n:int) -> bool:
	if n<2:
		return False
	for i in range(2,int(n**0.5)+1):
		if n% i == 0:
			return False
	return True
	
#Função de Saída
def saida(primos:list):
	for i in range(len(primos)):
		print(f"LISTA[{i}]={primos[i]}")
	
#Função principal
def main():
	primos = []
	n=int(1)
	while n>0:
		#Entrada de dados
		n=int(input())
		if is_primo(n):
			primos.append(n)
	#Saída de dados
	saida(primos)
	
if __name__ == "__main__":
	main()
