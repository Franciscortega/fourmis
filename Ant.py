#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:49:06 2018

@author: Francisco
"""

import numpy.random as rnd
import numpy as np

class Ant:
    'Class for ant individual elements.'
    
    def __init__(self, alpha, beta, gamma, city,home, goal):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.__position = city
        self.__destination = city
        self.__distance = 0
        self.__path = []
        self.__returning = False
        self.carry_food = False
        self.home = home
        self.goal = goal
       
    def selectRoad(self, phero_level):
        '''Fonction qui choisi la route à prendre à partir d'une ville. Doit 
        nécessairement être lancée quand la position est sur une ville '''
        choices = self.__position.L_road
        choices.pop(self.__path[-2])
        
        selected = 0
        max_value = 0
        q = rnd.rand()
        if q<0.4:
            for road,index in choices:
                value = road.pheromon*(1/road.length)^(self.__beta)
                if value > max_value:
                    selected = index
                    max_value = value
        else :
            for road,index in choices:
                value = road.pheromon^(self.__alpha)*(1/road.length)^(self.__beta)
                if value > max_value:
                    selected = index
                    max_value = value
                    
        self.__position = selected
        self.__distance = 1
        self.drop_pheromone(selected)
        
    def step_back(self):
        road = self.__path.pop()
        self.__distance = road.lenght
        self.__position = road
        self.__destination = self.__path.pop()
        
       
    def take_food(self):
        '''Active le booléen de possession de nourriture et entame le retour'''
        self.carry_food = True
        self.__returning = True
      
    def drop_food(self):
        '''Désactive le booléen de possession de nourriture et réinitialise son comportement'''
        self.carry_food = False
        self.__path = []
        self.__returning = False
       
    def drop_pheromone(self, road):
        '''Dépose de la phéromone sur la voie choisie'''
        existant_level = road.pheromon
        inner_term = self.__beta * existant_level + self.__gamma
        value = self.__alpha * np.sin(inner_term)
        road.pheromon += value
    
    
    def run_step(self):
        '''Fait avancer la fourmis d'un pas dans le cycle de la vie'''
        if self.__returning:
        #Si la fourmi est en train de revenir sur ses pas, elle reprend simplement les étapes précédentes.
            if type(self.position) == City :
                self.stepBack()
            
            elif type(self.position) == Road:
                self.__distance -= 1
                if self.__distance == 0:
                    self.__position = self.__destination
                    self.__distance = 0
                    if self.__position == self.__home:
                        self.drop_food
                        
        else:
        #Si la fourmi avance, elle doit tout le temps choisir son chemin.
            if type(self.position) == City :
                self.selectRoad()
        
            elif type(self.position) == Road:
            #Si on est sur une route, on gère simplement l'avancement en distance
                self.__distance += 1
                if self.__distance == self.__position.length:
                    self.__position = self.__destination
                    #Détection de l'arrivée
                    if self.__destination == self.__goal:
                        self.take_food
                    else:
                        self.__path.append(self.__position)
                        self.__distance = 0
                    
                        
                    
            
                