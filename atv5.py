def main():
    '''Pprograma que le um número inteiro positivo e
    imprime a tabuada deste número. Caso não seja positivo
    não imprima nada.'''
    #Declaração de variáveis
    num=int()
    cont=int()
    resultado=int()
    num=int(input())
    cont=0
    if num>0:
    #Processamento de dados
        while cont<10:
            cont=cont+1
            resultado=num*cont
            print(num,"x",cont,"=",resultado)
if __name__=="__main__":
    main()