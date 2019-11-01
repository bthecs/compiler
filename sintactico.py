import re

## Sintax Password
def sintax_passw(password):
    if len(password) < 8:
        print('Error: La contraseña debe tener al menos 8 caracteres')
        return False
    elif re.search('[0-9]',password) is None:
        print('Error: La contraseña debe tener al menos un digito')
        return False
    elif re.search('[A-Z]',password) is None:
        print('Error: La contraseña debe tener al menos una mayuscula')
        return False
    else:
        return True

## Sintax Username
def sintax_user(username):

    if len(username) < 6 or len(username) > 12:
        print('Error: El nombre de usuario debe tener entre 6 a 12 caracteres')
        return False
    elif re.search('[a-z]|[A-Z]',username) is None:
        print('Error: El nombre de usuario debe tener al menos una letra')
        return False
    elif re.search('[0-9]',username) is None:
        print('Error: El nombre de usuario debe tener al menos un digito')
        return False
    else:
        return True
