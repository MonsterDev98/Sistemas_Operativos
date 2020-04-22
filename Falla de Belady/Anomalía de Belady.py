# -*- coding: utf-8 -

#Código que realiza el algoritmo de colas FIFO y
#se demuestra la anomlía de Belady 

from random import randint

def generador(x): # Función para crear números del 0 al 9 x = Total de peticiones de página
    return [randint(0,9) for _ in range(x)]


def main(l_paginas, frames_totales):
    print '{} '.format(l_paginas)

    cola = []
    fallas = 0

    for numpagina in l_paginas:

        if numpagina in cola:
            pass
        else:
            fallas += 1
            if len(cola) == frames_totales:
                cola.pop() #Retira el útimo elemento de la lista
                cola.insert(0, numpagina) # Pone en la lista el nuevo elemnto
            else:
                cola.insert(0, numpagina)# Pone en lista un nuevo elemento

    return fallas # Retorna las fallas totales


if __name__=="__main__":
    print 'Ingrese el número para generar peticiones de página con num aleatorios -> '
    num = input() # recibe un número que será la cantidad total de peticiones de página a generador

    for j in range(10):
        x = generador(num)
        print 'si tiene 3 frames: , fallas: {}, si tiene 4 frames: , fallas:{}'.format(main(x, 3), main(x, 4))
