from urllib import request

def endereco (cep):
    '''
    Programa que retorna um dicionario com os dados de um dado CEP
    :param cep: inteiro que contem o cep da localidade, deve ter 8 digitos sem o '-'
    :return: dicionario com as caracteristicas do cep dado
    '''


    endereco = dict()
    site = f'https://viacep.com.br/ws/{cep}/piped/'
    f = request.urlopen(f"{site}")
    contents = f.read()
    f.close()
    contents = str(contents)[2:]
    contents = contents.replace('\\xc3\\xa9', 'é')
    contents = contents.replace('\\xc3\\xa3', 'ã')
    contents = contents.replace('\\xc3\\xb3', 'ó')
    contents = contents.replace('\\xc3\\xb5', 'õ')
    contents = contents.replace('\\xc3\\xba', 'ú')
    contents = contents.replace('\\xc3\\xa1', 'á')
    if str(contents) == 'erro:true\'':
        endereco['ERROR'] = 'Endereço Não Existe'
        return endereco
    else:
        contents = contents.split('|')
        endereco['cep'] = contents[0][contents[0].find(':') + 1:]
        endereco['logradouro'] = contents[1][contents[1].find(':')+1:]
        endereco['complemento'] = contents[2][contents[2].find(':')+1:]
        endereco['bairro'] = contents[3][contents[3].find(':') + 1:]
        endereco['localidade'] = contents[4][contents[4].find(':') + 1:]
        endereco['uf'] = contents[5][contents[5].find(':') + 1:]
        endereco['unidade'] = contents[6][contents[6].find(':') + 1:]
        endereco['ibge'] = contents[7][contents[7].find(':') + 1:]
    return endereco


'''def logradouro(cep):
    return endereco(cep)['logradouro']

def bairro(cep):
    return endereco(cep)['bairro']

def complemento(cep):
    return endereco(cep)['complemento']

def localidade(cep):
    return endereco(cep)['localidade']

def uf(cep):
    return endereco(cep)['uf']

def unidade(cep):
    return endereco(cep)['unidade']

def ibge(cep):
    return endereco(cep)['ibge']'''

