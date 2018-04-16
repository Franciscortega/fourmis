from city_road import *
from Ant import *
import numpy as np

class Civilisation:
    
    def __init__(self,city_source,city_nest, Lcities,Lroads,Lants,canvas):
        self.source=city_source
        self.nest=city_nest
        self.L_cities = Lcities
        self.L_roads=Lroads
        self.L_ants=Lants
        self.quantite_nourriture=0
        self.canvas = canvas
        self.proba_post_crossover=0.05
        self.amplitude_mutation=1
        
    def un_tour(self):
        "Toutes les fourmis avancent d'un pas et le dépôt de phéromone est fait si nécessaire"
        for i in range(len(self.L_ants)):
            ant= self.L_ants[i]
            carry_food_anterieur=ant.carry_food
            ant.run_step()
            if carry_food_anterieur and not(ant.carry_food):
                ant.compteur+=1
                self.quantite_nourriture+=1
        for road in self.L_roads:
            road.evaporate_pheromon()
        self.update_canvas()
                
    #Ici on définit la méthode affichage
    def update_canvas(self):
        self.canvas.delete("all")
        for city in self.L_cities:
            city.plot_element()
        for road in self.L_roads:
            road.plot_element()
        #for ant in self.L_ants :
           # ant.draw_ant(self.canvas)
            
        
            
