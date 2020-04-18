# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:45:37 2020

@author: Famille
"""
import numpy as np
from age import Age
from state import State


data_hospital_from_march_1st=[0,2,1,0,5,10,7,11,11,8,13,25,67,80,71,82,100,90,50,110,100,150,180,200,210,210,210,190,150,200,280,230,190,190,180]
data_ICU_beds=[0,0,0,1,2,5,10,30,40,50,70,100,120,200,300,350,450,294,360,484,545,640,787,1000,1100,1300,1400,1600,1700,1800,2000,2200,2300,2375,2436,2506,2537,2601,2668,2654,2665,2617,2626,2604,2599,2494,2419,2341]
data_daily_dead=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,43,23,18,53,69,95,103,118,110,119,147,222,193,202,220,176,140,248,272,223,190,260,116,132,156,233,203,179,191]
class Result():
    def __init__(self):
        self._result=np.empty((1,len(Age),len(State)))
    
    def init(self,result):
        self._result = np.reshape(result, (len(Age),len(State)))

    def append(self,result):
        result = np.reshape(result, (len(Age),len(State)))
        self._result=np.append(self._result,result,axis=0)
    
    def draw_dates(self,dates):
        print (dates)
        import matplotlib.pyplot as plt      
        for date in dates:
            plt.axvline(x=date)
            
    def show_result(self,dates):
        offset=dates[0]-17
        res=np.reshape(self._result,(-1,len(Age),len(State)))
        import matplotlib.pyplot as plt      
        plt.title('State Evolution over time')
        res2=np.sum(res,axis=1)
        plt.subplot(3,2,1)
        plt.plot(res2[:,State.SUSCEPTIBLE],'k')
        plt.plot(res2[:,State.RECOVERED],'b')
        plt.legend(['Unaffected', 'Recovered'])
        self.draw_dates(dates)
        plt.subplot(3,2,3)
        plt.plot(res2[:,State.DEAD],'k')
        plt.plot(res2[:,State.ICU],'b')
        plt.plot(res2[:,State.HOSPITAL],'r')
        plt.plot(res2[:,State.MILD_INFECTIOUS],'g')
        plt.plot(res2[:,State.SEVERE_INFECTIOUS],'c')
        plt.legend(['Dead','ICU','Hospital','Mild symptoms','Severe Symptoms'])
        self.draw_dates(dates)

        plt.subplot(3,2,2)
        daily_dead=res2[1:-1,State.DEAD]-res2[0:-2,State.DEAD]
        plt.plot(daily_dead,'k')
        plt.plot(range(offset,offset+len(data_daily_dead)),data_daily_dead,'.')
        plt.legend(['Daily dead','Data - daily dead'])
        self.draw_dates(dates)

        plt.subplot (3,2,4)
        daily_ICU=res2[1:-1,State.ICU]-res2[0:-2,State.ICU]
        plt.plot(daily_ICU,'c')
        plt.plot(range(offset,offset+len(data_hospital_from_march_1st)),data_hospital_from_march_1st,'k.')
        plt.legend(['Netto daily admissions in ICU','Data - daily admissions in ICU'])
        self.draw_dates(dates)

        plt.subplot(3,2,5)
        plt.plot(res2[:,State.EXPOSED],'r')
        plt.plot(res2[:,State.PRODROMIC_INFECTIOUS],'g')
        plt.legend(['Exposed','Prodromic'])
        last_state=np.sum(res[-1,:,:],axis=0)
        self.draw_dates(dates)
       
        plt.subplot (3,2,6)
        plt.plot(res2[:,State.ICU],'c')
        plt.plot(range(offset,offset+len(data_ICU_beds)),data_ICU_beds,'k.')
        plt.legend(['Occupied ICU beds','Data - occupied ICU beds'])
    
        print ('Nb Dead = ',last_state[State.DEAD])
        print ('Nb Recovered =', last_state[State.RECOVERED])
        print ('Nb ICU =', last_state[State.ICU])
       