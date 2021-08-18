
from tkinter import filedialog, Tk
from Funciones import Funciones
from Estudiante import Estudiante
from Reporte import Reporte

gestor = Funciones()
report = Reporte()

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
           
            report.valor_minimo_directo(gestor.usuario)
            report.valor_maximo_directo(gestor.usuario)
            report.valor_promedio_directo(gestor.usuario)
            report.valor_descendente_directo(gestor.usuario)
            report.valor_ascendente_directo(gestor.usuario)
            report.valor_reprobados_directo(gestor.usuario)
            report.valor_aprobados_directo(gestor.usuario)


            #report.reporte()
            
        elif opcion == 2:
            gestor.imprimirParametros(gestor.parametros)
            
        elif opcion == 3:
            print("En 3")
            report.reporte()
            
        else:
            print("Ingrese una opcion valida")
        opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Reporte en consola \n 3.Exportar reporte \n 4.Salir \n"))

