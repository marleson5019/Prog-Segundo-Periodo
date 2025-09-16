'''O progra l:

- A distância (em km) percorrida e o tempo gasto 
 (em segundos) de diversos trechos percorridos por um motorista;
- Para cada trecho percorrido, imprime o deslocamento em 
 metros (m) e o tempo gasto em segundos (s);
- Para cada trecho percorrido, calcule e imprime a velocidade 
média em metros por segundo (m/s) ;
- Imprime a maior e a menor velocidade média calculada, 
admitindo-se a simplificação que não existem valores repetidos 
para as velocidades médias calculadas.

          09/09/2025 Marlyson Rodrigues Souza'''
def main():
	#Declaração de Variáveis
	distancia_km=float()
	tempo_s=float()
	deslocamento_m=float()
	vm=float()
	maiorvm=None
	menorvm=None

	#Entrada de dados
	distancia_km=float(input())
	tempo_s=float(input())
		
	#Processamento de Dados
	while distancia_km>0 and tempo_s>0:
		deslocamento_m=distancia_km*1000
		vm=deslocamento_m/tempo_s
		print(f"S={deslocamento_m:.2f}m T={tempo_s:.2f}s VM={vm:.2f}m/s")
		distancia_km=float(input())
		tempo_s=float(input())
		
		if maiorvm is None or vm > maiorvm:
			maiorvm = vm
			
		if menorvm is None or vm < menorvm:
			menorvm = vm
			
	if maiorvm is not None and menorvm is not None:
		print(f"MAIOR VM={maiorvm:.2f}m/s MENOR VM={menorvm:.2f}m/s")
		
		
if __name__=="__main__":
	main()
