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


#Création du canvas
print("Définition du canvas")
master = tk.Tk()

view = tk.Canvas(master, width = canvas_width, height = canvas_heigh)
view.pack()

def startLife():
    global Civ
    Civ.un_tour()
    view.after(1, startLife)

startButton = tk.Button(master, text='Start', command= startLife)
startButton.pack()

nb_ants=1000

#Création population


#Creation des villes
print("Définition des villes")
L_cities=[]
source=city_road.City("Source",10,10,view)
L_cities.append(source)
city1=city_road.City("City1",400,100,view)
L_cities.append(city1)
city2=city_road.City("City1",250,200,view)
L_cities.append(city2)
city3=city_road.City("City1",500,100,view)
L_cities.append(city3)
city4=city_road.City("City1",350,400,view)
L_cities.append(city4)
city5=city_road.City("City1",40,476,view)
L_cities.append(city5)
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

for i in range(len(L_cities)):
    city=L_cities[i]
    city.my_roads(L_roads)


#Création des fourmis (aléatoires parce qu'on est comme ça). On va en mettre 
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


