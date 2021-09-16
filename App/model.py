"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
assert cf
from DISClib.Algorithms.Sorting import quicksort as QSort
from DISClib.Algorithms.Sorting import shellsort as ShSort
from DISClib.Algorithms.Sorting import selectionsort as SSort
from DISClib.Algorithms.Sorting import mergesort as MSort
from DISClib.Algorithms.Sorting import insertionsort as ISort
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'autores': None,
               'obras': None}

    catalog['autores'] = lt.newList('ARRAY_LIST')
    catalog['obras'] = lt.newList('ARRAY_LIST',cmpfunction= req2)

    return catalog

# Funciones para agregar informacion al catalogo

def addAutor(catalog, autor):
    """
    Adiciona un autor a la lista de autores
    """
    lt.addLast(catalog['autores'],autor)
    


def addObras(catalog, obra):
    """
    Adiciona una obra a la lista de autores
    """
    lt.addLast(catalog['obras'],obra)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
sortingAlgorigthms = [ISort.sort, MSort.sort, SSort.sort, ShSort.sort, QSort.quicksort]

def req2(catalogo, annoInicial, annoFinal, sortFunction):
    """
    for i in range(lt.size(instanceCatalogo["obras"])):
        if lt.getElement(instanceCatalogo["obras"], i) == '':
            lt.deleteElement(instanceCatalogo["obras"], i)
    """
    start_time = time.process_time()
    instanceCatalogo = catalogo
    months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    def sortingFunc(anno1, anno2):
        anno1use = anno1["DateAcquired"].split("-") if anno1["DateAcquired"].split("-")!=[''] else ["0" for _ in range(3)] #[2020, 10, 02]
        anno2use = anno2["DateAcquired"].split("-") if anno2["DateAcquired"].split("-")!=[''] else ["0" for _ in range(3)]
        firstAnno = (int)(anno1use[0]) + ((months[(int)(anno1use[1])-1] + (int)(anno1use[2]))/365) #2020.344 
        secondAnno = (int)(anno2use[0]) + ((months[(int)(anno2use[1])-1] + (int)(anno2use[2]))/365)
        if((int)(firstAnno)>(int)(secondAnno)):
            return 1
        return 0
    sortingAlgorigthms[(int)(sortFunction)](lst = instanceCatalogo["obras"], cmpfunction = sortingFunc) # ShSort.sort(lst = instanceCatalogo["obras"], cmpfunction = sortingFunc)
    annoInicialUse = annoInicial.split("-") if annoInicial.split("-")!=[''] else ["0" for _ in range(3)] #[1920, 02, 20]
    firstAnno = (int)(annoInicialUse[0]) + ((months[(int)(annoInicialUse[1])-1] + (int)(annoInicialUse[2]))/365)#1920.216
    annoFinalUse = annoFinal.split("-") if annoFinal.split("-")!=[''] else ["0" for _ in range(3)] #[1985, 02, 20]
    lastAnno = (int)(annoFinalUse[0]) + ((months[(int)(annoFinalUse[1])-1] + (int)(annoFinalUse[2]))/365)#1985.216
    resultado = []
    for i in instanceCatalogo["obras"]["elements"]:
        dateAcquiredUse = i["DateAcquired"].split("-") if i["DateAcquired"].split("-")!=[''] else ["0" for _ in range(3)]#[1920, 02, 20]
        dateNICE = (int)(dateAcquiredUse[0]) + ((months[(int)(dateAcquiredUse[1])-1] + (int)(dateAcquiredUse[2]))/365)#1920.216
        if (int)(dateNICE)>(int)(lastAnno):
            continue
        if (int)(dateNICE) < (int)(firstAnno):
            break
        resultado.append(i)
    resultado.reverse()
    for i in resultado:
        print(i["DateAcquired"])

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return resultado,elapsed_time_mseg