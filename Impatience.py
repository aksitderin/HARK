# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:18:37 2017

@author: derinaksit
"""
# A module to check impatience conditions
import numpy as np
from HARKutilities import approxUniform

def ImpatienceCondition (CRRA, DiscFac, N, nabla, Rfree, PermShkStd, PermGroFac, Unemp, PermShkCount, PermShkDstn):
    
    DiscFac_list = approxUniform(N,DiscFac-nabla,DiscFac+nabla)[1]  # Construct the beta distribution
    Beta_count = len(DiscFac_list)                                  # Number of preference types
    GIC=np.zeros(shape=(len(DiscFac_list),1))                       # Some initial conditions
    RIC=np.zeros(shape=(len(DiscFac_list),1))
    AIC=np.zeros(shape=(len(DiscFac_list),1))
    WRIC=np.zeros(shape=(len(DiscFac_list),1))
    FHWC=np.zeros(shape=(len(DiscFac_list),1))
    exp_psi_inv=0
    
    for i in range(len(PermShkDstn[1])):
        exp_psi_inv=exp_psi_inv+(1.0/PermShkCount)*(PermShkDstn[1][i])**(-1)    #Get expected psi inverse
    print(exp_psi_inv)
    j = 0
    while j < Beta_count:                                                       #Calculate the LHS of each condition  
        GIC[j]=(0.99375*exp_psi_inv*(Rfree*DiscFac_list[j])**(1/CRRA))/(PermGroFac)
        RIC[j]=((Rfree*DiscFac_list[j])**(1/CRRA))/Rfree
        WRIC[j]=((Unemp**(1/CRRA))*(Rfree*DiscFac_list[j])**(1/CRRA))/Rfree
        AIC[j]=(Rfree*DiscFac_list[j])**(1/CRRA)
        FHWC[j]=PermGroFac/Rfree
        j += 1     

    print(GIC)
    print(RIC)
    print(WRIC)
    print(AIC)
    print(FHWC)

    #Check whether the inequality implied by the impatience condition holds
    #################################################################################
    count_GIC=0
    for i in range(len(DiscFac_list)):
        if GIC[i] < 1:                                      
            count_GIC+=1
    if count_GIC!=len(DiscFac_list):
        fail_GIC=len(DiscFac_list)-count_GIC
        print str(fail_GIC) + ' Type(s) fail to satisfy growth impatience condition'
    #################################################################################
    count_RIC=0
    for i in range(len(DiscFac_list)):
        if RIC[i] < 1:
            count_RIC+=1
    if count_RIC!=len(DiscFac_list):
        fail_RIC=len(DiscFac_list)-count_RIC
        print str(fail_RIC) + ' Type(s) fail to satisfy return impatience condition'
    #################################################################################
    count_WRIC=0
    for i in range(len(DiscFac_list)):
        if WRIC[i] < 1:
            count_WRIC+=1
    if count_WRIC!=len(DiscFac_list):
        fail_WRIC=len(DiscFac_list)-count_WRIC
        print str(fail_WRIC) + ' Type(s) fail to satisfy weak return impatience condition'
    #################################################################################
    count_AIC=0
    for i in range(len(DiscFac_list)):
        if AIC[i] < 1:
            count_AIC+=1
    if count_AIC!=len(DiscFac_list):
        fail_AIC=len(DiscFac_list)-count_AIC
        print str(fail_AIC) + ' Type(s) fail to satisfy absolute impatience condition'
    #################################################################################
    count_FHWC=0
    for i in range(len(DiscFac_list)):
        if FHWC[i] < 1:
            count_FHWC+=1
    if count_FHWC!=len(DiscFac_list):
        fail_FHWC=len(DiscFac_list)-count_FHWC
        print str(fail_FHWC) + ' Type(s) fail to satisfy finite human wealth condition'
    #################################################################################
    count_all=count_GIC+count_RIC+count_WRIC+count_AIC+count_FHWC
    if count_all==0:
        print 'All types satisfy all conditions'