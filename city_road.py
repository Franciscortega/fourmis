import Ant
import tkinter as tk

class Road:
    "Une jolie route toute mimi"
    def __init__(self,v,v2,canvas,pher=0.1,length=-1):
        if length==-1: #Dans le cas où on ne donne pas de longueur, on la calcule à partir des coordonnées
            length=int(((v.x-v2.x)**2+(v.y-v2.y)**2)**0.5)/10
        self.length=length
        self.pheromon=pher
        self.city1=v
        self.city2=v2
        self.canvas = canvas
        
    def evaporate_pheromon(self):
        self.pheromon*=0.9995
        
    def plot_element(self):
        linewidth = (1+10*self.pheromon)/100
        x1 = self.city1.x
        y1 = self.city1.y
        x2 = self.city2.x
        y2 = self.city2.y
        self.canvas.create_line(x1,y1,x2,y2, width= linewidth)


class City:
    "Du hameau à la métropole en passant par la bourgade"
    def __init__(self,name,x,y,canvas):
        self.name=name
        self.L_road=[] #On initialise la liste des arêtes en vide
        self.L_adj_city=[] # De même pour la liste des villes adjacentes
        self.x=x
        self.y=y
        self.canvas = canvas

    def my_roads(self,L):
        selected_roads=[] # On met à jour la liste des arêtes
        L_adj_city=[]
        for i in range(len(L)): #Dans cette boucle, à partir de la liste des arêtes, on trouve la liste des villes adjacentes
            road=L[i]
            city1,city2=road.city1,road.city2
            if city1==self:
                selected_roads.append(road)
                L_adj_city.append(city2)    
            elif city2==self:
                selected_roads.append(road)
                L_adj_city.append(city1)
        self.L_adj_city=L_adj_city
        self.L_road = selected_roads
        
    def plot_element(self):
        x1 = self.x - 10
        x2 = self.y -10
        y1 = self.x + 10
        y2 = self.y +10
        self.canvas.create_oval(x1,x2,y1,y2, fill = 'blue')
        
