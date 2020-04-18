# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:25:36 2020

@author: Famille
"""

from population import Population
from result import Result
from contagion_matrix import ContagionMatrix

class Scenario():
    def __init__(self):
        self._days=[]
        self._initial_contagion=0
        self._result=None
        self._dates_for_display=[]
        
    def play(self):
        pop=Population.makePopulation(self._initial_contagion)
        result=Result()
        result.init(pop.get_state())
        for contagion in self._days:
            contagion_matrix=ContagionMatrix.make_contagion(contagion)
            pop.set_contagion_matrix(contagion_matrix.get_matrix())
            pop.advance()
            result.append(pop.get_state())
        self._result=result

    def show_result(self):
        self._result.show_result(self._dates_for_display)
        
    @staticmethod
    def makeScenario(daylist, initial_contagion):
        #creating
        days=[]
        for items in daylist:
            no_days=items[0]
            no_contagion_matrix=items[1]
            for  i in range(no_days):
                days.append(no_contagion_matrix)
        
        #creating transition dates for display
        date=0
        dates=[]
        for items in daylist[:-1]:
            date+=items[0]
            dates.append(date)
            
        scenario=Scenario()
        scenario._days=days
        scenario._initial_contagion=initial_contagion
        scenario._dates_for_display=dates
        return scenario