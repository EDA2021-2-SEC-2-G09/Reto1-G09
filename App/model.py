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

import ast
import config as cf
from DISClib.ADT import list as lt
assert cf
from DISClib.Algorithms.Sorting import quicksort as QSort
from DISClib.Algorithms.Sorting import shellsort as ShSort
from DISClib.Algorithms.Sorting import selectionsort as SSort
from DISClib.Algorithms.Sorting import mergesort as MSort
from DISClib.Algorithms.Sorting import insertionsort as ISort
sortingAlgorigthms = [ISort.sort, MSort.sort, SSort.sort, ShSort.sort, QSort.quicksort]

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
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
    catalog['obras'] = lt.newList('ARRAY_LIST')

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




def req1(catalogo, annoInicial, annoFinal):
    instanceCatalogo = catalogo
    instanceCatalogo["autores"]["elements"].sort(key=lambda elem: (float)(elem["BeginDate"]), reverse = True)
    resultado = []
    for i in instanceCatalogo["autores"]["elements"]:
        if (float)(i["BeginDate"])>(float)(annoFinal):
            continue
        if (float)(i["BeginDate"]) < (float)(annoInicial):
            break
        resultado.append(i)
    resultado.reverse()
    return resultado

def req2(catalogo, annoInicial, annoFinal, sortFunction):
    """
    for i in range(lt.size(instanceCatalogo["obras"])):
        if lt.getElement(instanceCatalogo["obras"], i) == '':
            lt.deleteElement(instanceCatalogo["obras"], i)
    """
    instanceCatalogo = catalogo
    months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    def sortingFunc(anno1, anno2):
        anno1use = anno1["DateAcquired"].split("-") if anno1["DateAcquired"].split("-")!=[''] else ["0" for _ in range(3)] #[2020, 10, 02]
        anno2use = anno2["DateAcquired"].split("-") if anno2["DateAcquired"].split("-")!=[''] else ["0" for _ in range(3)]
        firstAnno = (float)(anno1use[0]) + ((months[(int)(anno1use[1])-1] + (float)(anno1use[2]))/365) #2020.344 
        secondAnno = (float)(anno2use[0]) + ((months[(int)(anno2use[1])-1] + (float)(anno2use[2]))/365)
        if((float)(firstAnno)>(float)(secondAnno)):
            return 1
        return 0
    sortingAlgorigthms[(int)(sortFunction)](lst = instanceCatalogo["obras"], cmpfunction = sortingFunc) # ShSort.sort(lst = instanceCatalogo["obras"], cmpfunction = sortingFunc)
    annoInicialUse = annoInicial.split("-") if annoInicial.split("-")!=[''] else ["0" for _ in range(3)] #[1920, 02, 20]
    firstAnno = (float)(annoInicialUse[0]) + ((months[(int)(annoInicialUse[1])-1] + (float)(annoInicialUse[2]))/365)#1920.216
    annoFinalUse = annoFinal.split("-") if annoFinal.split("-")!=[''] else ["0" for _ in range(3)] #[1985, 02, 20]
    lastAnno = (float)(annoFinalUse[0]) + ((months[(int)(annoFinalUse[1])-1] + (float)(annoFinalUse[2]))/365)#1985.216
    resultado = []
    for i in instanceCatalogo["obras"]["elements"]:
        dateAcquiredUse = i["DateAcquired"].split("-") if i["DateAcquired"].split("-")!=[''] else ["0" for _ in range(3)]#[1920, 02, 20]
        dateNICE = (float)(dateAcquiredUse[0]) + ((months[(int)(dateAcquiredUse[1])-1] + (float)(dateAcquiredUse[2]))/365)#1920.216
        if (float)(dateNICE)>(float)(lastAnno):
            continue
        if (float)(dateNICE) < (float)(firstAnno):
            break
        resultado.append(i)
    resultado.reverse()
    #for i in resultado:
    #    print(i["DateAcquired"], dateNICE)
    return resultado


def req3(catalogo, artista):
    instanceCatalogo = catalogo
    artistaInfo = next(elem for elem in instanceCatalogo["autores"]["elements"] if elem["DisplayName"] == artista)
    obrasDelArtista = [elem for elem in instanceCatalogo["obras"]["elements"] if (int)(artistaInfo["ConstituentID"]) in ast.literal_eval(elem["ConstituentID"])] 
    tecnicas = [elem["Medium"] for elem in obrasDelArtista]
    seen = set()
    tecnicasUnicas = []
    for item in tecnicas:
        if item not in seen:
            seen.add(item)
            tecnicasUnicas.append(item)
    tecnicasFrecuencia = {i : 0 for i in tecnicasUnicas}
    for elem in obrasDelArtista:
        tecnicasFrecuencia[elem["Medium"]] += 1
    tecnicasFrecuencia=  {k: v for k, v in sorted(tecnicasFrecuencia.items(), key=lambda item: item[1], reverse=True)}
    resultado = obrasDelArtista
    return resultado, tecnicasFrecuencia


 
    