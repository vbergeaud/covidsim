# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:16:58 2020

@author: Famille
"""


from classe_age_state import ClasseAgeState
from evolution_matrix import EvolutionMatrix
import numpy as np 
    
class ClasseAge():
    def __init__(self,age,infection_rate):
        self._state=ClasseAgeState.makeClasseAgeState(infection_rate,age)
        self._M=EvolutionMatrix.makeEvolutionMatrix(age)
        self._age=age
        
    def set_infection_rate(self,rate):
        self._M.set_infection_rate(rate)
        
    def advance(self):
#        print (self._age.name)
#        print (self._M.get_matrix())
        self._state.set_vector(np.matmul(np.transpose(self._M.get_matrix()),self._state.get_vector()))
        self._state.renormalize()
    
    def get_infection_likelihood(self):
        return self._state.get_infection_likelihood()
    
    def get_state(self):
        return self._state.get_vector()