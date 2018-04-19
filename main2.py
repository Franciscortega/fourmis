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
cities = 10
rho = 0.95
nb_ants=100


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
    if indice_parcours%1000==0:
        Civ.evolve()
        Civ.raz()
        print(int(indice_parcours/1000)," ",len(Civ.L_ants))
    view.after(10, startLife)

startButton = tk.Button(master, text='Start', command= startLife)
startButton.pack()


#Création population


#Creation des villes
print("Définition des villes")
L_cities=[]
source=city_road.City("Source",10,10,view)
L_cities.append(source)

city1=city_road.City("City1",300,16,view)
L_cities.append(city1)

city2=city_road.City("City1",500,120,view)
L_cities.append(city2)

city3=city_road.City("City1",900,130,view)
L_cities.append(city3)

city4=city_road.City("City1",200,200,view)
L_cities.append(city4)

city5=city_road.City("City1",400,240,view)
L_cities.append(city5)

city6=city_road.City("City1",750,300,view)
L_cities.append(city6)

city7=city_road.City("City1",220,375,view)
L_cities.append(city7)

city8=city_road.City("City1",730,400,view)
L_cities.append(city8)

anthill=city_road.City("Anthill",800,400,view)
L_cities.append(anthill)

#Création des routes et prise en compte dans les villes
print("Définition des routes")
L_roads=[]
road1=Road(source,city1,view, rho)
road2=Road(source,city5,view, rho)
road3=Road(source,city4,view, rho)
road4=Road(city1,city4,view, rho)
road5=Road(city2,city1,view, rho)
road6=Road(city3,city1,view, rho)
road7=Road(city2,city3,view, rho)
road8=Road(city2,city5,view, rho)
road9=Road(city4,city5,view, rho)
road10=Road(city4,city7,view, rho)
road11=Road(city5,city7,view, rho)
road12=Road(city7,city8,view, rho)
road13=Road(city5,city8,view, rho)
road14=Road(city5,city6,view, rho)
road15=Road(city3,city6,view, rho)
road16=Road(anthill,city8,view, rho)
road17=Road(city6,anthill,view, rho)
road18=Road(city6,city8,view, rho)

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


