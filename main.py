
from tkinter import filedialog, Tk
from Funciones import Funciones

listaT = [1,56,65,24,23,89]
#dato = ""
gestor = Funciones()

def abrir():
    print("En el metodo abrir")
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

def prueba ():
    txt = abrir()
    if txt is not None:
        dato = txt
        gestor.obtenerData(dato)
       

        
        
    else:
        print("Error lectura")




if __name__ == "__main__":
  
    print("Bienvenido")
    opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Reporte en consola \n 3.Exportar reporte \n 4.Salir \n"))

    

    while opcion != 4:

        if opcion == 1:
            print("Opcion 1")
            prueba()
            
            
        elif opcion == 2:
            print("En 2")
            gestor.ascendente(listaT)
            
            
        elif opcion == 3:
            print("En 3")
            
        else:
            print("Ingrese una opcion valida")
        opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Reporte en consola \n 3.Exportar reporte \n 4.Salir \n"))

