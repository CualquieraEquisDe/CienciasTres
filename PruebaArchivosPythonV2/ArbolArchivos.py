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

def escritura(entrada, salida):
    pila = Pila()
    linea = entrada.readlines()

    for a in range(0, len(linea)):
        var = linea[a].strip("\n").split(" ")
        convertir(var, pila)
        out = str(evaluar(pila.desapilar()))
        print (diccionario("a", out))
        #salida.write(out + linesep)

def diccionario(variable, valor):
    dictionary = {}
    dictionary[variable] = valor
    return dictionary

entrada = open("expresion.in.txt")
salida = open("expresion.out.txt", "a")

escritura(entrada, salida)

entrada.close()
salida.close()
