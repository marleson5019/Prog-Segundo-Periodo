'''Faça um programa em Python3 que resolva o problema a seguir:

Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um programa que determine o tempo necessário para
que essa massa se torne menor do que 0,5 grama. Escreva a massa inicial, a massa final e o
tempo calculado em horas, minutos e segundos.
Marlyson Rodrigues Souza
22/09/2025
'''
def main():
	#Declaração de variaveis
	massa_inicial = float()
	massa_final = float()
	tempo = int()
	hora = int()
	minuto = int()
	segundo = int() 
	
	#Entrada de dados
	massa_inicial = float(input())
	massa_final = massa_inicial

	while massa_final >= 0.5:
		tempo=tempo+50
		massa_final=massa_final/2
		
	while tempo>=3600:
		hora=hora+1
		tempo=tempo-3600
	while tempo>=60:
		minuto=minuto+1
		tempo=tempo-60
	segundo=tempo
	#Saída de dados
	print(f"MASSA INICIAL={massa_inicial:.2f} MASSA FINAL={massa_final:.2f} TEMPO DECORRIDO={hora:02d}:{minuto:02d}:{segundo:02d}")
if __name__=="__main__":
	main()
