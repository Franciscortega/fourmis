#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:34:40 2018

@author: Francisco
"""

import tkinter as tk
import city_road.py
import Civilisation.py
import Ant.py


####### MAIN SCRIPT - BE PSO ##############

#Parameters

canvas_width = 1000
canvas_heigh = 800
cities = 7


#Création du canvas

master = tk.Tk()

view = Canvas(master, width = canvas_width, height = canvas_heigh)

nb_ants=20

#Création population


#Creation des villes

L_cities=[]
source=City("Source",0,0,view)
L_cities.append(source)
city1=City("City1",20,100,view)
L_cities.append(city1)
city2=City("City1",250,300,view)
L_cities.append(city2)
city3=City("City1",400,100,view)
L_cities.append(city3)
city4=City("City1",350,300,view)
L_cities.append(city4)
city5=City("City1",40,700,view)
L_cities.append(city5)
anthill=City("Anthill",600,750,view)
L_cities.append(anthill)

#Création des routes et prise en compte dans les villes
L_roads=[]
road1=Road(source,city1,view)
road2=Road(source,city5,view)
road3=Road(source,city3,view)
road4=Road(city1,city2,view)
road5=Road(city2,city3,view)
road6=Road(city1,city2,view)
road7=Road(city2,city5,view)
road8=Road(city3,city4,view)
road9=Road(city4,city5,view)
road10=Road(city4,anthill,view)
road11=Road(city2,anthill,view)
road12=Road(city5,anthill,view)

L_roads.append(road1)
L_roads.append(road2)
L_roads.append(road3)
L_roads.append(road4)
L_roads.append(road5)
L_roads.append(road6)
L_roads.append(road7)
L_roads.append(road8)
L_roads.append(road9)
L_roads.append(road10)
L_roads.append(road11)
L_roads.append(road12)

for i in range(len(L_cities)):
    city=L_cities[i]
    city.my_roads()


#Création des fourmis (aléatoires parce qu'on est comme ça). On va en mettre 

L_ants=[]
for i in range(nb_ants):
    alpha=10*np.random.random()-5
    beta=10*np.random.random()-5
    gamma=10*np.random.random()-5
    L_ants.append(Ant(alpha,beta,gamma,source,source,anthill))


#Civ creation
Civ=Civilisation(source,anthill,L_cities,L_roads,L_ants, #je sais pas quoi mettre dans "canvas")

#Life running
