# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:18:37 2017

@author: derinaksit
"""
# A module to define impatience conditions
import numpy as np
from HARKutilities import approxUniform

def ImpatienceCondition (CRRA, DiscFac, N, nabla, Rsave_list, PermShkStd, PermGroFac, Unemp, PermShkCount, PermShkDstn):
    DiscFac_list = approxUniform(N,DiscFac-nabla,DiscFac+nabla)[1]
    Beta_count = len(DiscFac_list)
    Rsave_count = len(Rsave_list)
    GIC=np.zeros(shape=(len(DiscFac_list),len(Rsave_list)))
    RIC=np.zeros(shape=(len(DiscFac_list),len(Rsave_list)))
    AIC=np.zeros(shape=(len(DiscFac_list),len(Rsave_list)))
    WRIC=np.zeros(shape=(len(DiscFac_list),len(Rsave_list)))
    FHWC=np.zeros(shape=(len(DiscFac_list),len(Rsave_list)))
    exp_psi_inv=0
    
    for i in range(len(PermShkDstn[1])):
        exp_psi_inv=exp_psi_inv+(1.0/PermShkCount)*(PermShkDstn[1][i])**(-1)
    j = 0
    b = 0
    while j < Beta_count:
        b=0
        while b < Rsave_count:
            GIC[j,b]=(0.99375*exp_psi_inv*(Rsave_list[b]*DiscFac_list[j])**(1/CRRA))/(PermGroFac)
            RIC[j,b]=((Rsave_list[b]*DiscFac_list[j])**(1/CRRA))/(Rsave_list[b])
            WRIC[j,b]=((Unemp**(1/CRRA))*(Rsave_list[b]*DiscFac_list[j])**(1/CRRA))/(Rsave_list[b])
            AIC[j,b]=(Rsave_list[b]*DiscFac_list[j])**(1/CRRA)
            FHWC[j,b]=PermGroFac/Rsave_list[b]
            b += 1
        j += 1     
    
    print(GIC)
    print(RIC)
    print(WRIC)
    print(AIC)
    print(FHWC)
    #################################################################################
    count=0
    for i in range(len(DiscFac_list)):
            for j in range(len(Rsave_list)):              
                if GIC[i][j] > 1:
                    count+=1
    if count>0:
        print str(count) + ' Type(s) fail to satisfy growth impatience condition'
    #################################################################################
    count=0
    for i in range(len(DiscFac_list)):
            for j in range(len(Rsave_list)):              
                if RIC[i][j] > 1:
                    count+=1
    if count>0:
        print str(count) + ' Type(s) fail to satisfy return impatience condition'
    #################################################################################
    count=0
    for i in range(len(DiscFac_list)):
            for j in range(len(Rsave_list)):              
                if WRIC[i][j] > 1:
                    count+=1
    if count>0:
        print str(count) + ' Type(s) fail to satisfy weak return impatience condition'
    #################################################################################
    count=0
    for i in range(len(DiscFac_list)):
            for j in range(len(Rsave_list)):              
                if AIC[i][j] > 1:
                    count+=1
    if count>0:
        print str(count) + ' Type(s) fail to satisfy absolute impatience condition'
    #################################################################################
    count=0
    for i in range(len(DiscFac_list)):
            for j in range(len(Rsave_list)):              
                if FHWC[i][j] > 1:
                    count+=1
    if count>0:
        print str(count) + ' Type(s) fail to satisfy finite human wealth condition'