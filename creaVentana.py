import tkinter as tk

class window :
    def __init__(self):
        self.__Ancho = 800
        self.__Alto= 600
        self.__realizar= false



def crear_ventana(n, m):

    # Crear la ventana principal

    ventana = tk.Tk()

    ventana.title("Ventana Fija")


    # Establecer el tamaño de la ventana (n x m píxeles)

    ventana.geometry(f"{n}x{m}")


    # Evitar que la ventana sea redimensionable

    ventana.resizable(False, False)


    # Iniciar el bucle principal de la ventana

    ventana.mainloop()


# Dimensiones de la ventana

n = 800  # Ancho en píxeles

m = 600  # Alto en píxeles


# Crear la ventana con las dimensiones especificadas

crear_ventana(n, m)