faltas=int()
def ler_notas():
	nota = float(input())
	if 0<= nota <= 100:
		return nota

def ler_faltas():
	faltas = int(input())
	if 0<= faltas <=60:
		return faltas
	
def preencher_lista(qtd):
	alunos = []
	
	for i in range(qtd):	
		nome = input()
		notas = ler_notas()
	
		faltas = ler_faltas()
	
		alunos.append([nome, notas, faltas])
	return alunos

def imprimir_relatorio(lista):
	for nome, notas, faltas, in lista:
		if faltas > 15 and notas < 60:
			situacao = "REPROVADO POR NOTA E FALTA"
		elif faltas >= 15:
			situacao = "REPROVADO POR FALTA"
		elif notas < 60:
			situacao = "REPROVADO POR NOTA"
		else:
			situacao = "APROVADO"
			
		print(f"Nome={nome} Situação Final={situacao}")

def main():
	qtd=int(input())
	lista = preencher_lista(qtd)
	imprimir_relatorio(lista)
	
if __name__ == "__main__":
	main()