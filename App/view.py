"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """
import ast
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from prettytable import PrettyTable



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar Cronologicamente los artistas")
    print("3- Listar Cronologicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por tecnica")


def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Archivos cargados')
        

    elif int(inputs[0]) == 2:
        annoInicial =  input('Ingrese el año inicial: ')
        annoFinal   =  input('Ingrese el año final:  ')
        resultado   =  controller.artchrono(catalog,annoInicial,annoFinal)
        x = PrettyTable()
        x.field_names = resultado[0].keys()
        xd = [0,1,2,-3,-2,-1]
        for i in xd:
            x.add_row(resultado[i].values())
        print("\n\nNumero de artistas en el rango: \n", len(resultado)) #numero de artistas en el rango entregado
        print(x)
       
    elif int(inputs[0]) == 3:
        fechaInicial = input('Ingrese la fecha inicial de la forma año-mes-dia: ')
        fechaFinal   = input('Ingrese la fecha final de la forma año-mes-dia: ')

        f= open(cf.data_dir + "/tableTry.txt","w+")
        resultado = controller.chrono(catalog,fechaInicial, fechaFinal, "3")
        x = PrettyTable()
        print([list(resultado[0].values())[3]])
        print(list(resultado[0].values())[:3] + list(resultado[0].values())[4:6] + [list(resultado[0].values())[3]] + list(resultado[0].values())[10:13]) #0(ObjectID),1(Title),2(ArtistsIDs),4(Medium),5(Dimensions),3(Date),10(DateAcquired),12(URL) [0,1,2,3,4,5,6,7,8,9,10,11,12]
        x.field_names = [*resultado[0]][:3] + [*resultado[0]][4:6] + [[*resultado[0]][3]] + [*resultado[0]][10:13]
        xd = [0,1,2,-3,-2,-1]
        for i in xd:
            artistasArray = []
            print([elem for elem in catalog["autores"]["elements"] if elem["ConstituentID"] == "429"])
            for j in ast.literal_eval(list(resultado[i].values())[2]):
                print(j)
                print(next((elem for elem in catalog["autores"]["elements"] if elem["ConstituentID"] == str(j)))["DisplayName"])
                artistasArray += [next((elem for elem in catalog["autores"]["elements"] if elem["ConstituentID"] == str(j)))["DisplayName"]]
            x.add_row(list(resultado[i].values())[:2] + [[dab for dab in artistasArray]] + list(resultado[i].values())[4:6] + [list(resultado[i].values())[3]] + list(resultado[i].values())[10:13])
        print("\n\nNumero de obras en el rango: \n", len(resultado)) #numero de obras en el rango entregado
        print("\nnumero de obras compradas: \n", len([elem for elem in resultado if ("Purchase" in elem["CreditLine"]) or ("purchase" in elem["CreditLine"])]))
        f.write(str(x))
        f.close()
        
    elif int(inputs[0]) == 4:
        try:
            artista = input('Ingrese el nombre de la artista que desea buscar: ')
            obras, tecnicas = controller.medium(catalog,artista)
            print(tecnicas)
            x = PrettyTable()
            x.field_names = ["MediumName", "Count"]
            count = 0
            for tech, uses in tecnicas.items(): # (nombre, 3) tech = nombre uses = 3
                x.add_row([tech, uses])
                count += 1
                if count == 5:
                    break
            print(x)
            x = PrettyTable()
            print("\n\nHis/Her most used technique is:", [*tecnicas][0], "with", list(tecnicas.values())[0], "pices")
            oCTMU = [elem for elem in obras if elem["Medium"]==[*tecnicas][0]] #obrasConTecnicaMasUtilizada
            listaUwU = ["ObjectID", "Medium", "Date", "Dimensions", "DateAcquired", "Department", "Classification", "URL"]
            x.field_names = listaUwU
            for i in oCTMU:
                dab = []
                for j in listaUwU:
                    dab += [i[j]]
                x.add_row(dab)
            f= open(cf.data_dir + "/tableTry.txt","w+")
            f.write(str(x))
            f.close()
            print('La otra tabla se encuentra en el tableTry.txt')
        except:
            print('El artista buscado no existe')

    else:
        sys.exit(0)
sys.exit(0)