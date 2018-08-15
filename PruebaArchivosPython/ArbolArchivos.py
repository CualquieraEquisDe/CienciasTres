from pila import *
from arbol import *
from os import linesep

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)


pila = Pila()
entrada = open("expresion.in.txt")
salida = open("expresion.out.txt", "a")
lista = entrada.readline()
#print(lista)
for a in lista:
    var = str(a.split(" "))
    var = var.replace('\\n', '')
    print(str(var))
    convertir(var, pila)
    out = str(evaluar(pila.desapilar()))
    salida.write(out + linesep)

entrada.close()
salida.close()
