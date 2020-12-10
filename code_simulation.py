#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mini projet Python équation de transport
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


#Programme principale

if __name__ == '__main__':
    
    plt.close('all')
    n = 150
    tmax = 1
    v = 1
    coeff = 1 #dt = coeff * dx
    m = int(n*tmax/coeff)
    
    dx = 1/n
    dt = tmax/m
    
    x = np.linspace(0,1,n)
    c = ctilde(x)
    t = 0
    
    line , = plt.plot(x,c,label=r'$c(0,x)$')
    plt.legend('upper right')
    
    plt.grid()
    plt.title('Évolution de c(t,x) pour différents temps')
    plt.xlabel('x')
    plt.ylabel('c(t,x)')
    
    for k in range(m):

        c = c - v * (dt/dx) * (c - np.roll(c,+1))
        t += dt
        line.set_ydata(c)
        line.set_label(r'$c({:.2f},x)$'.format(t))
        plt.pause(dt)
        plt.legend(loc='upper right')
        
        
        plt.show()
            
