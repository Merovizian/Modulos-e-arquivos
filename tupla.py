def tuplaint (quantidade):
    '''
    Modulo que cria uma Tupla de inteiros com os valores digitados pelo usuário.
    O valor maximo de elementos é definido pela 'quantidade' inserida pelo usuário.
    Não é possível digitar valores que não sejam inteiros.
    A saída é a tupla criada com os valores digitados: tupla.tuplaint(quantidade)
    '''

    lista = ''
    # Primeiramente cria-se uma lista de strings
    for c in range (0, quantidade):
        valor = input("Digite um valor: ").strip()
        lista += valor
        if c < quantidade-1:
            lista += ','
    lista = lista.split(',')
    # Apos criada a lista com strings numéricos, ela é convertida em uma lista de inteiros
    for c in range(0, quantidade):
        lista[c] = int(lista[c])
    # Transformo a lista em uma tupla.
    lista = tuple(lista)
    return lista