from tkinter import filedialog, Tk
class Funciones:
    def abrir_funcion(self):
        Tk().withdraw()
        archivo = filedialog.askopenfile(
            title = "Seleccionar un archivo LFP",
            initialdir = "./",
            filetypes = (
                ("archivos LFP", "*.lfp"),
                ("todos los archivos",  "*.*")
            )
        )
        if archivo is None:
            print('No se seleccionó ningun archivo\n')
            return None
        else:
            texto = archivo.read()
            archivo.close()
            print('Lectura exitosa\n')
            return texto
