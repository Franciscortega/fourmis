#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:49:06 2018

@author: Francisco
"""

import numpy.random as rnd
import numpy as np

import os
#os.chdir('/Users/Francisco/Documents/GitHub/fourmis')

#from city_road import City
import city_road as cr

class Ant:
    'Class for ant individual elements.'
    
    def __init__(self, alpha, beta, gamma, city, home, goal):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.position = city
        self.destination = city
        self.distance = 0
        self.path = [home]
        self.compteur=0
        self.returning = False
        self.carry_food = False
        self.home = home
        self.goal = goal
        self.nb_same_road = 0
        self.L_road_seen=[]
        self.path_length = 0
       
    def selectRoad(self):
        '''Fonction qui choisi la route à prendre à partir d'une ville. Doit 
        nécessairement être lancée quand la position est sur une ville '''
        choices = self.position.L_road[:]
        if len(self.path) > 2 :
            choices.remove(self.path[-2])
        if len(choices)>1 :
            selected = 0
            max_value = 0
            q = rnd.rand()
            if q<0.3:
                for index,road in enumerate(choices):
                    value = road.pheromon*(1/road.length)**(self.beta)
                    if value > max_value:
                        selected = index
                        max_value = value
            else :
                for index,road in enumerate(choices):
                    value = (road.pheromon**(self.alpha))*((1/road.length)**(self.beta))
                    if value > max_value:
                        selected = index
                        max_value = value
                    
        else:
            selected = 0
        
        selected_road = choices[selected]
        cities = [selected_road.city1, selected_road.city2]
        cities.remove(self.path[-1])
        self.position = selected_road
        self.distance = 1
        self.destination = cities[0]
        self.drop_pheromone(self.position)
        self.path.append(self.position)
        self.path_length += self.position.length

    def step_back(self):
        road = self.path.pop()
        self.distance = road.length
        self.drop_pheromone(road)
        self.position = road
        self.destination = self.path.pop()
        
       
    def take_food(self):
        '''Active le booléen de possession de nourriture et entame le retour'''
        self.carry_food = True
        self.returning = True
      
    def drop_food(self):
        '''Désactive le booléen de possession de nourriture et réinitialise son comportement'''
        self.carry_food = False
        for a_road in self.path:
            if a_road in self.L_road_seen :
                self.nb_same_road+=1
            else:
                self.L_road_seen.append(a_road)
        self.path = [self.home]
        self.returning = False
        self.path_length = 0
       
    def drop_pheromone(self, road):
        '''Dépose de la phéromone sur la voie choisie'''
        existant_level = road.pheromon
        inner_term = self.beta * existant_level + self.gamma
        value = (0.01+self.returning*50/(self.path_length+0.1))*abs(self.alpha * np.sin(inner_term))/100
        road.pheromon += value
        
    def draw_ant(self,canvas):
        if type(self.position) == cr.Road:
            x_vector = self.position.city2.x - self.position.city1.x
            y_vector = self.position.city2.y - self.position.city1.y
            ant_x = self.position.city1.x + self.distance*x_vector/(self.position.length)
            ant_y = self.position.city1.y + self.distance*y_vector/(self.position.length)
            x1 = ant_x - 5
            x2 = ant_y -5
            y1 = ant_x + 5
            y2 = ant_y + 5
            if self.carry_food:
                color = 'red'
            else:
                color = 'green'
            canvas.create_oval(x1,x2,y1,y2, fill = color)
        else :
            if self.carry_food:
                color = 'red'
            else:
                color = 'green'
            ant_x = self.position.x
            ant_y = self.position.y
            x1 = ant_x - 5
            x2 = ant_y -5
            y1 = ant_x + 5
            y2 = ant_y + 5
            canvas.create_oval(x1,x2,y1,y2, fill = color)
            
    
    
    def run_step(self):
        '''Fait avancer la fourmis d'un pas dans le cycle de la vie'''
        if self.returning:
        #Si la fourmi est en train de revenir sur ses pas, elle reprend simplement les étapes précédentes.
            if type(self.position) == cr.City :
                self.step_back()
            
            elif type(self.position) == cr.Road:
                self.distance -= 1
                if self.distance <= 0:
                    self.position = self.destination
                    self.distance = 0
                    if self.position == self.home:
                        self.drop_food()
                        
        else:
        #Si la fourmi avance, elle doit tout le temps choisir son chemin.
            if type(self.position) == cr.City :
                self.selectRoad()
        
            elif type(self.position) == cr.Road:
            #Si on est sur une route, on gère simplement l'avancement en distance
                self.distance += 1
                if self.distance >= self.position.length:
                    self.position = self.destination
                    #Détection de l'arrivée
                    if self.destination == self.goal:
                        self.take_food()
                    else:
                        self.path.append(self.position)
                        self.distance = 0
                    
                        
                    
            
                
