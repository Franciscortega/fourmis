import city_road.py
import Ant.py

class Civilisation:
    def __init__(self,city_source,city_nest, Lcities,Lroads,Lants):
        self.source=city_source
        self.nest=city_nest
        self.L_cities = Lcities
        self.L_roads=Lroads
        self.L_ants=Lants
        self.quantite_nourriture=0
    def un_tour(self):
        "Toutes les fourmis avancent d'un pas et le dépôt de phéromone est fait si nécessaire"
        for i in range(len(L_ants)):
            ant=L_ants[i]
            carry_food_anterieur=ant.carry_food
            ant.run_step()
            if carry_food_anterieur and not(ant.carry_food):
                ant.compteur+=1
                city_nest.quantite_nourriture+=1
        #Ici on appelle la méthode affichage
                
    #Ici on définit la méthode affichage


#En dessous : gestion de la génétique


