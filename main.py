#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:34:40 2018

@author: Francisco
"""
print("Définition des fourmis")

import tkinter as tk
import city_road
from city_road import Road
from Civilisation import * 
from Ant import *

import os
#os.chdir('/Users/Francisco/Documents/GitHub/fourmis')
#print(os.getcwd() )
#int(input('?'))

print("Définition des fourmis")
####### MAIN SCRIPT - BE PSO ##############

#Parameters
print("Définition des paramètres")
canvas_width = 1000
canvas_heigh = 500
cities = 7
rho = 0.93


#Création du canvas
print("Définition du canvas")
master = tk.Tk()

view = tk.Canvas(master, width = canvas_width, height = canvas_heigh)
view.pack()

indice_parcours = 0
def startLife():
    global Civ
    global indice_parcours
    Civ.un_tour()
    indice_parcours+=1
    if indice_parcours%400==0:
        Civ.evolve()
        Civ.raz()
        print(int(indice_parcours/4000)," ",len(Civ.L_ants))
    view.after(50, startLife)

startButton = tk.Button(master, text='Start', command= startLife)
startButton.pack()

nb_ants=50

#Création population


#Creation des villes
print("Définition des villes")
L_cities=[]
source=city_road.City("Source",10,10,view)
L_cities.append(source)
city1=city_road.City("City1",400,100,view)
L_cities.append(city1)
city2=city_road.City("City2",250,200,view)
L_cities.append(city2)
city3=city_road.City("City3",500,100,view)
L_cities.append(city3)
city4=city_road.City("City4",350,400,view)
L_cities.append(city4)
city5=city_road.City("City5",40,476,view)
L_cities.append(city5)
city6=city_road.City("City6",267,123,view)
L_cities.append(city6)
city7=city_road.City("City7",300,91,view)
L_cities.append(city7)
city8=city_road.City("City8",311,427,view)
L_cities.append(city8)
city9=city_road.City("City9",300,212,view)
L_cities.append(city9)
city10=city_road.City("City10",552,500,view)
L_cities.append(city10)
city11=city_road.City("City11",352,319,view)
L_cities.append(city11)
city12=city_road.City("City12",673,500,view)
L_cities.append(city12)
city13=city_road.City("City13",179,472,view)
L_cities.append(city13)
city14=city_road.City("City14",106,500,view)
L_cities.append(city14)
city15=city_road.City("City15",222,248,view)
L_cities.append(city15)
city16=city_road.City("City16",411,88,view)
L_cities.append(city16)
city17=city_road.City("City17",662,328,view)
L_cities.append(city17)
city18=city_road.City("City18",694,375,view)
L_cities.append(city18)
city19=city_road.City("City19",391,435,view)
L_cities.append(city19)
city20=city_road.City("City20",64,13,view)
L_cities.append(city20)
city21=city_road.City("City21",296,221,view)
L_cities.append(city21)
city22=city_road.City("City22",120,300,view)
L_cities.append(city22)
anthill=city_road.City("Anthill",600,450,view)
L_cities.append(anthill)

#Création des routes et prise en compte dans les villes
print("Définition des routes")
L_roads=[]

road1=Road(source,city1,view)
road2=Road(source,city5,view)
road3=Road(source,city3,view)
road4=Road(city1,city2,view)
road5=Road(city2,city3,view)
road7=Road(city2,city5,view)
road8=Road(city3,city4,view)
road9=Road(city4,city5,view)
road10=Road(city4,anthill,view)
road11=Road(city2,anthill,view)
road12=Road(city5,anthill,view)
road12=Road(city4,city13,view)
road13=Road(city10,city17,view)
road14=Road(city10,city17,view)
road15=Road(city10,city11,view)
road16=Road(source,city8,view)
road17=Road(city7,city20,view)
road18=Road(city3,city20,view)
road19=Road(city3,city10,view)
road20=Road(city3,city13,view)
road21=Road(source,city4,view)
road22=Road(city8,city12,view)
road23=Road(city12,city15,view)
road24=Road(city8,city11,view)
road25=Road(city1,city3,view)
road26=Road(city15,city17,view)
road27=Road(city18,city19,view)
road28=Road(city4,city18,view)
road29=Road(city5,city22,view)
road30=Road(source,city10,view)
road31=Road(city9,city14,view)
road32=Road(city9,city16,view)
road33=Road(city12,city18,view)
road34=Road(city6,city13,view)
road35=Road(city10,city14,view)
road36=Road(city6,city7,view)
road37=Road(city4,city9,view)
road38=Road(city10,city15,view)
road39=Road(city12,city22,view)
road40=Road(city1,city20,view)
road41=Road(city14,anthill,view)
road42=Road(city16,anthill,view)
road43=Road(city13,anthill,view)
road44=Road(city10,anthill,view)
road45=Road(city17,anthill,view)


L_roads.append(road1)
L_roads.append(road2)
L_roads.append(road3)
L_roads.append(road4)
L_roads.append(road5)
L_roads.append(road7)
L_roads.append(road8)
L_roads.append(road9)
L_roads.append(road10)
L_roads.append(road11)
L_roads.append(road12)
L_roads.append(road13)
L_roads.append(road14)
L_roads.append(road15)
L_roads.append(road16)
L_roads.append(road17)
L_roads.append(road18)
L_roads.append(road19)
L_roads.append(road20)
L_roads.append(road21)
L_roads.append(road23)
L_roads.append(road24)
L_roads.append(road25)
L_roads.append(road26)
L_roads.append(road27)
L_roads.append(road28)
L_roads.append(road29)
L_roads.append(road30)
L_roads.append(road31)
L_roads.append(road32)
L_roads.append(road33)
L_roads.append(road34)
L_roads.append(road35)
L_roads.append(road36)
L_roads.append(road37)
L_roads.append(road38)
L_roads.append(road39)
L_roads.append(road40)
L_roads.append(road41)
L_roads.append(road42)
L_roads.append(road43)
L_roads.append(road44)
L_roads.append(road45)



for i in range(len(L_cities)):
    city=L_cities[i]
    city.my_roads(L_roads)


#Création des fourmis (aléatoires parce qu'on est comme ça).
print("Définition des fourmis")
L_ants=[]
for i in range(nb_ants):
    alpha=10*np.random.random()-5
    beta=10*np.random.random()-5
    gamma=10*np.random.random()-5
    L_ants.append(Ant(alpha,beta,gamma,source,source,anthill))


#Civ creation
print("Définition de la civilisation")
Civ = Civilisation(source,anthill,L_cities,L_roads,L_ants, view)
Civ.update_canvas()
view.mainloop()


