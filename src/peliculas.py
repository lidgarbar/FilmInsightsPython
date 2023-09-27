# -*- coding: utf-8 -*-
'''
Created on 1 ene. 2021

@author: lidia


En este proyecto trabajaremos con datos extraidos de Kaggle (www.kaggle.com)
correspondientes a las peliculas estrenadas entre los anyos de 2007 y 2011. Los registros con
los que obraremos contienen diversas informaciones de las peliculas que nos permitiran
elaborar una serie de funciones utiles para explorar los datos de los que disponemos

CONJUNTO DE DATOS:
------------------
El proyecto incluye un conjunto de datos en formato CSV llamado "Dataset_proyecto_FP.csv" ubicado 
en la carpeta "data" del proyecto.
Cada registro del fichero de entrada ocupa una linea y contiene siete informaciones separadas por
puntos y comas sobre las peliculas: el titulo, el genero, las valoraciones de Rotten Tomatoes, las 
valoraciones de la audiencia, las ganancias en millones de dolares, el anyo de estreno y la fecha de 
estreno.

FUNCIONES A IMPLEMENTAR:
------------------------
BLOQUE 1
    -recorre_fichero(fichero):
        lee el fichero csv y devuelve una lista de tuplas con nombre
BLOQUE 2
    1.-filtrar_por_genero(peliculas, genero):
        recibe una lista de tuplas y devuelve otra con solo los registros que coincidan con 
        el genero recibido como parametro
    4.-ganancias_sin_repetir(peliculas):
        recibe una lista de tuplas y devuelve otra lista con todos los campos de los registros
        cuyas ganancias no sean iguales
BLOQUE 3
    3.-calcula_media_anyo(peliculas, anyo):
        calcula la media de las valoraciones de los registros cuyo anyo coincida con el seleccionado
    2.-calcula_ganancias_genero(peliculas, genero):
        calcula las ganancias totales de los registros cuyo genero sea el elegido como parametro
BLOQUE 4
    2.-peliculas_peores_valoradas(peliculas, anyo):
        devuelve una lista de los registros que tenga una calificacion menor al 20% y cuyo anyo de estreno
        coincida con el seleccionado como parametro
BLOQUE 5
    1.-peliculas_mejores_valoradas(peliculas, ranking)
        recibe una lista y un parametro ranking (que va desde el 1 al 100) y devuelve otra lista con los 
        registros mejores valorados ordenados en un ranking marcado por el parametro
BLOQUE 6
    1.-diccionario_de_genero(peliculas, genero):
        calcula un diccionario {genero:[titulo, anyo, ganancias]}
    2.-diccionario_de_anyo(peliculas, anyo):
        calcula un diccionario {anyo:[valoracion audiencia, valoracion Rotten Tomatoes]} de las peliculas cuyas 
        claves cumplan determinada condicion
 
'''
import csv
import operator
from collections import namedtuple


fichero = namedtuple('fichero','titulo, genero,valoraciones_Rotten, valoraciones_audiencia,ganancias, anyo, fecha')
###############################################################################################################################

def recorre_fichero(fichero):
    '''
    lee el fichero csv y devuelve una lista de tuplas con nombre
    
    ENTRADA
        -fichero: nombre del fichero de entrada -> str
    
    SALIDA
        -peliculas: lista de tuplas (titulo, genero, valoraciones Rotten Tomatoes, valoraciones audiencia, ganancias, anyo, fecha) -> 
            -> ([str, str, int, int, int, int, datetime])
    '''

    peliculas=[ ]
    with open (fichero, encoding="utf-8") as f:
        lineas= csv.reader(f)
        next(lineas)
        for linea in lineas:
            
            registro=linea[0].replace(" ;",",")                 #corregimos unos espacios que nos daban error en comas
            registro=registro.replace(";",",")                  #cambiamos el resto de puntos y comas en comas
              
            lista=registro.split(',')                           #dividimos cada linea por las comas 
                    
            titulo=lista[0]                                     #asignamos los valores segun el dato
            genero=lista[1]                                     #''
            valoraciones_Rotten=int(lista[2])                   #''
            valoraciones_audiencia=int(lista[3])                #''
            ganancias=int(lista[4])                             #''
            anyo=int(lista[5])                                  #''
            fecha=lista[6]                                      #asignamos los valores segun el dato
               
            tupla = (titulo ,genero ,valoraciones_Rotten ,valoraciones_audiencia ,ganancias ,anyo ,fecha)   #metemos los datos en una lista
            
            peliculas.append(tupla)             

    return peliculas





###############################################################################################################################

###############################################################################################################################

