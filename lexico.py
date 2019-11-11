import re

def lex_passw(cadena):
    alfabeto = '[a-z]|[A-Z]'
    digito = '[0-9]'
    caracter = '[.]|[@]|[ ]'

    pw = re.compile(fr'\b{alfabeto}|{digito}|{caracter}\b')

    for i in cadena:
        if (pw.findall(i)):
            return True
        else:
            return False
        
def lex_user(cadena):
    alfabeto = '[a-z]|[A-Z]'
    digito = '[0-9]'
    caracter = '[.]|[@]|[ ]'

    us = re.compile(fr'\b{alfabeto}|{digito}|{caracter}\b')
    
    for i in cadena:
        if (us.findall(i)):
            return True
        else:
            return False    