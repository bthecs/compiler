from lexico import *
from sintactico import *
import tkinter as tk


def validar():
    info = tk.Tk()
    info.title('Info')
    info.geometry('380x200')

    info1 = tk.Label(info, text='*** Username ***')
    info2 = tk.Label(info, text='')
    info3 = tk.Label(info, text='')
    info1.pack(padx=5, pady=5, ipadx=5, ipady=5)
    info2.pack()
    info3.pack()

    if lex_user(entry_user.get()) == True:
        info2.configure(text='Lexico: Correcto')
        if sintax_user(entry_user.get()) == True:
            info3.configure(text='Sintactico: Correcto')
        else:
            info3.configure(text='Sintactico: Error')
    else:
        info2.configure(text='Lexico: Error')

    info4 = tk.Label(info, text='*** Password ***')
    info5 = tk.Label(info, text='')
    info6 = tk.Label(info, text='')
    info4.pack(padx=5, pady=5, ipadx=5, ipady=5)
    info5.pack()
    info6.pack()

    if lex_passw(entry_passw.get()) == True:
        info5.configure(text='Lexico: Correcto')
        if sintax_passw(entry_passw.get()) == True:
            info6.configure(text='Sintactico: Correcto')
        else:
            info6.configure(text='Sintactico: Error')
    else:
        info5.configure(text='Lexico: Error')

    info.mainloop()


ventana = tk.Tk()
ventana.title('Inicio de Sesion')  # Titulo de la ventana
ventana.geometry('380x200')  # Dimension de la ventana (Ancho x Alto)
e1 = tk.Label(ventana, text='Nombre de Usuario', fg='black')
e1.pack(padx=5, pady=5, ipadx=5, ipady=5)
entry_user = tk.Entry(ventana)
entry_user.pack(padx=5, pady=5, ipadx=5, ipady=5)
e2 = tk.Label(ventana, text='Contraseña', fg='black')
e2.pack(padx=5, pady=5, ipadx=5, ipady=5)
entry_passw = tk.Entry(ventana)
entry_passw.pack(padx=5, pady=5, ipadx=5, ipady=5)
bttn = tk.Button(ventana, text='Enviar', fg='black', command=validar)
bttn.pack()

ventana.mainloop()  # Linea final de la ventana
