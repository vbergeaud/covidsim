# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:19:56 2020

@author: Famille
"""
import numpy as np
from state import State
from population_params import PopulationParams
class ClasseAgeState():
    def __init__(self):
        self._X=np.zeros(len(State))
        self._age=0
    
    def get_vector(self):
        return self._X
    
    def set_vector(self,vector):
        self._X=vector
        
    @staticmethod
    def makeClasseAgeState(infectious,age):
        ca=ClasseAgeState()
        param=PopulationParams()
        population=param.retrievePopulationByAgeClass()
        ca._X[State.SUSCEPTIBLE]=population[age.value]*(1-infectious)
        ca._X[State.EXPOSED]=population[age.value]*infectious
        ca._age=age
        return ca
    
    def get_infection_likelihood(self):
        from params import Params
        params=Params(self._age)
        total=0.0
        infected=0.0
        for state in State:
            total=total+self._X[state]
            if state in (State.PRODROMIC_INFECTIOUS, State.ASYMPTOMATIC_INFECTIOUS,State.PAUCYSYMPTOMATIC_INFECTIOUS):
                infected=infected+self._X[state]*params['r_beta']
            elif state in (State.MILD_INFECTIOUS, State.SEVERE_INFECTIOUS):
                infected=infected+self._X[state]
        return float(infected/total)*params['contagion_rate']

    def renormalize(self):
        population=[3e6,4e6,3e6]
        total=np.sum(self._X)
        self._X*=population[self._age]/total