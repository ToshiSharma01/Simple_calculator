#!/usr/bin/env python
# coding: utf-8

# In[3]:


#SIMPLE CALCULATOR
#Here we can use the funtions for performing the arithmetic operations
#function to Adding two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtracting two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiplying two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to dividing two numbers
def divide(num1, num2):
    return num1 / num2

print("Select operation.")
print("1.Add")
print("2.Divide")
print("3.Multiply")
print("4.Subtract")

# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",divide(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",subtract(number_1, number_2))
else:
    print("Input is invalid")


# In[ ]:





# In[ ]:




