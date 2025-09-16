def main():
    '''Marlyson Rodrigues Souza
    21/08/2025'''
    #Declaração de Variáveis
    x=int()
    y=int()
    num=int(input())
    #Processamento de dados
    while num>0 :
    	if num%2==0:
    		x=x+1
    	else :
    		y=y+num
    	num=int(input())
    #Saída de Dados
    if x>1 or y>1:
    	print(x, "NUMEROS SAO PARES")
    	print("SOMA IMPARES=%.0f"%y)

if __name__ =="__main__":
    main()