
from Estudiante import Estudiante 


minimo = ""

class Reporte:
    def __init__(self):
        var = 0
        
    
    def valor_minimo (self,lista):
        valor_max = None
        
        for x in lista:
            if (valor_max is None or x.nota < valor_max):
                valor_max = x.nota
                nom = x.nombre
        print("Nota Minima\n","El estudiante ",nom," tiene una nota de: ",valor_max)
        minimo="Nota Minima\n","El estudiante "+(nom)+" tiene una nota de: "+(valor_max)
        print("\n")
        return minimo
    
    def valor_maximo (self,lista):
        valor_max = None
        for x in lista:
            if (valor_max is None or x.nota > valor_max):
                valor_max = x.nota
                nom = x.nombre
        print("\n")
        print("Nota Maxima\n","El estudiante ",nom," tiene una nota de: ",valor_max)
        print("\n")
    
        
    def promedio(self,lista):
        promedio=0
        total=0
        for i in range (len(lista)):
            total+=float(lista[i].nota.strip())
        
        promedio=total/float(len(lista))
        print("\n")
        print ("el promedio de notas es de:",promedio)
        print("\n")

    
    def descendente(self,lista):

        for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1].nota > lista[j].nota):
                    aux=lista[j].nota;
                    aux_nombre = lista[j].nombre;


                    lista[j].nota=lista[j+1].nota;
                    lista[j].nombre=lista[j+1].nombre;

                    lista[j+1].nota=aux;
                    lista[j+1].nombre=aux_nombre;
        print("\n")
        self.printUser (lista)
        print("\n")
        return(lista)

    def ascendente(self,lista):
        for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1].nota < lista[j].nota):
                    aux=lista[j].nota;
                    aux_nombre = lista[j].nombre;


                    lista[j].nota=lista[j+1].nota;
                    lista[j].nombre=lista[j+1].nombre;

                    lista[j+1].nota=aux;
                    lista[j+1].nombre=aux_nombre;
        print("\n")
        self.printUser (lista)
        print("\n")
        return(lista)

    def printUser(self,lista):
        for x in lista:
            print(x.nombre,' ',x.nota)
    
    def reprobados(self,lista):
        reprobados=0
        total=0
        for i in range (len(lista)):
            if (float(lista[i].nota) < 61):
                reprobados=reprobados+1
                total=reprobados
        print("\n")
        print ("Los estudiantes reprobados son: ",total)
        print("\n")

    def aprobados(self,lista):
        reprobados=0
        total=0
        for i in range (len(lista)):
            if (float(lista[i].nota) >= 61):
                reprobados=reprobados+1
                total=reprobados
        print("\n")
        print ("Los estudiantes aprobados son: ",total)
        print("\n")



    def reporte(self):
        #mandar lista de usuarios y lista de parametros
        #ASC,DESC,AVG,MIN,MAX,APR,REP
        

        f = open('reporte.html','w')

        mensaje = """<html>
        <head>Reporte</head>
        <body><p>sustitucion</p></body> 
        </html>"""
        x=mensaje.replace('sustitucion',minimo)
        f.write(x)
        f.close()
        print("Reporte creado con Exito")