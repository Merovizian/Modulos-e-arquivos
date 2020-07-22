def leiaint(msg='',i=-float('inf'),f=float('inf')):
    '''
    Programa que lê um valor pelo usuario e retorna inteiro, caso o usuário não digite nenhum inteiro será mostrado uma mensagem de erro.
    :param msg: Mensagem que o usuario final vai ler ex:"digite um número: "
    :param i: inicio do intervalo
    :param f: final do intervalo
    :return: o inteiro dentro desse intervalo
    '''
    # Verifica se o intervalo é funcional , ou seja, minimo seja menor que o maximo, se não for, inverte-se a ordem
    if i>f:
        aux = i
        i = f
        f = aux
    while True:
        numero = input(msg)
        # primeiro verifica-se se tem algum valor na variavel
        if len(numero) != 0:
            # verifica se é negativo, pois o python não reconhece negativo como numero
            if numero[0] == '-':
                # se for negativo, é necessario primeiramente tirar o simbolo '-' para fazer a testagem
                if numero[1:].isnumeric():
                    # depois da testagem a string digitada pelo usuario vira int
                    numero = int(numero)
                    # verifica se esta dentro do intervalo
                    if numero < i or numero > f:
                        print(f"\033[1;33mError, Digite um valor entre {i} e {f}\033[m")
                    else:
                        return (numero)
                else:
                    print("\033[1;31mError, Digite um valor inteiro válido!\033[m")
            else:
                # Caso o numero seja positivo
                if numero.isnumeric():
                    # verifica se esta dentro do intervalo
                    numero = int(numero)
                    if numero < i or numero > f:
                        print(f"\033[1;33mError, Digite um valor entre {i} e {f}\033[m")
                    else:
                        return numero
                else:
                    print("\033[1;31mError, Digite um valor inteiro válido!\033[m")
        else:
            print("\033[1;31mError, Digite um valor inteiro válido!\033[m")



