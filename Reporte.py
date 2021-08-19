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
        print("\n")

    def valor_maximo (self,lista):
        valor_max = None
        for x in lista:
            if (valor_max is None or x.nota > valor_max):
                valor_max = x.nota
                nom = x.nombre

        print("Nota Maxima\n","El estudiante ",nom," tiene una nota de: ",valor_max)
        print("\n")
    
        
    def promedio(self,lista):
        promedio=0
        total=0
        for i in range (len(lista)):
            total+=float(lista[i].nota.strip())
        
        promedio=total/float(len(lista))
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

        #print("Lista descendente:\n")
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
            
        #print("Lista ascendente:\n")
        self.printUser (lista)
        print("\n")
        return(lista)

    def printUser(self,lista):
        for x in lista:
            print(x.nombre+' '+x.nota)

    def reprobados(self,lista):
        reprobados=0
        total=0
        for i in range (len(lista)):
            if (float(lista[i].nota) < 61):
                reprobados=reprobados+1
                total=reprobados
        
        print ("Los estudiantes reprobados son: ",total)
        print("\n")
        

    def aprobados(self,lista):
        reprobados=0
        total=0
        for i in range (len(lista)):
            if (float(lista[i].nota) >= 61):
                reprobados=reprobados+1
                total=reprobados
        
        print ("Los estudiantes aprobados son: ",total)
        print("\n")

    

    


#-----------------------------------------------------------------------------------------
    def valor_minimo_directo (self,lista):
            valor_max = None
            
            for x in lista:
                if (valor_max is None or x.nota < valor_max):
                    valor_max = x.nota
                    nom = x.nombre

            #print("Nota Minima\n","El estudiante ",nom," tiene una nota de: ",valor_max)
            self.valor_minimo= valor_max
            self.valor_nom = nom
    
    def valor_maximo_directo (self,lista):
        valor_max = None
        for x in lista:
            if (valor_max is None or x.nota > valor_max):
                valor_max = x.nota
                nomm = x.nombre

        self.valor_maximo= valor_max
        self.valor_nom_max = nomm
    
        
    def valor_promedio_directo(self,lista):
        promedio=0
        total=0
        for i in range (len(lista)):
            total+=float(lista[i].nota.strip())
        
        promedio=total/float(len(lista))
        self.valor_promedio = promedio

    
    def valor_descendente_directo(self,lista):

        for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1].nota > lista[j].nota):
                    aux=lista[j].nota;
                    aux_nombre = lista[j].nombre;


                    lista[j].nota=lista[j+1].nota;
                    lista[j].nombre=lista[j+1].nombre;

                    lista[j+1].nota=aux;
                    lista[j+1].nombre=aux_nombre;
        

        #self.printUser_directo (lista)
        self.valor_des = lista
        

    def valor_ascendente_directo(self,lista):
        for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1].nota < lista[j].nota):
                    aux=lista[j].nota;
                    aux_nombre = lista[j].nombre;


                    lista[j].nota=lista[j+1].nota;
                    lista[j].nombre=lista[j+1].nombre;

                    lista[j+1].nota=aux;
                    lista[j+1].nombre=aux_nombre;

        self.valor_asc = lista
        #self.printUser_directo (lista)
        

    def printUser_directo(self,lista):
        for x in lista:
            print(x.nombre+' '+x.nota)

    def valor_reprobados_directo(self,lista):
        reprobados=0
        total=0
        for i in range (len(lista)):
            if (float(lista[i].nota) < 61):
                reprobados=reprobados+1
                total=reprobados
        
        self.valor_reprobados = total
        

    def valor_aprobados_directo(self,lista):
        reprobados=0
        total=0
        for i in range (len(lista)):
            if (float(lista[i].nota) >= 61):
                reprobados=reprobados+1
                total=reprobados
        
        self.valor_aprobados = total

#---------------------------------------------------------------------------
    def reporte(self):
        #mandar lista de usuarios y lista de parametros

        f = open('reporte.html','w')

        mensaje = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <meta http-equiv="X-UA-Compatible" content="ie=edge" />
                <title>Reporte-LFP</title>

                <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:400,600" />
                <link rel="stylesheet" href="html/css/all.min.css" />
                <link rel="stylesheet" href="html/css/bootstrap.min.css" />
                <link rel="stylesheet" href="html/css/templatemo-style.css" />
            </head>

            <body id="servicesPage">
                
                <div class="container-fluid">
                    <div class="row tm-brand-row">
                    <div class="col-lg-4 col-11">
                        <div class="tm-brand-container tm-bg-white-transparent">
                        <i class="fas fa-5x fa-clipboard-list"></i>
                        <div class="tm-brand-texts">
                            <h1 class="text-uppercase tm-brand-name">LFP</h1>
                            <p class="small">Reporte</p>
                        </div>
                        </div>
                    </div>
                    <div class="col-lg-8 col-1">
                        <div class="tm-nav">
                        
                        </div>
                    </div>
                    </div>

                    <!-- Services header -->
                    <section class="row" id="tmServices">
                    <div class="col-12">
                        <div class="parallax-window tm-services-parallax-header"
                            data-parallax="scroll"
                            data-z-index="101"
                        >

                            <div class="tm-bg-black-transparent text-center tm-services-header">
                                <h2 class="text-uppercase tm-services-page-title">Resultados</h2>
                                <p class="tm-services-description mb-0 small">
                                    <p>Nota Minima</p>
                        <p>La nota minima es de aaa y la nota es de ssd</p>
                        <p> </p>
                        <p>Nota Maxima</p>
                        <p>La nota maxima es de bbb y la nota es de ccc</p>
                        <p> </p>
                        <p>Promedio</p>
                        <p>El promedio de notas es de ddd</p>
                        <p> </p>
                        <p>Aprobados</p>
                        <p>El numero de estudiantes aprobados es de ggg</p>
                        <p> </p>
                        <p>Reprobados</p>
                        <p>El numero de estudiantes reprobados es de hhh</p>
                        <p> </p>
                        <p>Lista Descendente</p>
                        <p>eee</p>
                        <p> </p>
                        <p>Lista Ascendente</p>
                        <p>fff</p>
                                </p>
                            </div>
                        </div>
                    </div>  
                            
                    </section>

                    <!-- Page footer -->
                    <footer class="row">
                    <p class="col-12 text-white text-center tm-copyright-text">
                        Copyright &copy; 2021 Saúl Alfredo Barbero Contreras.
                    </p>
                    </footer>
                </div>
                <!-- .container-fluid -->
                
            </body>
            </html>"""
    
        mensaje = mensaje.replace("ssd",str(self.valor_minimo))
        mensaje = mensaje.replace("aaa",str(self.valor_nom))
        mensaje = mensaje.replace("bbb",str(self.valor_nom_max))
        mensaje = mensaje.replace("ccc",str(self.valor_maximo))
        mensaje = mensaje.replace("ddd",str(self.valor_promedio))
        #mensaje = mensaje.replace("eee",str(self.valor_des))
        #mensaje = mensaje.replace("fff",str(self.valor_asc))
        mensaje = mensaje.replace("ggg",str(self.valor_aprobados))
        mensaje = mensaje.replace("hhh",str(self.valor_reprobados))
        #print(mensaje)
        f.write(mensaje)
        f.close()
        print("Reporte creado con Exito")


   