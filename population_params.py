# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:21:24 2020

@author: Famille
"""
class PopulationParams():
    def __init__(self):
        self.params={}
        self.params['total_population']=1e7
        self.params['alpha_child']=0.25
        self.params['alpha_adult']=0.6
        self.params['alpha_senior']=0.15

    def retrievePopulationByAgeClass(self):
        tot=self.params['total_population']
        a_c=self.params['alpha_child']
        a_a=self.params['alpha_adult']
        a_s=self.params['alpha_senior']
        pop= [tot*a_c,tot*a_a,tot*a_s]
        return pop              
    
    def __getitem__(self,key):
        return self.params[key]
    