# Marlyson Rodrigues Souza
# Data: 18/09/2025
# O programa resolve uma equação do 2º grau com coeficientes reais (a, b, c).
# Exibe as raízes reais se existirem; caso contrário, mostra mensagens apropriadas.

import math

# Declaração de variaveis
a = float()
b = float()
c = float()
delta = float()
raiz1 = float()
raiz2 = float()
x1= float()
x2=float()

#Entrada de dados
a= float(input())
b= float(input())
c= float(input())

# Processamento de dados
if a == 0:
    print("NAO EH EQ 2G")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("NAO TEM SOLUCAO NO DOMINIO DO NUMEROS REAIS")
    else:
        raiz1 = (-b - math.sqrt(delta)) / (2*a)
        raiz2 = (-b + math.sqrt(delta)) / (2*a)
        x1 = min(raiz1, raiz2)
        x2 = max(raiz1, raiz2)
        #Saída de dados
        print(f"x1={x1:.2f}")
        print(f"x2={x2:.2f}")
