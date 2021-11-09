#!/usr/bin/env python
# coding: utf-8

# In[1]:


def LIS(L):
    L2=[1 for i in range(len(L))]
    
    for i in range(1,len(L)):
        L3=[1]
        for j in range(0,i,):
            if L[i]>L[j]:
                L3.append(L2[j]+1)
        L2[i]=max(L3)
    return L2,"LIS is "+str(max(L2))


# In[2]:

#example 1
L=[-3, 10, 5, 12, 15]
print(LIS(L))

##([1, 2, 2, 3, 4], 'LIS is 4')
# In[3]:

#example 2
L=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(LIS(L))

##([1, 2, 2, 3, 2, 3, 3, 4, 2, 4, 3, 5, 3, 5, 4, 6], 'LIS is 6')





