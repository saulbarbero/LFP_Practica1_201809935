
from Estudiante import Estudiante 
import re
curso = ''
nombre = ''
nota = ''
parametro = ''
class Funciones:
    def __init__(self):
        self.usuario = []
        self.usuario.append(Estudiante("Saul","20"))
        
    

    def valor_minimo (self,lista):
        valor_max = None
        for x in lista:
            if (valor_max is None or x < valor_max):
                valor_max = x

        print(valor_max)

    def valor_maximo (self,lista):
        valor_max = None
        for x in lista:
            if (valor_max is None or x > valor_max):
                valor_max = x

        print(valor_max)

    def promedio(self,lista):
        promedio=0

        promedio=sum(lista)/float(len(lista))
            
        print (promedio)

    def descendente(self,lista):

        lista_desc = [0 for i in range(len(lista))]
        count = 0

        for x in lista:
            posicion = 0

            while (posicion < count) and (x < lista_desc[posicion]):
                posicion += 1

            for pos2 in range(count, posicion, -1):
                lista_desc[pos2] = lista_desc[pos2 - 1]

            lista_desc[posicion] = x
            count += 1

        print(lista_desc)

        return lista_desc

    def ascendente(self,lista):
        for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1] < lista[j]):
                    aux=lista[j];
                    lista[j]=lista[j+1];
                    lista[j+1]=aux;
        print (lista)
        return(lista)

    """ def datos(self,data):
        

        aux = ''
        estado = 'c'
        posicion = 1

        for x in data:
            if estado == 'c':
                #Reconocer curso
                if x == '=':
                    estado = 'm'
                    curso = aux
                    aux = ''
                else:
                    aux += x
                
                posicion += 1

            elif estado == 'm':
                if x == '{' :
                    if x == '\n' :
                        pass
                    elif x == '<' :
                        pass
                    elif x == '"' :
                        estado = 'n'
                        nombre = aux
                        aux = ''
                    else:
                        aux += x
            elif estado == 'n':
                if x == '"':
                    pass
                elif x == ';' :
                    estado = 'p'
                    nota = aux
                    aux = ''
                else:
                        aux += x
            elif estado == 'p':
                if(posicion == len(data)):
                    aux += x
                    parametro = aux
                    aux = ''
                else:
                    aux += x

                posicion += 1
            else:
                return None"""

    def obtenerData(self,data):
        #curso = c
        #nombre = nom
        #nota = no
        #ingreso del objeto = obj
        #parametro = c
        aux = ''
        posicion = 1
        estado = 'c' #curso
        nombreCurso = ' '
        nombreNombre = ' '
        nombreNota = ' '
        parametro = ' '

        for x in data:
            if estado == 'c':
                if (x != ' ' ) or (x != '=' ):
                    aux += x
                else:
                    nombreCurso = aux
                    estado = 'nom'
                    aux = ''
                    #return nombreCurso
            elif estado == 'nom':
                if (x != '{') or (x != '\n') or (x != '<') or (x != '"'):
                    pass
                else:
                    nombreNombre = aux
                    estado = 'no'
                    aux = ''
            elif estado == 'no':
                if  ( x != '"') or(x != ';'):
                    pass
                else:
                    nombreNota = aux
                    estado = 'obj'
                    aux = ''
            elif estado == 'obj':
                self.usuario.append(Estudiante(nombreNombre,nombreCurso))
                nombreNombre = ''
                nombreNota = ''
                estado = 'c'
            elif estado == 'c':
                if (x != '>') or (x != ',') or (x != '}') or (x != '\n'):
                    pass
                else:
                    parametro = aux
                    estado = ''
                    aux = ''
            else:
                return None

                


                    






                    





                        




