# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:37:25 2023

@author: fanny
"""

import numpy as np
import math

def ex1():
    Ang_to_nano= np.linspace(1,5,21)
    print(Ang_to_nano)
    le = len(Ang_to_nano)
    for i in range(le):
        Ang_to_nano[i] = Ang_to_nano[i]/10
        print(Ang_to_nano)



def ex2():
    x0 = float(input("Enter the value of X0 : "))
    s = float(input("Enter the value of s : "))
    n1 = float(input("Enter the minimal value of the interval : "))
    n2 = float(input("Enter the maximal value of the interval : "))
    n3 = int(input("Enter the the number of points : "))
    x = np.linspace(n1, n2, n3)
    y = np.zeros(n3)
    for i in range(n3):
        y[i] = math.exp((-(x[i]-x0)**2)/(2 * s**2))/math.sqrt(2*math.pi)
    for i in range(n3):
        print(f"{x[i]:.3f} {y[i]:.5f}")
    


def ex3():

    temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4,
                20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    temp_mar = np.asarray(temp_mar)
    mean = temp_mar.mean()
    print(f"The average sea surface temperature in 2014 is {mean:2f} ")
    mini = temp_mar.min()
    maxi = temp_mar.max()
    for i in range(len(temp_mar)):
        if mini == temp_mar[i]:
            moismin = months[i]
            
    for i in range(len(temp_mar)):
        if maxi == temp_mar[i]:
            moismax = months[i]
    print(f"The month in which the sea surface has been coldest is {moismin} with {mini} degrees")
    print(f"The month in which the sea surface has been warmest is {moismax} with {maxi} degrees")
    


def ex4():
    nbstudent=int(input("Enter the number of students : "))
    mat=np.zeros((nbstudent,4))
    for i in range (nbstudent):
        theorie=int(input(f"Enter the theory note of the student number {i} : "))
        problem=int(input(f"Enter the problem note of the student number {i} : "))
        totalmark=0.4*theorie+0.6*problem
        mat[i,0]=int(i)
        mat[i,1]=theorie
        mat[i,2]=problem
        mat[i,3]=totalmark
    print()
    print("st.nbr theorie problem finalmark")
    print(mat)
    
    print()
    maxi=0
    mini=20
    index=0
    sum=0
    for i in range (nbstudent):
        sum+=mat[i,3]
        if(maxi<mat[i,3]):
            maxi=mat[i,3]
            index=int(mat[i,0])
        if(mini>mat[i,3]):
            mini=mat[i,3]
    print(f"maximum total grade : {maxi} and the student number {index} obtained it")
    print(f"minimum total grade : {mini}")
    avg=sum/nbstudent
    print(f"the average is {avg}")



print("Choose an exercise : ")
print("1. Convert Angstroms to Nanometers")
print("2. Table of values")
print("3. Sea temperature statistics")
print("4. Exam grades")


while True:
    try:
        choice = int(input("Enter the number of the exercise : "))
        if choice==1:
            ex1()
            break
        elif choice==2:
            ex2()
        elif choice==3:
            ex3()
        elif choice==4:
            ex4()
        else:
            print("Enter a number between 1 and 4")
    except ValueError:
        print("Enter a number between 1 and 4")