def filtrar_por_genero(peliculas, genero):
    '''
    recibe una lista de tuplas y devuelve otra con solo los registros que coincidan con el genero recibido como parametro
    
    ENTRADA
        -peliculas: lista de tuplas (titulo, genero, valoraciones Rotten Tomatoes, valoraciones audiencia, ganancias, anyo, fecha) -> 
            -> ([str, str, int, int, int, int, datetime])
        - genero: del que se seleccionaran los registros -> str
    
    SALIDA
        -lista de tuplas (titulo, anyo, ganancias, fecha) -> ([str, int, int, datetime])
    '''
    lista=[]

    for linea in peliculas:
        if linea[1]==genero:                                 #si coincide el genero seleccionado
            tupla=(linea[0],linea[4], linea[5], linea[6])    #mete el titulo, ganancias, anyo y fecha en una lista                                  
            lista.append(tupla)     
    return lista




###############################################################################################################################

###############################################################################################################################

def ganancias_sin_repetir(peliculas):
    '''    
     recibe una lista de tuplas y devuelve otra lista con todos los campos de los registros
     cuyas ganancias no sean iguales
     
     ENTRADA
        -peliculas: lista de tuplas (titulo, genero, valoraciones Rotten Tomatoes, valoraciones audiencia, ganancias, anyo, fecha) -> 
            -> ([str, str, int, int, int, int, datetime])
            
     SALIDA
        -lista de tuplas (titulo, genero, valoraciones Rotten Tomatoes, valoraciones audiencia, anyo, fecha)->
            ->([str, str, int, int, int, int, datetime])
    '''



    unico = []
    
    lista=[]
    
    for linea in peliculas:                                                                                                  
        if linea[4] not in unico:                                               #si las ganancias no están en la lista unico
            tupla=(linea[4])                                                    #se meten las ganacias en la lista unico
            tupla2=(linea[0],linea[2],linea[3],linea[5],linea[6])               #y se meten los datos (Titulo, genero, valoraciones...) en otra lista  
            unico.append(tupla)
            lista.append(tupla2)           
   
    return lista

###############################################################################################################################

###############################################################################################################################

def calcula_media_anyo(peliculas, anyo):
    '''
    calcula la media de las valoraciones de los registros cuyo anyo coincida con el seleccionado
    
    ENTRADA
        -peliculas: lista de tuplas (titulo, genero, valoraciones Rotten Tomatoes, valoraciones audiencia, ganancias, anyo, fecha) -> 
            -> ([str, str, int, int, int, int, datetime])
        -anyo: del que se seleccionaron los registros -> int
    
    SALIDA
        -lista de tuplas (anyo, media) -> ([int, int])
    '''
    lista=[]


    for linea in peliculas:          
        if linea[5]==anyo:                       #Si coincide con el año
            lista.append(int(linea[2]))          #se ponen la valoracion en una lista
            sumatotal=sum(lista)                 #sumamos los valores de la lista
            longitud=len(lista)                  #vemos cuantos valores hay en la lista
            media=sumatotal//longitud            #calculamos la media sin decimales
            tupla=(anyo, media)                  #se meten el anyo y la media en una lista de tuplas

    return tupla

             
    
###############################################################################################################################

###############################################################################################################################

def calcula_ganancias_genero(peliculas, genero):
    '''
    calcula las ganancias totales de los registros cuyo g�nero sea el elegido como parametro
    
    ENTRADA
        -peliculas: lista de tuplas (titulo, genero, valoraciones Rotten Tomatoes, valoraciones audiencia, ganancias, anyo, fecha) -> 
            -> ([str, str, int, int, int, int, datetime])
        - genero: del que se seleccionaron los registros -> str
        
    SALIDA
        -lista de tuplas (genero, ganancias_totales) -> ([str, int])
    '''
    lista=[]

    for linea in peliculas:
        if linea[1]==genero:                        #si el genero coincide con el seleccioando
            lista.append(linea[4])                  #se añade las ganancias a una lista
            ganancias_totales=sum(lista)            #se suman los valores de la lista
            tupla=(genero, ganancias_totales)       #se mete el genero y el valor de la suma en una lista de tuplas

    return tupla



###############################################################################################################################

###############################################################################################################################

