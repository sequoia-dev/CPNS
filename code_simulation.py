#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mini projet Python équation de transport
À utiliser préférentiellement sur spyder pour avoir des cellules
"""

#Importation des librairies

import numpy as np
import matplotlib.pyplot as plt

#Definition des fonctions

def ctilde(x):
    """
    Retourne la valeur de ctilde(x) comme donnée dans l'énoncé
    c(0,x) = ctilde(x)
    """
    
    c = np.maximum(0,np.exp(-(x-0.2)**2/0.005 - 1 ))
    return c


def first_transport(n,tmax,v,coeff,reverse=False):
    """
    Plot de l'animation de l'évolution de c(x,t).
    n est le nombre de pas de l'échantillonage de x.
    tmax est la borne supérieure du domaine de définition de t.
    v est la vitesse de propagation.
    coeff est le coefficient liant le pas de temps au pas d'espace
    dt = coeff * dx
    reverse permet d'avoir une figure qui 'fonctionne' quand v est négative
        (seconde implémentation)
    """
    #m est le nombre de pas de temps
    m = int(n*tmax/coeff)
    
    #definition des pas de temps et d'espace (repectivement \Delta x et \Delta t dans l'énoncé)
    dx = 1/n
    dt = tmax/m
    
    #création de l'échantillonage de x
    x = np.linspace(0,1,n)
    
    #initialisation des valeurs à t=0
    c = ctilde(x)
    t = 0
    #plot de la première valeur
    line , = plt.plot(x,c,label=r'$c(0,x)$')
    plt.legend('upper right')
    
    #definition des éléments du plot que ne vont pas changer au cours de l'animation
    plt.grid()
    plt.title('Évolution de c(t,x) pour différents temps')
    plt.xlabel('x')
    plt.ylabel('c(t,x)')
    
    #Boucle sur les pas de temps
    for k in range(m):

        #ligne issue de l'équation différencielle donnée dans l'énoncé
        #la fonction np.rolls permet d'écrire c^k_{i-1} tout en gérant les conditions au bords
        #reverse permet d'avoir une figure 'qui fonctionne' quand v est negative : c'est la seconde implémentation
        if reverse == False:
            c = c - v * (dt/dx) * (c - np.roll(c,+1))
        else : 
            c = c - v * (dt/dx) * - (c - np.roll(c,-1))

        #Nouveau temps après une boucle
        t += dt
        
        #Nouvelles valeurs des ordonnées après une boucle
        line.set_ydata(c)
        #label et legend qui évoluent avec le temps
        line.set_label(r'$c({:.2f},x)$'.format(t))
        plt.pause(dt)
        plt.legend(loc='upper right')
        
        
        plt.show()


#Programme principale

if __name__ == '__main__':
    
    plt.close('all')
    
    #%% Cellule pour spyder
    #1- Première implémentation, première figure :
    fig = plt.figure(1)
    n = 150
    tmax = 0.5
    v = 1
    coeff = 1 #dt = coeff * dx
    first_transport(n,tmax,v,coeff)
    
    #%%
    #1- Première implémentation, seconde figure avec un tmax suffisement long pour faire sortir la gaussienne du domaine de calcul
    fig = plt.figure(2)
    n = 150
    tmax = 1
    v = 1
    coeff = 1 #dt = coeff * dx
    first_transport(n,tmax,v,coeff)
    
    #On observe que la courbe 'revient' à l'origine, en boucle
    
    #%%
    #2- Test avec v = -1
    fig = plt.figure(3)
    n = 150
    tmax = 1
    v = -1
    coeff = 1 #dt = coeff * dx
    first_transport(n,tmax,v,coeff)
    
    # On observe que rapidement la fonction se met à augmenter,en se déplacant vers la gauche, on pense observer comme une propagation au cours du temps d'un désordre qui commence à droite et se propage à gauche
    
    
    #%%
    #3- Deuxième implémentation, avec toujours v = -1
    fig = plt.figure(4)
    n = 150
    tmax = 1
    v = -1
    coeff = 1 #dt = coeff * dx
    #On change juste la valeur de reverse pour faire la seconde implémentation
    first_transport(n,tmax,v,coeff,reverse=True)
    #On observe que la fonction gaussienne semble se déplacer vers la droite cette fois-ci
    
    #%%
    #4- Avec maintenant v = 1
    fig = plt.figure(5)
    n = 150
    tmax = 1
    v = 1
    coeff = 1 #dt = coeff * dx
    #On change juste la valeur de reverse pour faire la seconde implémentation
    first_transport(n,tmax,v,coeff,reverse=True)
    #On observe que la même chose qu'à la question 2, cette fois-ci seulement la fonction se déplace vers la droite
    
    #5-Voir document fourni...
    
    #%%
    #6- On modifie maintenant le coeff
    fig = plt.figure(6)
    n = 150
    tmax = 1
    v = 1
    coeff = 0.5 #dt = coeff * dx
    first_transport(n,tmax,v,coeff)
    #On observe que la gaussinne s'applatie ! C'est comme si le milieu dans lequel la gausienne se propageait était plus 'visqueux', on a simuler un amortissement !
    
    
    #%%
    #6- On modifie maintenant le coeff
    fig = plt.figure(7)
    n = 150
    tmax = 1
    v = 1
    coeff = 1.5 #dt = coeff * dx
    first_transport(n,tmax,v,coeff)
    #On observe le même comportement que dans les questions 2 et 4, cette fois ci la courbe se déplace de la gauche vers la droite et le désordre provient de la partie gauche
    #On a en fait simuler ici un comportement dans un milieu qui amplifierai la quantité c !