#En dessous : gestion de la génétique

    def evolve(self):
        L_ant_last=self.L_ants


        #Trouver les deux meilleurs travailleurs
        i1_trav=0
        max1=-1
        max2=-1 #max1>max2
        i2_trav=0

        for i in range(len(L_ant_last)):
            ant=L_ant_last[i]
            val=ant.compteur
            if val>max1:
                max2=max1
                i2_trav=i1_trav
                max1=val
                i1_trav=i
            elif val>max2:
                i2_trav=i
                max2=val
        best_ant_trav=L_ant_last[i1_trav]
        best_ant_trav2=L_ant_last[i2_trav]

        #Trouver les deux meilleurs explorateurs
        i1_exp=0
        min1=100000
        min2=10000 #min1<min2
        i2_exp=0

        for i in range(len(L_ant_last)):
            ant=L_ant_last[i]
            val=ant.nb_same_road
            if val<min1:
                min2=min1
                i2_exp=i1_exp
                min1=val
                i1_exp=i
            elif val<min2:
                i2_exp=i
                min2=val
        best_ant_exp=L_ant_last[i1_exp]
        best_ant_exp2=L_ant_last[i2_exp]

        # Supprimer les champions de la liste des fourmis restantes (on les met de côté pour la recherche des pires)
        if best_ant_exp in L_ant_last:
            L_ant_last.remove(best_ant_exp)
        if best_ant_exp2 in L_ant_last:
            L_ant_last.remove(best_ant_exp2)
        if best_ant_trav in L_ant_last:
            L_ant_last.remove(best_ant_trav)
        if best_ant_trav in L_ant_last:
            L_ant_last.remove(best_ant_trav2)
                
        
                

               

        #Trouver les deux pires explorateurs restants et les supprimer
        i1_exp=0
        max1=-1
        max2=-1 #max1>max2
        i2_exp=0

        for i in range(len(L_ant_last)):
            ant=L_ant_last[i]
            val=ant.nb_same_road
            if val>max1:
                max2=max1
                i2_exp=i1_exp
                max1=val
                i1_exp=i
            elif val>max2:
                i2_exp=i
                max2=val
        worst_ant_exp=L_ant_last[i1_exp]
        worst_ant_exp2=L_ant_last[i2_exp]
        if worst_ant_exp in L_ant_last:
            L_ant_last.remove(worst_ant_exp)
        if worst_ant_exp2 in L_ant_last:
            L_ant_last.remove(worst_ant_exp2)                

        #Trouver les deux pires travailleurs restants
        i1_trav=0
        min1=100000
        min2=100000 #min1<min2
        i2_trav=0

        for i in range(len(L_ant_last)):
            ant=L_ant_last[i]
            val=ant.compteur
            if val<min1:
                min2=min1
                i2_trav=i1_trav
                min1=val
                i1_trav=i
            elif val<min2:
                i2_trav=i
                min2=val
        worst_ant_trav=L_ant_last.pop(i1_trav)
        worst_ant_trav2=L_ant_last.pop(i2_trav)

        if worst_ant_trav in L_ant_last:
            L_ant_last.remove(worst_ant_trav)
        if worst_ant_trav2 in L_ant_last:
            L_ant_last.remove(worst_ant_trav2)

        #Deux crossover d'explorateurs
        if np.random.random()>0.5:
            alpha=best_ant_exp.alpha
        else:
            alpha=best_ant_exp2.alpha

        if np.random.random()>0.5:
            beta=best_ant_exp.beta
        else:
            beta=best_ant_exp2.beta

        if np.random.random()>0.5:
            gamma=best_ant_exp.gamma
        else:
            gamma=best_ant_exp2.gamma

        cross_exp=Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        if np.random.random()>0.5:
            alpha=best_ant_exp.alpha
        else:
            alpha=best_ant_exp2.alpha

        if np.random.random()>0.5:
            beta=best_ant_exp.beta
        else:
            beta=best_ant_exp2.beta

        if np.random.random()>0.5:
            gamma=best_ant_exp.gamma
        else:
            gamma=best_ant_exp2.gamma

        cross_exp2=Ant(alpha,beta,gamma,self.source,self.source,self.nest)
        
        #Deux crossover de travailleurs
        if np.random.random()>0.5:
            alpha=best_ant_trav.alpha
        else:
            alpha=best_ant_trav2.alpha

        if np.random.random()>0.5:
            beta=best_ant_trav.beta
        else:
            beta=best_ant_trav2.beta

        if np.random.random()>0.5:
            gamma=best_ant_trav.gamma
        else:
            gamma=best_ant_trav.gamma

        cross_trav=Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        if np.random.random()>0.5:
            alpha=best_ant_trav.alpha
        else:
            alpha=best_ant_trav2.alpha

        if np.random.random()>0.5:
            beta=best_ant_trav.beta
        else:
            beta=best_ant_trav2.beta

        if np.random.random()>0.5:
            gamma=best_ant_trav.gamma
        else:
            gamma=best_ant_trav.gamma

        cross_trav2=Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        if np.random.random()>0.5:
            alpha=best_ant_trav.alpha
        else:
            alpha=best_ant_trav2.alpha

        if np.random.random()>0.5:
            beta=best_ant_trav.beta
        else:
            beta=best_ant_trav2.beta

        if np.random.random()>0.5:
            gamma=best_ant_trav.gamma
        else:
            gamma=best_ant_trav.gamma

        cross_trav3=Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        if np.random.random()>0.5:
            alpha=best_ant_trav.alpha
        else:
            alpha=best_ant_trav2.alpha

        if np.random.random()>0.5:
            beta=best_ant_trav.beta
        else:
            beta=best_ant_trav2.beta

        if np.random.random()>0.5:
            gamma=best_ant_trav.gamma
        else:
            gamma=best_ant_trav.gamma

        cross_trav4=Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        if np.random.random()>0.5:
            alpha=best_ant_trav.alpha
        else:
            alpha=best_ant_trav2.alpha

        if np.random.random()>0.5:
            beta=best_ant_trav.beta
        else:
            beta=best_ant_trav2.beta

        if np.random.random()>0.5:
            gamma=best_ant_trav.gamma
        else:
            gamma=best_ant_trav.gamma

        cross_trav5=Ant(alpha,beta,gamma,self.source,self.source,self.nest)


        if np.random.random()>0.5:
            alpha=best_ant_trav.alpha
        else:
            alpha=best_ant_trav2.alpha

        if np.random.random()>0.5:
            beta=best_ant_trav.beta
        else:
            beta=best_ant_trav2.beta

        if np.random.random()>0.5:
            gamma=best_ant_trav.gamma
        else:
            gamma=best_ant_trav.gamma

        cross_trav6=Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        if np.random.random()>0.5:
            alpha=best_ant_trav.alpha
        else:
            alpha=best_ant_trav2.alpha

        if np.random.random()>0.5:
            beta=best_ant_trav.beta
        else:
            beta=best_ant_trav2.beta

        if np.random.random()>0.5:
            gamma=best_ant_trav.gamma
        else:
            gamma=best_ant_trav.gamma

        cross_trav7=Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        if np.random.random()>0.5:
            alpha=best_ant_trav.alpha
        else:
            alpha=best_ant_trav2.alpha

        if np.random.random()>0.5:
            beta=best_ant_trav.beta
        else:
            beta=best_ant_trav2.beta

        if np.random.random()>0.5:
            gamma=best_ant_trav.gamma
        else:
            gamma=best_ant_trav.gamma

        cross_trav8=Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        if np.random.random()>0.5:
            alpha=best_ant_trav.alpha
        else:
            alpha=best_ant_trav2.alpha

        if np.random.random()>0.5:
            beta=best_ant_trav.beta
        else:
            beta=best_ant_trav2.beta

        if np.random.random()>0.5:
            gamma=best_ant_trav.gamma
        else:
            gamma=best_ant_trav.gamma

        cross_trav9=Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        if np.random.random()>0.5:
            alpha=best_ant_trav.alpha
        else:
            alpha=best_ant_trav2.alpha

        if np.random.random()>0.5:
            beta=best_ant_trav.beta
        else:
            beta=best_ant_trav2.beta

        if np.random.random()>0.5:
            gamma=best_ant_trav.gamma
        else:
            gamma=best_ant_trav.gamma

        cross_trav10=Ant(alpha,beta,gamma,self.source,self.source,self.nest)


        L_ant_last.pop(0)
        L_ant_last.pop(0)
        L_ant_last.pop(0)
        
        #Mutation de tous les autres
        for i in range(len(L_ant_last)):
            ant=L_ant_last[i]
            if np.random.random()<1/3:
                ant.alpha=ant.alpha+self.amplitude_mutation*(np.random.random()-0.5)
                ant.alpha=max(-5,ant.alpha)
                ant.alpha=min(5,ant.alpha)

            elif np.random.random()<2/3:
                ant.beta=ant.beta+self.amplitude_mutation*(np.random.random()-0.5)
                ant.beta=max(-5,ant.beta)
                ant.beta=min(5,ant.beta)
                
            else:
                ant.gamma=ant.gamma+self.amplitude_mutation*(np.random.random()-0.5)
                ant.gamma=max(-5,ant.gamma)
                ant.gamma=min(5,ant.gamma)
            L_ant_last[i]=ant

        #Mutation peu probable des crossover
        if np.random.random()<self.proba_post_crossover:
            ant=cross_exp
            if np.random.random()<1/3:
                ant.alpha=ant.alpha+self.amplitude_mutation*(np.random.random()-0.5)
                ant.alpha=max(-5,ant.alpha)
                ant.alpha=min(5,ant.alpha)

            elif np.random.random()<2/3:
                ant.beta=ant.beta+self.amplitude_mutation*(np.random.random()-0.5)
                ant.beta=max(-5,ant.beta)
                ant.beta=min(5,ant.beta)
                
            else:
                ant.gamma=ant.gamma+self.amplitude_mutation*(np.random.random()-0.5)
                ant.gamma=max(-5,ant.gamma)
                ant.gamma=min(5,ant.gamma)
            cross_exp=ant
            
        if np.random.random()<self.proba_post_crossover:
            ant=cross_exp2
            if np.random.random()<1/3:
                ant.alpha=ant.alpha+self.amplitude_mutation*(np.random.random()-0.5)
                ant.alpha=max(-5,ant.alpha)
                ant.alpha=min(5,ant.alpha)

            elif np.random.random()<2/3:
                ant.beta=ant.beta+self.amplitude_mutation*(np.random.random()-0.5)
                ant.beta=max(-5,ant.beta)
                ant.beta=min(5,ant.beta)
                
            else:
                ant.gamma=ant.gamma+self.amplitude_mutation*(np.random.random()-0.5)
                ant.gamma=max(-5,ant.gamma)
                ant.gamma=min(5,ant.gamma)
            cross_exp2=ant

        if np.random.random()<self.proba_post_crossover:
            ant=cross_trav
            if np.random.random()<1/3:
                ant.alpha=ant.alpha+self.amplitude_mutation*(np.random.random()-0.5)
                ant.alpha=max(-5,ant.alpha)
                ant.alpha=min(5,ant.alpha)

            elif np.random.random()<2/3:
                ant.beta=ant.beta+self.amplitude_mutation*(np.random.random()-0.5)
                ant.beta=max(-5,ant.beta)
                ant.beta=min(5,ant.beta)
                
            else:
                ant.gamma=ant.gamma+self.amplitude_mutation*(np.random.random()-0.5)
                ant.gamma=max(-5,ant.gamma)
                ant.gamma=min(5,ant.gamma)
            cross_trav=ant

        if np.random.random()<self.proba_post_crossover:
            ant=cross_trav2
            if np.random.random()<1/3:
                ant.alpha=ant.alpha+self.amplitude_mutation*(np.random.random()-0.5)
                ant.alpha=max(-5,ant.alpha)
                ant.alpha=min(5,ant.alpha)

            elif np.random.random()<2/3:
                ant.beta=ant.beta+self.amplitude_mutation*(np.random.random()-0.5)
                ant.beta=max(-5,ant.beta)
                ant.beta=min(5,ant.beta)
                
            else:
                ant.gamma=ant.gamma+self.amplitude_mutation*(np.random.random()-0.5)
                ant.gamma=max(-5,ant.gamma)
                ant.gamma=min(5,ant.gamma)
            cross_trav2=ant

        if np.random.random()<self.proba_post_crossover:
            ant=cross_trav3
            if np.random.random()<1/3:
                ant.alpha=ant.alpha+self.amplitude_mutation*(np.random.random()-0.5)
                ant.alpha=max(-5,ant.alpha)
                ant.alpha=min(5,ant.alpha)

            elif np.random.random()<2/3:
                ant.beta=ant.beta+self.amplitude_mutation*(np.random.random()-0.5)
                ant.beta=max(-5,ant.beta)
                ant.beta=min(5,ant.beta)
                
            else:
                ant.gamma=ant.gamma+self.amplitude_mutation*(np.random.random()-0.5)
                ant.gamma=max(-5,ant.gamma)
                ant.gamma=min(5,ant.gamma)
            cross_trav3=ant
            
        if np.random.random()<self.proba_post_crossover:
            ant=cross_trav4
            if np.random.random()<1/3:
                ant.alpha=ant.alpha+self.amplitude_mutation*(np.random.random()-0.5)
                ant.alpha=max(-5,ant.alpha)
                ant.alpha=min(5,ant.alpha)

            elif np.random.random()<2/3:
                ant.beta=ant.beta+self.amplitude_mutation*(np.random.random()-0.5)
                ant.beta=max(-5,ant.beta)
                ant.beta=min(5,ant.beta)
                
            else:
                ant.gamma=ant.gamma+self.amplitude_mutation*(np.random.random()-0.5)
                ant.gamma=max(-5,ant.gamma)
                ant.gamma=min(5,ant.gamma)
            cross_trav4=ant
   
        

        #Migration : création d'une nouvelle fourmi
        alpha=10*np.random.random()-5
        beta=10*np.random.random()-5
        gamma=10*np.random.random()-5

        new_ant = Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        alpha=10*np.random.random()-5
        beta=10*np.random.random()-5
        gamma=10*np.random.random()-5

        new_ant2 = Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        alpha=10*np.random.random()-5
        beta=10*np.random.random()-5
        gamma=10*np.random.random()-5

        new_ant3 = Ant(alpha,beta,gamma,self.source,self.source,self.nest)

        alpha=10*np.random.random()-5
        beta=10*np.random.random()-5
        gamma=10*np.random.random()-5

        new_ant4 = Ant(alpha,beta,gamma,self.source,self.source,self.nest)



        #On met tout (crossover, bests, nouvelle fourmi) dans la liste qu'on met à jour
        L_ant_last.append(new_ant)
        L_ant_last.append(new_ant2)
        L_ant_last.append(cross_trav3)
        L_ant_last.append(cross_trav4)
        #L_ant_last.append(cross_trav5)
        #L_ant_last.append(cross_trav6)
        #L_ant_last.append(cross_trav7)
        #L_ant_last.append(cross_trav8)
        #L_ant_last.append(cross_trav9)
        #L_ant_last.append(cross_trav10)
        L_ant_last.append(cross_trav)
        L_ant_last.append(cross_exp)
        #L_ant_last.append(cross_exp2)
        L_ant_last.append(cross_trav2)
        L_ant_last.append(best_ant_trav)
        L_ant_last.append(best_ant_trav2)
        L_ant_last.append(best_ant_exp)
        L_ant_last.append(best_ant_exp2)
        
        self.L_ants=L_ant_last



    def raz(self):
        
        for ant in self.L_ants:
            ant.position = self.source
            ant.destination = self.source
            ant.distance = 0
            ant.path = [self.source]
            ant.compteur=0
            ant.returning = False
            ant.carry_food = False
            ant.home = self.source
            ant.goal = self.nest
            ant.nb_same_road = 0
            ant.L_road_seen=[]
            
        for road in self.L_roads:
            road.pheromon=0.1
