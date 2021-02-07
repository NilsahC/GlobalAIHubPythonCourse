#!/usr/bin/env python
# coding: utf-8

# In[1]:


prime_numbers = 0

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True
                

for i in range(int(input("Enter that how many numbers you wish to check: "))):
    if is_prime_number(i):
        prime_numbers += 1
        print(i)

print("There are " + str(prime_numbers) + " prime numbers.")

