class Fragmentos:
    def __init__(self, x=3):
        self.n1= x
    
    def usarWhile(self):
        # ciclo repetitivo 
        vocal= input("Ingrese una vocal: ").lower()
        while vocal not in('a','e','i', 'o', 'u'):
            vocal= input("Ingrese de nuevo una vocal: ").lower()
        print("El caracter ingresado: {} es una vocal" .format(vocal))
        
frag = Fragmentos()
frag.usarWhile()