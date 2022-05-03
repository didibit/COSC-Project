#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

# Util the user choose "quit", keep repeating calculations
while True:
    
    #Step 1: Present a menu every time
    print("1. Cartesian distance")
    print("2. Vector x matrix")
    print("3. Normalize")
    print("4. Quit")
    
    # Wait for the user to input their desired calculation and convert to an integer
    a = int(input("Enter command: "))
    
    # If user want to calculate "cartesian distance" (user input is 1)
    if a == 1:
        ## need further input for calculation and create a list
        values = input("Enter 4 float points, use space to seperate: ").split(" ")
        
        # transform each string into its floating point equivalent
        for i in range(len(values)):
             values[i] = float(values[i])
                
        x1 = values[0]
        y1 = values[1]
        x2 = values[2]
        y2 = values[3]
        
        # calculate "cartesian distance"
        cartesian_distance = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 -y1),2))
        # print output
        print("Cartesian distance:", cartesian_distance)
    
    # If user want to calculate "Vector x matrix" (user input is 2)
    elif a == 2:
        # need further input for calculation and create a list
        values_vec = input("Enter 12 float points, use space to seperate: ").split(" ")
        # transform each string into its floating point equivalent
        for i in range(len(values_vec)):
             values_vec[i] = float(values_vec[i])
        
        #  create matrix and vector
        matrix = [[values_vec[0],values_vec[1],values_vec[2]],
                  [values_vec[3],values_vec[4],values_vec[5]],
                  [values_vec[6],values_vec[7],values_vec[8]]]
        
        vector = [values_vec[9],values_vec[10],values_vec[11]]
        
        resultvector = [0, 0, 0]
        
        # multiply a matrix by a vector
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                resultvector[row] += vector[col] * matrix[row][col]
        # print output        
        print("Vector x matrix:", resultvector)
    
    # If user want to calculate "noralization" (user input is 3)
    elif a == 3:
        # need further input for calculation and create a list
        values_normalv = input("Enter 3 float points, use space to seperate: ").split(" ")
        # transform each string into its floating point equivalent
        for i in range(len(values_normalv)):
             values_normalv[i] = float(values_normalv[i])
        
        v1 = values_normalv[0]
        v2 = values_normalv[1]
        v3 = values_normalv[2]   
        
        # calculate the length
        length = math.sqrt(math.pow(v1,2) + math.pow(v2,2) + math.pow(v3,2))
        # shrink it to unit length (divide each element of the vector by length)
        normal_vector = [v1/length, v2/length, v3/length]
        print("Normal vector:", normal_vector)
        
    elif a == 4:
        print("Quit")
        break
        
    else:
        print("You entered an incorrect value.")
            
        


# In[ ]:




