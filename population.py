# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:29:55 2020

@author: Famille
"""

from age import Age
from classe_age import ClasseAge
import numpy as np
class Population():
    def __init__(self):
        self._ages=[]
        self._contagion_matrix=None
        
    @staticmethod
    def makePopulation(start_infection_rate):
        pop=Population()
        for age in Age:
            pop._ages.append(ClasseAge(age,start_infection_rate))
        return pop
        
    def set_contagion_matrix(self,matrix):
        self._contagion_matrix=matrix
        
    def advance(self):
        for age in Age:
            infection_likelihood=0.0
            for contact in Age:
                infection_likelihood=infection_likelihood+self._contagion_matrix[age][contact]*self._ages[contact].get_infection_likelihood()
            self._ages[age].set_infection_rate(infection_likelihood)
            self._ages[age].advance()
#        print (age.name,self.get_state())
    
    def get_state(self):
        vec=[]
        for thisage in Age:
            vec.append( self._ages[thisage.value].get_state())
        return np.concatenate(vec)
 