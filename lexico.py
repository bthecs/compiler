import re

def lex_passw(cadena):
    alfabeto = '[a-z]|[A-Z]'
    digito = '[0-9]'
    caracter = '[.]|[@]|[ ]'

    pw = re.compile(fr'\b{alfabeto}|{digito}|{caracter}\b')

    retorno = True

    for i in cadena:
        if (pw.findall(i)):
            pass
        else:
            retorno = False
    return retorno
        
def lex_user(cadena):
    alfabeto = '[a-z]|[A-Z]'
    digito = '[0-9]'

    us = re.compile(fr'\b{alfabeto}|{digito}\b')
    
    retorno = True

    for i in cadena:
        if (us.findall(i)):
            pass
        else:
            retorno = False
    return retorno