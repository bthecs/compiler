from lexico import *
from sintactico import *

user = input('Ingrese usuario: ')
passw = input('Ingrese contraseña: ')

print('\n*** Username')
if lex_user(user) == True:
    print('Lexico: Correcto')
    if sintax_user(user) == True:
        print('Sintax: Correcto')
    else:
        print('Sintax: Error')
else:
    print('Lexico: Error')

print('\n*** Password')
if lex_passw(passw) == True :
    print('Lexico: Correcto')
    if sintax_passw(passw) == True:
        print('Sintax: Correcto')
    else:
        print('Sintax: Error')
else:
    print('Lexico: Error')