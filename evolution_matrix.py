# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:26:28 2020

@author: Famille
"""
from state import State
from params import Params
import numpy as np

class EvolutionMatrix():
    def __init__(self):
        self._matrix=np.zeros((len(State),len(State)))
    
    def set_infection_rate(self,rate):
        print ("Rate",rate)
        self._matrix[State.SUSCEPTIBLE][State.EXPOSED]=rate
        self.set_diagonal()
    
    def set_diagonal(self):
        for irow in range(len(State)):
            extra_diag=0
            for icol in range(len(State)):
                if icol!=irow :
                    extra_diag +=self._matrix[irow][icol]
            self._matrix[irow][irow]=1-extra_diag
    
    def get_matrix(self):
        return self._matrix
    @staticmethod
    def makeEvolutionMatrix(age):
        params=Params(age)
        matrix=EvolutionMatrix()
        matrix._matrix[State.EXPOSED][State.PRODROMIC_INFECTIOUS] = 1/params['inv_epsilon']
        matrix._matrix[State.PRODROMIC_INFECTIOUS][State.ASYMPTOMATIC_INFECTIOUS] = params['p_a']/params['inv_mu_p']
        matrix._matrix[State.PRODROMIC_INFECTIOUS][State.MILD_INFECTIOUS] = (1-params['p_a'])*params['p_ms']/params['inv_mu_p']
        matrix._matrix[State.PRODROMIC_INFECTIOUS][State.SEVERE_INFECTIOUS] = (1-params['p_a'])*params['p_ss']/params['inv_mu_p']
        matrix._matrix[State.PRODROMIC_INFECTIOUS][State.PAUCYSYMPTOMATIC_INFECTIOUS] = (1-params['p_a'])*params['p_ps']/params['inv_mu_p']
        matrix._matrix[State.ASYMPTOMATIC_INFECTIOUS][State.RECOVERED] = 1/params['inv_mu']
        matrix._matrix[State.MILD_INFECTIOUS][State.RECOVERED] = 1/params['inv_mu']
        matrix._matrix[State.PAUCYSYMPTOMATIC_INFECTIOUS][State.RECOVERED] = 1/params['inv_mu']
        matrix._matrix[State.SEVERE_INFECTIOUS][State.HOSPITAL] = 1/params['inv_mu']*(1-params['p_ICU'])
        matrix._matrix[State.SEVERE_INFECTIOUS][State.ICU] = 1/params['inv_mu']*(params['p_ICU'])
        matrix._matrix[State.HOSPITAL][State.DEAD] = params['lambda_H_D']
        matrix._matrix[State.HOSPITAL][State.RECOVERED] = params['lambda_H_R']
        matrix._matrix[State.ICU][State.DEAD] = params['lambda_ICU_D']
        matrix._matrix[State.ICU][State.RECOVERED] = params['lambda_ICU_R']
        matrix.set_diagonal()
        return matrix
        
    