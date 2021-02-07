#!/usr/bin/env python
# coding: utf-8

# # Homework 1 question 1

# In[3]:


my_list = [1,3,5,7,9,11]
len(my_list)


# In[4]:


my_list_fh = my_list[0:3]
print(my_list_fh)
my_list_sh = my_list[3:6]
print(my_list_sh)


# In[5]:


my_list_sh.extend(my_list_fh)
print(my_list_sh)


# In[6]:


my_list = my_list_sh
print(my_list)


# # Homework 1 question 2

# In[7]:


num = int(input("Please enter a single digit integer : "))

for number in range(0, num+1):
    if(number % 2 ==0):
        print("{0}".format(number))


# In[ ]:




