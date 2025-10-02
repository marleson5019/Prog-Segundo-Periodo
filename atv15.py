'''O seguinte programa em python recebe números inteiros, calcula a média dos numeros inteiros pares positivos,
e classifica o maior e menor numero representador 
Marlyson Rodrigues Souza
02/10/2025'''
def main():
	#Declaração de variaveis
	num=int()
	maxi=None
	mini=None
	contador=int()
	soma=int()
	media=None
	totalnegi=int()
	totalposi=int()
	
	#Entrada de dados
	num=int(input())
	
	#Processamento de dados
	while num!=0:
		if maxi is None or maxi<num:
			maxi=num
		if mini is None or mini>num:
			mini=num
		if num%2!=0 and num<0	:
			contador=contador+1
			soma=soma+num
			media=0
		if num<0:
			totalnegi=totalnegi+1
		if num>0:
			totalposi=totalposi+1
		num=int(input())
				
	#Saída de dados
	if media is not None:
		media=soma/contador
		print(f"MEDIA = {media:.2f}")
	if maxi is not None and mini is not None:
		if media is None:
			print("MEDIA = 0.00")
		print(f"MAIOR = {maxi}")
		print(f"MENOR = {mini}")
		print(totalnegi,"NEGATIVOS")
		print(totalposi,"POSITIVOS")
if __name__=="__main__":
	main()
