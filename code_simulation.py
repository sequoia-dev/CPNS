#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mini projet Python équation de transport
"""

#Importation des librairies

import numpy as np

#Definition des fonctions

def ctilde(x):
    """
    Retourne la valeur de ctilde(x) comme donnée dans l'énoncé
    c(0,x) = ctilde(x)
    """
    
    c = np.max(0,np.exp(-(x-0.2)**2/0.005 - 1 ))
    
    return c

def c(v,dt,dx):
    




#Programme principale

if __name__ == '__main__':
    pass
