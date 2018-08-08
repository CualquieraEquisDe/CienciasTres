class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

pila1 = Pila()
pila2 = Pila()

libros = ["GABO", "Cien años de soledad", "Realismo Mágico"]
pila1.apilar(libros)
libros = ["Mario Mendoza", "Diario del fin del mundo", "Drama"]
pila1.apilar(libros)
libros = ["Stephen King", "IT", "Horror"]
pila1.apilar(libros)
libros = ["Ana Frank", "El Diario de Ana Frank", "Autobiografia"]
pila1.apilar(libros)
libros = ["Adolf Hitler", "Mi lucha", "Autobiografia"]
pila1.apilar(libros)

opcion = input("¿Qué libro desea?: ")

def buscar(opcion,p1,p2):
    print(p1.es_vacia( )!= fALSE)
    """  while  p1.es_vacia()!= False:
        var=p1.desapilar
        print (var)
        if var[1] == opcion:
            return var
            break
        else:
            p2.apilar(var)"""

H=buscar(opcion,pila1,pila2)
print(H)

