#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Germán Pardo González
# 202338054


# In[8]:


# Exercise 3.1:

# The worst case for the binary search algorithm is when the key is a maximum or a minimum in the list x.
# i.e., the key value is rather in the first position of x or in the last position of x.
# Therefore, the algorithm would need to divide the list into 2 until there is one element left in the list.
# Hence, the algorithm must do enough comparisons until the list is of lenght 1, that means 
# until the floor of length(x)/(2^n) becomes one.
# if we approximate, say N = length(x) (N and n are different) and we take out the floor function, therefore:
# 1 = N/(2^n)   which leads to 2^n = N so:
# log_2 (N) = n
# I can conlcude that the number of comparisons that binary search does in the worst case is  log_2 (N) = n 
# Where N is the length of the input list x.


# In[9]:


# Exercise 3.2:
def binsearch(key, x, i, j):
    
        
    
    # Checks if key (input value) is equal to the element in the half of the current list
    if key == x[i:j][len(x[i:j]) // 2]:



        ### To return the first key value in the list ###

        last = False
        # This will save the value of the index of key in x
        check_ind = (i+j) // 2

        while not last:
            # Decrease by one the index until it finds the first element equal to key
            if check_ind != 0:
                if x[check_ind - 1] == key:
                    check_ind -= 1
                else:
                    last = True
            else:
                last = True

        ### Ends  ###


        return check_ind
    
    
    
    ### This happens when key is not in x
    elif j == i + 1:
    
        if x[i:j][len(x[i:j]) // 2] < key:
            return i + 1
        elif x[i:j][len(x[i:j]) // 2] > key:
            return i
    ###
    
    
    ### Binary search ###
    # Checks if key value is in the lower half of current x
    elif key < x[i:j][len(x[i:j]) // 2]:

        # Calculates the new upper limit of the index of list x
        j = i + len(x[i:j]) // 2
        return binsearch(key, x, i, j)

    # Key value is in the upper half of current x
    else:       

        # Calculates the new lower limit of the index of list x
        i += len(x[i:j]) // 2
        return binsearch(key, x, i, j)


# In[10]:


# Exercise 3.3

def test():
    
    
    i = 0
    
    ### First test
    
    x = [7,7,10,23,42,42,42,51,60]
    j = len(x)
    key = 3 
    
    index = binsearch(key, x, i, j)
    found = False
    if x[index] == key:
        found = True
    
    print('Testing list:', x)
    if found:
        print('Key', key, 'found at index', index )
    else:
        print('Key', key, 'not found, should be at index', index)
        insert(key, x)
        print('Key', key, 'inserted at index' , index)
        print('New list:',x)
    
    
    
    ### Second test
    x = [i for i in range(1, 2 * 10**8) if not i % 2 == 0]
    j = len(x)
    key = 3
    index = binsearch(key, x, i, j)
    found = False
    if x[index] == key:
        found = True
        
    print('Testing big list')
    if found:
        print('Key', key, 'found at index', index )
    else:
        print('Key', key, 'not found, should be at index', index)
        insert(key, x)
        print('Key', key, 'inserted at index' , index)

    
    
    
    ### Third test
    x = [9 for i in range(10**8)]
    j = len(x)
    key = 3
    index = binsearch(key, x, i, j)
    
    found = False
    if x[index] == key:
        found = True
        
    print('Testing big list of 9s')
    if found:
        print('Key', key, 'found at index', index )
    else:
        print('Key', key, 'not found, should be at index', index)
        insert(key, x)
        print('Key', key, 'inserted at index' , index)    


# In[11]:


# Exercise 3.4
def insert(key, x):
    
    i = 0
    j = len(x)
    index = binsearch(key, x, i, j)
    
    
    x.append(key)
    for i in range(len(x) - 2, index, -1):
        x[i + 1] = x[i]
    x[index] = key

    return x


# In[12]:


test()


# In[ ]:




