#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Germán R. Pardo González
# 202338054


# In[1]:


def wordcount(text):
    if text != '':
        
        counter = 0

        space = []
        space.append(text[0].isspace())

        if space[-1] == False:
            counter = 1

        for letter in text:
            if space[-1] and letter.isspace() == False:
                counter += 1

            space.append(letter.isspace())
        
        
    else:
        counter = 0
    return counter


# In[ ]:




