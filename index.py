
from tkinter import ttk
from tkinter import *

import sqlite3   #importación libreria para conectar con sqlite3

class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Aplicación de productos')

        frame = LabelFrame(self.wind, text = "Ingresa un nuevo producto")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        Label(frame, text='Nombre: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)

        Label(frame, text="Precio: ").grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        #boton agregar producto
        ttk.Button(frame, text="guardar producto").grid(row=3, columnspan=2, sticky= W + E)

if __name__=='__main__':

    window = Tk()
    app = Product(window)
    window.mainloop()

