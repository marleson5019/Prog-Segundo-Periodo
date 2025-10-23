'''PROBLEMA:

a) Crie uma função que receba como parâmetro um valor real e calcule a soma deste valor a 1. Retorne o valor calculado.
Esta função representa a função da matemática: f(x) = x + 1
b) Crie uma função que receba como parâmetro um valor real e calcule o quadrado deste valor. Retorne o valor calculado.
Esta função representa a função da matemática: g(x) = x2
c) Crie uma função que receba como parâmetro um valor real e calcule a fog(x). Retorne o valor calculado.
Esta função representa a função da matemática: fog(x)
d) Crie uma função que receba como parâmetro um valor real e calcule a gof(x). Retorne o valor calculado.
Esta função representa a função da matemática: gof(x)
e) Crie uma função principal (ou programa principal) que lê um valor real k, qualquer, e invoca, na ordem,
as funções a), b), c) e d) com o valor de k. Imprima o valor retornado por cada função.'''
#Função x+1
def fx(x:float)->float:
	return x+1
#Função x²
def gx'x(x:float)->float:
	return x*x
#Função fog
def fog(x:float)->float:
	return fx(gx(x))
#Função gof
def gof(x:float)->float:
	return gx(fx(x))
#Função principal
def main():
	#Declaração de variáveis
	k=float()
	a=float()
	b=float()
	c=float()
	d=float()
	#Entrada de dados
	k=float(input())
	a=fx(k)
	b=gx(k)
	c=fog(k)
	d=gof(k)
	#Saída de dados
	print(f"Valor de k={k:.2f}")
	print(f"f({k:.2f})={a:.2f}")
	print(f"g({k:.2f})={b:.2f}")
	print(f"fog({k:.2f})={c:.2f}")
	print(f"gof({k:.2f})={d:.2f}")
if __name__ == "__main__":
	main()
