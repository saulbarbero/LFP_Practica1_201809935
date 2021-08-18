from Estudiante import Estudiante 
import re
from Reporte import Reporte

class Funciones:
    def __init__(self):
         
        self.nombreCurso = ''
        self.nombreNombre = ''
        self.nombreNota = ''
        self.parametro = ''
        self.usuario = []
        self.parametros=[]



    def imprimirParametros(self,lista_parametros):
        rep = Reporte()
        #ASC,DESC,AVG,MIN,MAX,APR,REP
        for x in lista_parametros:
            if (x==" ASC" or x=="ASC" or x==" ASC "):
                rep.ascendente(self.usuario)
            elif (x=="DESC"):
                rep.descendente(self.usuario)
            elif (x=="AVG"):
                rep.promedio(self.usuario)
            elif (x=="MIN"):
                rep.valor_minimo(self.usuario)
            elif (x=="MAX"):
                rep.valor_maximo(self.usuario)
            elif (x=="APR"):
                rep.reprobados(self.usuario)
            elif (x=="REP"):
                rep.aprobados(self.usuario)
            else:
                print("Error")


    def valor_imprimirParametros_directo(self,lista_parametros):
        rep = Reporte()
        #ASC,DESC,AVG,MIN,MAX,APR,REP
        for x in lista_parametros:
            if (x==" ASC" or x=="ASC" or x==" ASC "):
                rep.valor_ascendente_directo(self.usuario)
            elif (x=="DESC"):
                rep.valor_descendente_directo(self.usuario)
            elif (x=="AVG"):
                rep.valor_promedio_directo(self.usuario)
            elif (x=="MIN"):
                rep.valor_minimo_directo(self.usuario)
            elif (x=="MAX"):
                rep.valor_maximo_directo(self.usuario)
            elif (x=="APR"):
                rep.valor_reprobados_directo(self.usuario)
            elif (x=="REP"):
                rep.valor_aprobados_directo(self.usuario)
            else:
                print("Error en llenar HTML")
    

        

    def obtenerData(self,data):
    
        aux = ''
        posicion = 1
        estado = 1 #curso
        for x in data:
            if(estado==0):
                if(x == ' ' or x == '<' or x == '>' or x == ','):
                    pass
                elif(x =='}'):
                    estado =4
                else:
                    if(x == '"'):
                        estado = 2
                    elif (x== ';'):
                        estado = 3
            elif(estado==1):
                
                if (x == '=' ):
                    self.nombreCurso = aux
                    estado = 0
                    aux = ''
                 
                    
                else:
                    aux += x 
            elif(estado==2):
                if (x == '"' ):
                    self.nombreNombre = aux
                    estado = 0
                    aux = ''
                    
                    
                else:
                    aux += x 
            elif(estado == 3):
                if (x == '>' ):
                    self.usuario.append(Estudiante(self.nombreNombre,aux))
                    estado = 0
                    aux = ''
                    
                else:
                    aux += x 
            elif(estado== 4):
                if (x == ',' ):
                    self.parametros.append(aux)
                    aux = ''
                else:
                    aux += x 


        self.parametros.append(aux) #Aqui guardo el ultimo parametro ingresado
