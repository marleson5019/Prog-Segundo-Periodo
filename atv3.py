#Declaração da variável
num = int
#Entrada de Dados
num = int(input())
#Processamento e Saída de Dados
if num > 0:
	if num%2==0:
		print("NUM=%.0f POSITIVO PAR"% (num))
	else:
	    print("NUM=%.0f POSITIVO IMPAR"% (num))
elif num < 0:
    if num%2==0:
        print("NUM=%.0f NEGATIVO PAR"% (num))
    else:
        print("NUM=%.0f NEGATIVO IMPAR"% (num))
elif num==0:
    print("NUM=%.0f NULO" % (num))