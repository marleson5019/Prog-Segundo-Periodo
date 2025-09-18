'''
Esse é um programa em Python que:
Faça um programa em Python que:

Leia vários conjuntos de 3 números reais.

Para cada conjunto de 3 números verifique se os mesmos formam um triângulo.

Se formarem um triângulo:

- Calcule e imprima a área do triângulo usando a fórmula de Heron.

- Determine a maior e a menor área calculada para os triângulos.

- Conte quantos triângulos são: EQUILATEROS, ESCALENOS ou ISOSCELES. 

Se os 3 números reais não formarem um triângulo emita uma mensagem NAO 
TRIANGULO e conte os conjuntos de 3 números que não forma triangulo.

Considere que:

- a entrada de dados encerra quando o usuário informar os 3 números reais iguais a zero.

- 3 valores reais quaisquer formam um triângulo quando cada valor for 
menor que a soma dos outros dois.
Marlyson Rodrigues Souza
11/09/2025
'''

import math

def main():
    # Declaração de variáveis
    x = float() 
    y = float() 
    z = float() 
    area = float() 
    s= float() 
    maior_area = None 
    menor_area = None 
    n_equilatero = int() 
    n_escaleno = int() 
    n_isosceles = int() 
    n_naotriangulo = int()

    # Entrada de dados inicial
    x = float(input())
    y = float(input())
    z = float(input())

    # Processamento
    while x != 0 or y != 0 or z != 0:
        if x + y > z and y + z > x and x + z > y:
            s = (x + y + z) / 2
            area = math.sqrt(s * (s - x) * (s - y) * (s - z))

            if maior_area is None or area > maior_area:
                maior_area = area
            if menor_area is None or area < menor_area:
                menor_area = area

            if x == y and y == z:
                print(f"X={x:.2f} Y={y:.2f} Z={z:.2f} AREA={area:.2f}")
                n_equilatero += 1
            elif x != y and y != z and x != z:
                print(f"X={x:.2f} Y={y:.2f} Z={z:.2f} AREA={area:.2f}")
                n_escaleno += 1
            else:
                print(f"X={x:.2f} Y={y:.2f} Z={z:.2f} AREA={area:.2f}")
                n_isosceles += 1
        else:
            print(f"X={x:.2f} Y={y:.2f} Z={z:.2f} NAO TRIANGULO")
            n_naotriangulo += 1

        # Próxima entrada
        x = float(input())
        y = float(input())
        z = float(input())

    # Resultados finais
    if maior_area is None:
       maior_area=0
    if menor_area is None:
       menor_area=0
    if n_equilatero !=0 or n_isosceles!=0 or n_escaleno !=0 or n_naotriangulo != 0:
        print(f"MAIOR AREA={maior_area:.2f}")
        print(f"MENOR AREA={menor_area:.2f}")
        print(f"{n_equilatero} EQUILATEROS")
        print(f"{n_isosceles} ISOSCELES")
        print(f"{n_escaleno} ESCALENOS")
        print(f"{n_naotriangulo} NAO TRIANGULOS")

if __name__ == "__main__":
    main()
