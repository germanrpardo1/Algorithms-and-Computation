#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Germán R. Pardo González
# 202338054


# In[2]:


def primeAtLeast(n):
    
    
   
    found = False
    p = n
    
    if n <= 1: 
        found = True
        p = 2
        
    while not found:
        
        
        ### Check if the number is prime or not
        
        i = 2
        prime = True
        
        while prime and i < p:
            
            if p % i == 0:
                
                prime = False
                
            else:
                
                i += 1

        ### If it's not prime then continue searching with the next number p >= n, otherwise stop outer while
        
        if not prime:
            
            p += 1
            
        else:
            
            found = True

            
    return p


# In[3]:


n = 9302029
primeAtLeast(n)


# In[ ]:




