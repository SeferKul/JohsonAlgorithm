# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:35:15 2021

@author: sefer
"""
from numpy import Inf # ımporting Infinity Value from numpy library

m1= [18,23,28,26,26,28,23,17,30,24,15,17,28,29,19] 

m2= [14,13,12,11,9,13,11,8,7,5,10,14,10,12,7]

m3= [12,8,5,11,11,3,9,4,13,6,2,12,14,11,6]


f=[]
s=[]
set1=[]
set2=[]

#JOHNSON METHOD
if min(m1)>= max(m2) or min(m3)>=max(m2):    #check if johnson applicable
    f= [sum(i) for i in zip(m1,m2)]          #create the sum of m1 and m2 machine to apply the algorithm
    print("first virtual machine: ",f)
    s= [sum (i) for i in zip (m3,m2)]        #create the sum of m3 and m2 machine to apply the algorithm
    print("second virtual machine: ",s)
    
    for i in range(len(f)):
        print(min(f),"compare to",min(s))
        if min(f)<min(s): 
            fIndex=f.index(min(f))    # find index number of min number in f list
            set1.append(fIndex)       # creating set1 list    
            
            s[fIndex]=Inf    #equate assigned values to Infinite
            f[fIndex]=Inf    #equate assigned values to Infinite
            print(f)
            print(s)
            print(set1 , "set1","\n")
            
            
        else:
            sIndex=s.index(min(s))   # find index number of min number in s list
            set2.append(sIndex)      # creating set1 list       
            
            f[sIndex]= Inf           #equate assigned values to Infinite
            s[sIndex]= Inf           #equate assigned values to Infinite
            print(f)
            print(s)
            print(set2 , "set2", "\n")
            
    set2.reverse()    #"append" function adds the values ​​to the end of the list, so set2 needs to be reversed
    
    if set1 and set2 :
        order= set1+set2        
    elif set1 and not set2:    
        order = set1
    elif set2 and not set1:   
        order = set2
    jorder= [(i+1) for i in order]
    print("job order:", jorder)
else:
    print("Johnson Algorithm is not applicable")
    
def makespan(joborder,mac1,mac2,mac3): # for calculating makespan 
    m1t=0
    m2t=0
    m3t=0
    for t in joborder:
        m1t= m1t+mac1[t-1]
        if m1t>m2t:
            m2t= m1t+mac2[t-1]
        else:
            m2t=m2t+mac2[t-1]
        if m2t>m3t:   
           m3t= m2t+mac3[t-1]
        else:
           m3t= m3t+mac3[t-1] 
    return("Makespan of M1: ",m1t,"\n","Makespan of M2: ",m2t,"\n","Makespan of M3: ",m3t,"\n","Total Makespan: ", m3t)    

print(makespan(jorder,m1,m2,m3))

    
