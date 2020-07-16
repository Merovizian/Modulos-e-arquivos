def leiaint(msg='',i=-float('inf'),f=float('inf')):
    '''
    Programa que lê um valor pelo usuario e retorna inteiro, caso o usuário não digite nenhum inteiro será mostrado uma mensagem de erro.
    :param msg: Mensagem que o usuario final vai ler ex:"digite um número: "
    :param i: inicio do intervalo
    :param f: final do intervalo
    :return: o inteiro dentro desse intervalo
    '''
    while True:
        numero = input(msg)
        if numero[0] == '-':
            if numero[1:].isnumeric():
                numero = int(numero)
                if numero < i or numero > f:
                    print(f"\033[1;33mError, Digite um valor entre {i} e {f}\033[m")
                else:
                    return (numero)
            else:
                print("\033[1;31mError, Digite um valor inteiro válido!\033[m")
        else:
            if numero.isnumeric():
                numero = int(numero)
                if numero < i or numero > f:
                    print(f"\033[1;33mError, Digite um valor entre {i} e {f}\033[m")
                else:
                    return numero
            else:
                print("\033[1;31mError, Digite um valor inteiro válido!\033[m")
