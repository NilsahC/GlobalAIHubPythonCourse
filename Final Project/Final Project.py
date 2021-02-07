#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Employees():
    def __init__(self, name, age, language):
        self.name = name
        self.language = language
        self.age = age
        
    def showName(self):
        print(self.name)
    
    def showAge(self):
        print(self.age)
        
    def showLanguage(self):
        print("{} speaks {} ".format(self.name,self.language))

employee1 = Employees("Nilsah", "29", "English, German, Turkish")
employee1.showLanguage()

employee2 = Employees("Ali", "38", "German, French, English")
employee2.showLanguage()

employee3 = Employees ("Joe", "21", "English")
employee3.showLanguage()


# In[2]:


class Managers(Employees):
    pass

manager1 = Managers("Jonathan", "48", "English, German, Spanish")
manager1.showLanguage()

manager2 = Managers("Vina", "28", "French, English")
manager2.showLanguage()


# In[ ]:




