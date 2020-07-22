def leiafloat(msg='',i=-float('inf'),f=float('inf')):
    '''
    Programa que lê um valor pelo usuario e retorna um float, caso o usuário não digite nenhum float será mostrado uma mensagem de erro.
    :param msg: Mensagem que o usuario final vai ler ex:"digite um número: "
    :param i: inicio do intervalo
    :param f: final do intervalo
    :return: o float dentro desse intervalo
    '''
    # Verifica se o intervalo é funcional , ou seja, minimo seja menor que o maximo, se não for, inverte-se a ordem
    if i>f:
        aux = i
        i = f
        f = aux
    while True:
        # retorna uma mensagem de erro, caso o usuario interrompa o processo
        try:
            numero = input(msg)
        except KeyboardInterrupt:
            return f'\nO usuário preferiu não continuar com o programa'
        # Se o processo não for interrompido o programa continua
        else:
            # Caso o usuario tenha digitado ',' no lugar de '.' o programa faz a troca
            numero = numero.replace(',','.')

            # cria uma nova variavel 'n' sem o valor de '.' para verificar se 'n' é numero
            if numero.find('.') != -1:
                n = numero[0:numero.find('.')] + numero[(numero.find('.')+1):]
            else:
                n = numero
            # primeiro verifica-se se tem algum valor na variavel
            if len(n) != 0:
                # verifica se é negativo, pois o python não reconhece negativo como numero
                if n[0] == '-':
                    # se for negativo, é necessario primeiramente tirar o simbolo '-' para fazer a testagem
                    if n[1:].isnumeric():
                        # caso seja numero, coloca-se na variavel 'n' o valor do numero digitado, já com o '.', se houver.
                        n = float(numero)
                        # verifica se esta dentro do intervalo
                        if n < i or n > f:
                            print(f"\033[1;33mError, Digite um valor entre {i} e {f}\033[m")
                        else:
                            return (n)
                    else:
                        print("\033[1;31mError, Digite um valor float válido!\033[m")
                else:
                    # caso o numero digitado seja positivo
                    if n.isnumeric():
                        n = float(numero)
                        if n < i or n > f:
                            print(f"\033[1;33mError, Digite um valor entre {i} e {f}\033[m")
                        else:
                            return n
                    else:
                        print("\033[1;31mError, Digite um valor float válido!\033[m")
            else:
                print("\033[1;31mError, Digite um valor float válido!\033[m")

