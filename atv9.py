'''Esse é um programa em Python que:
Lê vários conjuntos de 3 números reais.
Para cada conjunto de 3 números verifica
 se os mesmos formam um triângulo, se formarem 
 um triângulo classifica em: EQUILATERO, 
 ESCALENO ou ISOSCELES. Se os 3 números reais não 
 formarem um triângulo emite uma mensagem NAO TRIANGULO.
 Marlyson Rodrigues Souza
 11/09/2025'''
def main():
	#Declaração de Variáveis
	x = float()
	y = float()
	z = float()

	#Entrada de Dados
	x = float(input())
	y = float(input())
	z = float(input())

	#Processamento de dados
	while x!=0 or y!=0 or z!=0:
		if x+y>z and y+z>x and x+z>y:
			if x==y and y==z:
			#Saída de Dados
				print(f"X={x:.2f} Y={y:.2f} Z={z:.2f} EQUILATERO")
			elif x!=y and y!=z and x!=z:
				print(f"X={x:.2f} Y={y:.2f} Z={z:.2f} ESCALENO")
			else:
				print(f"X={x:.2f} Y={y:.2f} Z={z:.2f} ISOSCELES")
		else:
			print(f"X={x:.2f} Y={y:.2f} Z={z:.2f} NAO TRIANGULO")
		
		x = float(input())
		y = float(input())
		z = float(input())
if __name__=="__main__":
	main()
