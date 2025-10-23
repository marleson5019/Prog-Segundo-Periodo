'''O programa a seguir calcula o fatorial de um número lido
Marlyson Rodrigues Souza 23/10/2025'''
#Comado fatorial
def fat(num:int)->int:
	#Declaração de variáveis
	cont=int()
	answ=int()
	cont=1
	answ=1
	#Processamento de dados
	for cont in range (1, num+1,1):
		answ=answ*cont
	return answ
	
def main():
	#Declaração das variáveis locais
	num=int()
	num=int(input())
	answ=fat(num)
	#Saída de dados
	print(f"Número={num} FATORIAL={answ}")
if __name__ == "__main__":
	main()
