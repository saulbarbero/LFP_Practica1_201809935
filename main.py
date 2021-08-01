from tkinter import filedialog, Tk

listaT = []

def abrir():
   print("En el metodo abrir")



if __name__ == "__main__":
  
    print("Bienvenido")
    opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Reporte en consola \n 3.Exportar reporte \n 4.Salir \n"))

    

    while opcion != 4:

        if opcion == 1:
            txt = abrir()
            
            
        elif opcion == 2:
            print("En 2")
            
        elif opcion == 3:
            print("En 3")
            
        else:
            print("Ingrese una opcion valida")
        opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Reporte en consola \n 3.Exportar reporte \n 4.Salir \n"))

