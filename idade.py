'''
EXPLICANDO O MODULO:
A DATA DEVE SER COLOCADA NO FORMATO DD/MM/AAAA
E RETORNA O ANO, O MES E O DIA QUE A PESSOA TEM DE VIDA
DIA = idade.dia(arg)
MES = idade.mes(arg)
ANO = idade.ano(arg)

##ERROS:
Se o formado digitado for diferente do pedido: Ele dira que a data é incorreta e retorna -1 no braço ano.
Se a data for futura: Ele dira que a data é incorreta e retorna -1 no braço ano.
Se for um dia que o mês não tem: Ele avisa que o mes tem determinado limite e retorna -1 no braço ano.

'''


from datetime import datetime
import calendar

def ano (nascimento):
    dia = (nascimento[0:2])
    if dia in '00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31':
        dia = int(dia)
    else:
        print("\033[1;31mInforme uma data correta!\033[;m")
        return -1
    mes = (nascimento[3:5])
    if mes in '00,01,02,03,04,05,06,07,08,09,10,11,12':
        mes = int(mes)
    else:
        print("\033[1;31mInforme uma data correta!\033[;m")
        return  -1
    ano = int(nascimento[6:10])
    if ano < 1000:
        ano += 2000
    idade_ano = idade_mes = idade_dia = 0

    ## Verifica se a pessoa ja nasceu e se a data é possivel
    if dia > 31 or mes > 12 or (
            ano > datetime.now().year or (ano == datetime.now().year and mes > datetime.now().month) or (
            ano == datetime.now().year and mes == datetime.now().month and dia > datetime.now().day)):
        print("\033[1;31mInforme uma data correta!\033[;m")
        return -1

    ## Verifica se o mês tem a quantidade de dias certo
    elif dia > (calendar.monthrange(ano, mes)[1]):
        print(
            f"O Mês {mes} do ano {ano} não tem {dia} dias e sim {calendar.monthrange(ano, mes)[1]} dias\n\033[1;31mInforme uma data correta!\033[;m")
        return -1

    ## Calcula a sua idade em dia, mes e anos.
    else:
        idade_ano = datetime.now().year - ano
        idade_mes = datetime.now().month - mes
        idade_dia = datetime.now().day - dia
        if idade_dia < 0:
            idade_mes = idade_mes - 1
            idade_dia = calendar.monthrange(ano, mes)[1] + idade_dia
        if idade_mes < 0:
            idade_ano = idade_ano - 1
            idade_mes = 12 + idade_mes
    return idade_ano

def mes (nascimento):
    dia = int(nascimento[0:2])
    mes = int(nascimento[3:5])
    ano = int(nascimento[6:10])
    idade_ano = idade_mes = idade_dia = 0


    ## Calcula a sua idade em dia, mes e anos.
    idade_ano = datetime.now().year - ano
    idade_mes = datetime.now().month - mes
    idade_dia = datetime.now().day - dia
    if idade_dia < 0:
        idade_mes = idade_mes - 1
        idade_dia = calendar.monthrange(ano, mes)[1] + idade_dia
    if idade_mes < 0:
        idade_ano = idade_ano - 1
        idade_mes = 12 + idade_mes
    return idade_mes


def dia (nascimento):
    dia = int(nascimento[0:2])
    mes = int(nascimento[3:5])
    ano = int(nascimento[6:10])
    idade_ano = idade_mes = idade_dia = 0


    ## Calcula a sua idade em dia, mes e anos.
    idade_ano = datetime.now().year - ano
    idade_mes = datetime.now().month - mes
    idade_dia = datetime.now().day - dia
    if idade_dia < 0:
        idade_mes = idade_mes - 1
        idade_dia = calendar.monthrange(ano, mes)[1] + idade_dia
    if idade_mes < 0:
        idade_ano = idade_ano - 1
        idade_mes = 12 + idade_mes
    return idade_dia