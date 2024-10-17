

class Window:
    __alto = 200
    __ancho = 100
    __title = "test"
    __resizable = False

    def set_dimensions(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho

    def get_dimensions(self):
        return [self.__alto,self.__alto]

    def allow_resize(self, resizable):
        self.__resizable = resizable

    def get_resiable(self):
        return self.__resizable

    def set_title(self,titulo):
        self.__title= titulo

    def get_title(self):
        return self.__title


    def create_window(self):
        import tkinter as tk
        ventana = tk.Tk()
        ventana.title(self.__title)
        ventana.geometry(f"{self.__alto}x{self.__ancho}")
        ventana.resizable(self.__resizable, self.__resizable)
        ventana.mainloop()