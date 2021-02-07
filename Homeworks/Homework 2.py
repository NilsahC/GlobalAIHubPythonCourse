#!/usr/bin/env python
# coding: utf-8

# # Homework 2 question 1

# In[1]:


user_name = "Nilsah"
password ="Nilsahlovespython"

user_name1 =input("Please enter your user name:")

password1= input("Please enter your password:")

if (user_name != user_name1 and password == password1):
    print("Invalid user name")
elif (user_name==user_name1 and password != password1):
    print("Invalid password")
elif (user_name != user_name1 and password!= password1):
    print("Invalid user name and password")
else:
    print("You are now succesfully logged in the system.")


# # Homework 2 extra question

# In[2]:


username_password = {"username": "Nilsah", "password": "Nilsahlovespython"}

user_name1 =input("Please enter your user name:")

password1= input("Please enter your password:")

if username_password.get("username") != user_name1 and username_password.get("password") == password1:
    print("Invalid user name")
elif username_password.get("username") ==user_name1 and username_password.get("password") != password1:
    print("Invalid password")
elif username_password.get("username") != user_name1 and username_password.get("password") != password1:
    print("Invalid user name and password")
else:
    print("You are now succesfully logged in the system.")

