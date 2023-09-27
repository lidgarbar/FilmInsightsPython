# -*- coding: utf-8 -*-
'''
Created on 1 ene. 2021

@author: lidia
'''


from peliculas import*

################################################################
#  Programa principal
################################################################

PELICULAS = recorre_fichero('../data/Dataset_proyecto_FP.csv')

################################################################
#  Funciones auxiliares
################################################################

def mostrar_numerado(coleccion):
    i=0
    for p in coleccion:
        i=i+1
        print (i, p) 
        
###############################################################################################################################
#  Funciones de test
###############################################################################################################################
def test_filtrar_por_genero():
    print('Test de "filtrar_por_genero"')   
    films= filtrar_por_genero(PELICULAS, 'Drama')
    mostrar_numerado(films)
    
#test_filtrar_por_genero()
     
def test_ganancias_sin_repetir():
    print('Test de "ganancias_sin_repetir"')
    films= ganancias_sin_repetir(PELICULAS)
    mostrar_numerado(films)

#test_ganancias_sin_repetir()
    
def test_calcula_media_anyo():
    print('Test de "calcula_media_anyo"')
    films= calcula_media_anyo(PELICULAS, 2009) 
    print(films)

#test_calcula_media_anyo()

def test_calcula_ganancias_genero():
    print('Test de "calcula_ganancias_genero"')
    films= calcula_ganancias_genero(PELICULAS, 'Action')   
    print(films)
    
#test_calcula_ganancias_genero()

def test_peliculas_peores_valoradas():
    print('Test de "peliculas_peores_valoradas"')
    films= peliculas_peores_valoradas(PELICULAS, 2010)
    print(films)

#test_peliculas_peores_valoradas()
    
def test_peliculas_mejores_valoradas():
    print('Test de "peliculas_mejores_valoradas"')
    films= peliculas_mejores_valoradas(PELICULAS, 50)
    print(films)

#test_peliculas_mejores_valoradas()

def test_diccionario_de_genero():
    print('Test de "diccionario_de_genero"')
    films= diccionario_de_genero(PELICULAS, 'Thriller')
    print(films)
 
#test_diccionario_de_genero()
    
def test_diccionario_de_anyo():
    print('Test de "diccionario_de_año"')
    films= diccionario_de_anyo(PELICULAS, 2007)
    print(films)

#test_diccionario_de_anyo()
