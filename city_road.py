import Ant.py

class Road:
    "Une jolie route toute mimi"
    def __init__(self,v,v2,pher=0,length=-1):
        if length==-1: #Dans le cas où on ne donne pas de longueur, on la calcule à partir des coordonnées
            length=int((v.x^2+v.y^2)**0.5)
        self.length=length
        self.pheromon=pher
        self.city1=v
        self.city2=v2
        
    def evaporate_pheromon(self):
        self.pheromon*=rho



class City:
    "Du hameau à la métropole en passant par la bourgade"
    def __init__(self,name,x,y):
        self.name=name
        self.L_road=[] #On initialise la liste des arêtes en vide
        self.L_adj_city=[] # De même pour la liste des villes adjacentes
        self.x=x
        self.y=y

    def my_roads(self,L):
        self.L_road=L # On met à jour la liste des arêtes
        L_adj_city=[]
        for i in range(len(L)): #Dans cette boucle, à partir de la liste des arêtes, on trouve la liste des villes adjacentes
            road=self.L_road[i]
            city1,city2=road.city1,road.city2
            if city1==self:
                L_adj_city.append(city2)
            elif city2==self:
                L_adj_city.append(city1)
        self.L_adj_city=L_adj_city
