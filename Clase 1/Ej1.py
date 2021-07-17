#Boolean
# tuplas= () datos tipo inmutables
usuario= ('diadema','262651','carolina@gmail.com', True)
usuario[3]= "unemi"  #comporbación que su valor no cambia
# listas= [] datos tipo mutables
materias=['Python', 'PHP', 'POO']
materias[2]= "Java"  
materias.append("C++") #agregar al final
# diccionarios={} colección clave: valor tipo json
docente= {'nombre':'Daniel', 'edad':50, 'universidad':'UNEMI', 'fac':'faci'}
#Imprimir
#print("Mi nombre es {}, tengo {} años" .format(nombres,edad))
print(usuario,materias, docente)