def peliculas_peores_valoradas(peliculas, anyo):
    '''
    devuelve una lista de los registros que tenga una calificacion menor al 20% y cuyo anyo de estreno
    coincida con el seleccionado como parametro
    
    ENTRADA
        -peliculas: lista de tuplas (titulo, genero, valoraciones Rotten Tomatoes, valoraciones audiencia, ganancias, anyo, fecha) -> 
            -> ([str, str, int, int, int, int, datetime])
        -anyo: del que se seleccionaron los registros -> int
        
    SALIDA
        -peores_peliculas: lista de tuplas (anyo, titulos) de los registros con una calificaion menor al 20% -> ([int, str])
    '''
    titulos=[]
   
    for linea in peliculas:                    
        if linea[3]<20 and linea[5]==anyo:     #si la calificacion es menor al 20% y coincide el año 
            titulos.append(linea[0])           #se mete el titulo en una lista
            
        tupla=(anyo, titulos)                  #ponemos el año y los titulos en una lista de tuplas

    return tupla



###############################################################################################################################

###############################################################################################################################

def peliculas_mejores_valoradas(peliculas, ranking):
    '''
    recibe una lista y un parametro ranking (que va desde el 1 al 100) y devuelve otra lista con los 
    registros mejores valorados ordenados en un ranking marcado por el parametro
    
    ENTRADA
        -peliculas: lista de tuplas (titulo, genero, valoraciones Rotten Tomatoes, valoraciones audiencia, ganancias, anyo, fecha) -> 
            -> ([str, str, int, int, int, int, datetime])
        -ranking: parametro del 1 al 100 que marca el ranking de las peliculas -> int
        
    SALIDA 
        -mejores_peliculas: lista de tuplas (titulos) -> str
    '''
    lista=[]
    mejores_peliculas=[]
  
    for linea in peliculas:
        lista={linea[3]: linea[0]}                                  #creamos un diccionario con la clave de ganancias y el titulo   
        sorted(lista, key=operator.itemgetter(0), reverse=True)     #ordenamos el diccionario segun las ganancias de mayor a menor 
        
        i=0                                                         #creamos un bucle cuyo valor de i inicial es 0
        while i<=ranking in lista:                                  #mientras i valga menos o igual que el ranking
            mejores_peliculas.append(lista[1])                      #se añade el titulo a la lista 
            i=i+1                                                   #le sumamos 1 a la i, empieza de nuevo el bucle
            
    return mejores_peliculas
        
        
     

###############################################################################################################################

###############################################################################################################################

def diccionario_de_genero(peliculas,genero):
    '''
    calcula un diccionario {genero:[titulo, anyo, ganancias]}
    
    ENTRADA
        -peliculas: lista de tuplas (titulo, genero, valoraciones Rotten Tomatoes, valoraciones audiencia, ganancias, anyo, fecha) -> 
            -> ([str, str, int, int, int, int, datetime])
        -genero: del que se seleccionaran los registros -> str
    
    SALIDA
        -diccionario con la clave de genero y cuyos datos son el titulo de la pelicula, el anyo en el que salio  y el dinero 
         ganado con la pelicula {genero:[titulo, anyo, ganancias]} -> {str,[str, int, int]}
    '''
    
    tupla=[]
    lista=[]
    
    for linea in peliculas:                           
        if genero==linea[1]:                             #si coincide el genero seleccionado
            lista=(linea[0],linea[5],linea[3])           #metemos los datos en una lista
            tupla.append(lista)                          #metemos la lista en una tupla                   
            diccionario_de_genero={genero:[tupla]}       #metemos la tupla en un diccionario con la clave genero
    return diccionario_de_genero


###############################################################################################################################

###############################################################################################################################

def diccionario_de_anyo(peliculas, anyo):     
    '''
    calcula un diccionario {anyo:[titulo,valoracion audiencia, valoracion Rotten Tomatoes]} de las peliculas cuyas 
    claves cumplan determinada condicion  
     
    ENTRADA
        -peliculas: lista de tuplas (titulo, genero, valoraciones Rotten Tomatoes, valoraciones audiencia, ganancias, anyo, fecha) -> 
            -> ([str, str, int, int, int, int, datetime)
        -anyo: del que se seleccionaron los registros -> int
     
    SALIDA
        -diccionario de registros cuya  valoracion de la audiencia supere el 60% y el de Rotten Tomatoes el 40% y  coincida con el 
         anyo {anyo:[titulo,valoracion audiencia, valoracion Rotten Tomatoes]} -> {int:[int, int]}
    '''
    
    tupla=[]
    lista=[]
    
    for linea in peliculas:
        if linea[2]>40 and linea[3]>60 and linea[5]==anyo:      #si las condiciones se cumplen
            lista=(linea[0],linea[2],linea[3])                  #metemos los registros en una lista                      
            tupla.append(lista)                                 #metemos la lista en una tupla
            diccionario_de_anyo={anyo:tupla}                    #metemos la tupla en un diccionario cuya clave es el anyo
    return diccionario_de_anyo

