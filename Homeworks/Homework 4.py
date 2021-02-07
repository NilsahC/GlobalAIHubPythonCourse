#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Animals:
    def __init__(self, name, colour, species):
        self.name = name
        self.colour = colour
        self.species = species
    
    def print_colour(self):
        print(self.name + " is " + self.colour)
    
    def print_species(self):
        print(self.name + " is " + self.species)


# In[2]:


class Dogs(Animals):
    pass

dog = Dogs("Cano", "white", "maltipo")
dog.print_colour()


# In[3]:


class Cats(Animals):
    pass

cat = Cats("Pamuk", "brown", "tekir")
cat.print_species()

