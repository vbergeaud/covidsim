# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:28:15 2020

@author: Famille
"""
from enum import IntEnum

class State(IntEnum):
    SUSCEPTIBLE=0
    EXPOSED=1
    PRODROMIC_INFECTIOUS=2
    ASYMPTOMATIC_INFECTIOUS=3
    PAUCYSYMPTOMATIC_INFECTIOUS=4
    MILD_INFECTIOUS=5
    SEVERE_INFECTIOUS=6
    ICU=7
    HOSPITAL=8
    RECOVERED=9
    DEAD=10
    
    def is_infectious(self):
        if self.name != State.SUSCEPTIBLE or \
            self.name != State.EXPOSED or\
            self.name != State.RECOVERED :
            return False
        else:
            return True