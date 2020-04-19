# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:52:56 2020

@author: Famille
"""

from scenario import Scenario
from contagion_matrix import Contagion
daylist=[]
daylist.append([50,Contagion.BASELINE])
daylist.append([50,Contagion.LOCKDOWN])
daylist.append([100,Contagion.SEMI_LOCKDOWN])
scenario=Scenario.makeScenario(daylist,9.7e-6)
scenario.play()
scenario.show_result()



