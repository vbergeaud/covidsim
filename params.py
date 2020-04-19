# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:36:22 2020

@author: Famille
"""

from age import Age

class Params():
    def __init__(self,age_group):
        self.params={}
        self.params['inv_theta']=5.2
        self.params['inv_mu_p']=1.5
        self.params['inv_epsilon']=self.params['inv_theta']-self.params['inv_mu_p']
        self.params['p_a']=0.2
        self.params['s']=7.5
        self.params['inv_mu']=self.params['s']-self.params['inv_theta']
        self.params['r_beta']=0.51
        self.params['contagion_rate']=3./(self.params['s']-self.params['inv_epsilon'])/10.5
       
        if age_group==Age.CHILD:
            self.params['p_ps']=1
            self.params['p_ms']=0
            self.params['p_ss']=0
            self.params['p_ICU']=0
            self.params['lambda_H_R']=0
            self.params['lambda_H_D']=0
            self.params['lambda_ICU_R']=0
            self.params['lambda_ICU_D']=0
        elif age_group==Age.ADULT:
            self.params['p_ps']=0.2
            self.params['p_ms']=0.7
            self.params['p_ss']=0.1
            self.params['p_ICU']=0.36
            self.params['lambda_H_R']=0.072
            self.params['lambda_H_D']=0.0042
            self.params['lambda_ICU_R']=0.05
            self.params['lambda_ICU_D']=0.0074
        elif age_group==Age.SENIOR:
            self.params['p_ps']=0.2
            self.params['p_ms']=0.6
            self.params['p_ss']=0.2
            self.params['p_ICU']=0.2
            self.params['lambda_H_R']=0.022
            self.params['lambda_H_D']=0.014
            self.params['lambda_ICU_R']=0.036 
            self.params['lambda_ICU_D']=0.029 
            
    def __getitem__(self,key):
        return self.params[key]
        