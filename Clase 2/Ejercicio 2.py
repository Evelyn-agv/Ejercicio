class Datos():
    c=0   # variables de clases 
    
    def __init__(self, informar="Inicio"):
        self.info=informar   #variables de instancia
    
    def datoPersonal(self):
        #Númericos
        edad, peso= 20, 70.5 
        #Strings  
        nombres= 'Evelyn García'  
        ciudad= "Milagro"
        sexo= "Femenino"
        civil= True
        
        """COLECCIONES"""
        # tuplas= () datos tipo inmutables
        ingresado= ('diadema','262651','carolina@gmail.com', True)
        # ingresado[3]= "unemi"  #comporbación que su valor no cambia
        # listas= [] datos tipo mutables
        materias=['Python', 'PHP', 'POO']
        materias[2]= "Java"  
        materias.append("C++") #agregar al final
        # diccionarios={} colección clave: valor tipo json
        docente= {'nombre':'Daniel', 'edad':50, 'universidad':'UNEMI', 'fac':'faci'}
        docente['nombre']= "Mariela"
        #Imprimir
        print("Mi nombre es {}, tengo {} años, vivo en {}" .format(nombres,edad,ciudad))
        print(ingresado, ingresado[1], ingresado[0:-1], ingresado[-2])
        print(materias, materias[1:], materias[:1], materias[::], materias[:-2])
        print(docente, docente['nombre'])

if __name__ == '__main__':
    respuesta= Datos() #creación del objeto
    print(respuesta.info)
    respuesta.datoPersonal()




