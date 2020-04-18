# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:35:49 2020

@author: Famille
"""
from age import Age
from enum import IntEnum
import numpy as np

class Contagion(IntEnum):
    BASELINE=0
    LOCKDOWN=1
    SEMI_LOCKDOWN=2
    SEMI_LOCKDOWN_OPEN_SCHOOLS=3
    
class ContagionMatrix():
    def __init__(self):
        self._matrix=np.zeros((len(Age),len(Age)))
    
    def get_matrix(self):
        return self._matrix
    
    
    @staticmethod
    def make_contagion(contagion):
        matrix=ContagionMatrix()
        if contagion==Contagion.BASELINE:
            matrix._matrix[Age.CHILD][Age.CHILD]=8
            matrix._matrix[Age.CHILD][Age.ADULT]=5
            matrix._matrix[Age.CHILD][Age.SENIOR]=1
            matrix._matrix[Age.ADULT][Age.CHILD]=3
            matrix._matrix[Age.ADULT][Age.ADULT]=6.5
            matrix._matrix[Age.ADULT][Age.SENIOR]=3
            matrix._matrix[Age.SENIOR][Age.CHILD]=1
            matrix._matrix[Age.SENIOR][Age.ADULT]=6
            matrix._matrix[Age.SENIOR][Age.SENIOR]=4
        elif contagion==Contagion.LOCKDOWN:
            matrix._matrix[Age.CHILD][Age.CHILD]=2
            matrix._matrix[Age.CHILD][Age.ADULT]=2
            matrix._matrix[Age.CHILD][Age.SENIOR]=0
            matrix._matrix[Age.ADULT][Age.CHILD]=1
            matrix._matrix[Age.ADULT][Age.ADULT]=1.5
            matrix._matrix[Age.ADULT][Age.SENIOR]=1
            matrix._matrix[Age.SENIOR][Age.CHILD]=0
            matrix._matrix[Age.SENIOR][Age.ADULT]=1
            matrix._matrix[Age.SENIOR][Age.SENIOR]=1
        elif contagion==Contagion.SEMI_LOCKDOWN:
            matrix._matrix[Age.CHILD][Age.CHILD]=2
            matrix._matrix[Age.CHILD][Age.ADULT]=2
            matrix._matrix[Age.CHILD][Age.SENIOR]=0.5
            matrix._matrix[Age.ADULT][Age.CHILD]=1.5
            matrix._matrix[Age.ADULT][Age.ADULT]=2
            matrix._matrix[Age.ADULT][Age.SENIOR]=1.5
            matrix._matrix[Age.SENIOR][Age.CHILD]=0.5
            matrix._matrix[Age.SENIOR][Age.ADULT]=1.25
            matrix._matrix[Age.SENIOR][Age.SENIOR]=1.25
        elif contagion==Contagion.SEMI_LOCKDOWN_OPEN_SCHOOLS:
            matrix._matrix[Age.CHILD][Age.CHILD]=8
            matrix._matrix[Age.CHILD][Age.ADULT]=4
            matrix._matrix[Age.CHILD][Age.SENIOR]=0.5
            matrix._matrix[Age.ADULT][Age.CHILD]=2
            matrix._matrix[Age.ADULT][Age.ADULT]=2
            matrix._matrix[Age.ADULT][Age.SENIOR]=1.5
            matrix._matrix[Age.SENIOR][Age.CHILD]=0.5
            matrix._matrix[Age.SENIOR][Age.ADULT]=1.25
            matrix._matrix[Age.SENIOR][Age.SENIOR]=1.25
  
        return matrix