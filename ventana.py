import tkinter as tk
from tkinter import messagebox

def interfaz():
    ventana = tk.Tk()
    ventana.title('Inicio de Sesion')   #Titulo de la ventana
    ventana.geometry('380x200') #Dimension de la ventana (Ancho x Alto)
    e1=tk.Label(ventana,text='Nombre de Usuario',fg='black')
    e1.pack(padx=5,pady=5,ipadx=5,ipady=5)
    entry_user=tk.Entry(ventana)
    entry_user.pack(padx=5,pady=5,ipadx=5,ipady=5)
    e2=tk.Label(ventana,text='Contraseña',fg='black')
    e2.pack(padx=5,pady=5,ipadx=5,ipady=5)
    entry_passw=tk.Entry(ventana)
    entry_passw.pack(padx=5,pady=5,ipadx=5,ipady=5)
    bttn=tk.Button(ventana,text='Enviar',fg='black')
    bttn.pack()

    ventana.mainloop()  #Linea final de la ventana

interfaz()