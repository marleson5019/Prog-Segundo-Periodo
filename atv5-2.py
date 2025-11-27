def let_nota (k):
	notas = []
	for i in range(k):
		while len.notas<k:
			nota=int(input())
			if 0<= nota <= 100:
				notas.append(nota)
	return notas
	
def analisar_notas (notas):
	todas = list(range(101))
	freq = [0]*101
	for n in notas:
		freq[n]+=1
	presentes = sorted(set(notas))
	print(notas)
	print(presentes)
	for n in presentes:
		print(f"Nota{n}: {freq[n]} ocorrências")
		
def main():
	k=int(input())
	notas= ler_notas(k)
	analisar_notas(notas)
