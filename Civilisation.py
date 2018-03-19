import city_road.py
import Ant.py

class Civilisation:
    def __init__(self,city_source,city_nest, Lcities,Lroads,Lants,canvas):
        self.source=city_source
        self.nest=city_nest
        self.L_cities = Lcities
        self.L_roads=Lroads
        self.L_ants=Lants
        self.quantite_nourriture=0
        self.canvas = canvas
        
    def un_tour(self):
        "Toutes les fourmis avancent d'un pas et le dépôt de phéromone est fait si nécessaire"
        for i in range(len(self.L_ants)):
            ant= self.L_ants[i]
            carry_food_anterieur=ant.carry_food
            ant.run_step()
            if carry_food_anterieur and not(ant.carry_food):
                ant.compteur+=1
                self.city_nest.quantite_nourriture+=1
        self.update_canvas
                
    #Ici on définit la méthode affichage
    def update_canvas(self):
        self.canvas.delete("all")
        for city in self.L_cities:
            city.plot_element
        for road in self.L_roads:
            road.plot_element
            
#En dessous : gestion de la génétique
        
