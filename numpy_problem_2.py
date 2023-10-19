# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:41:48 2023

@author: fanny
"""

import numpy as np
import matplotlib.pyplot as plt

 
def ex1():
    
    print("Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.")
    vect=np.arange(21)
    vect[9:16]*=(-1)
    print (vect)

    
def ex2():
    print("create a vector with values ranging from 15 to 55 and print all values except the first and last.")
    vect=np.arange(15,56)
    print(vect[1:-1])

def ex3():
    print("create a 3X4 array and iterate over it")

    mat = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12]])
    for i in range (mat.shape[0]):
        if(i!=0):
            print()
        for j in range (mat.shape[1]):
            print(mat[i,j], end=" ")

def ex4():
    print("create a vector of length 10 with values evenly distributed between 5 and 50.")    
    vect=np.linspace(5,50,10, dtype=int)
    print(vect)

def ex5():
    print("create a vector of length 5 filled with arbitrary integers from 0 to 10.")
    vect=np.random.randint(0,11,5, dtype=int)
    print(vect)

def ex6():
    print("program to multiply the values of two given vectors.")
    vect1=np.random.randint(0,11,5)
    vect2=np.random.randint(0,11,5)
    print("vect1 : {}".format(vect1))
    print("vect2 : {}".format(vect2))
    vect3=vect1*vect2
    print("Multiplication of the 2 vectors : {}".format(vect3))
    
def ex7():
    print("create a 3x4 matrix filled with values from 10 to 21")
    mat=np.arange(10,22).reshape(3,4)
    print(mat)

def ex8():
    print("find the number of rows and columns in a given matrix")
    x=np.random.randint(1,10)
    y=np.random.randint(1,10)
    mat=np.random.randint(0,10, size=(x,y))
    print(mat)
    i=mat.shape[0]
    j=mat.shape[1]
    print("number of rows : {}".format(i))
    print("number of colomns : {}".format(j))
    
def ex9():
    print("create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.")
    mat=np.zeros((4,4))
    for i in range (mat.shape[0]):
        for j in range (mat.shape[1]):
            if((i%2==0 and j%2==1) or (i%2==1 and j%2==0)):
                mat[i,j]=1
    mat=mat.astype(int)
    print(mat)
    
def ex10():
    print("find common values between two arrays")
    vect1=[0,10,20,40,60]
    vect2=[10,30,40]
    print(f"vect1 = {vect1}")
    print(f"vect2 = {vect2}")
    
    vect3=[]
    for i in range (len(vect1)):
        for j in range (len(vect2)):
            if(vect1[i]==vect2[j]):
                vect3.append(vect1[i])
    print(vect3)
    
    #or function np.intersect1d(vect1,vect2)

def ex11():
    print("get the unique elements of an array")
    vect1=np.array([10, 10, 20, 20, 30, 30])
    vect2=np.unique(vect1)
    print(f"vect1 = {vect1}")
    print(f"unique elements of vect1 = {vect2}")
    


def ex12():
    print("Write a NumPy program to compute the cross product of two given vectors")
    vect1 = np.array([1, 2, 3])
    vect2 = np.array([4, 5, 6])
    product = np.cross(vect1, vect2)
    print(f"Cross Product of the 2 vectors is : {product}")

def ex13():
    print("convert cartesian coordinates to polar coordinates of a random 10x2 matrix representing cartesian coordinates")
    vect_cartesian=[ 0.89225122, 0.68774813, 0.20392039, 1.22093243, 1.24435921, 1.00358852, 0.37378547, 0.8534585, 0.31999648, 0.567451 ]
    vect_polar=[ 1.02751197, 1.26964967, 0.02567519, 0.85386412, 0.73152767, 0.45822494,1.50634505, 1.47389983, 0.80818521, 0.33001182]

    print(f"vect_cartesian : {vect_cartesian}")
    print(f"vect_polar : {vect_polar}")
    
    
def ex14():
    print("find the closest value (to a given scalar) in an array")
    x=np.arange(100)
    print(x)
    n=float(input("Enter a float between 0 and 99 to compare which number is the closest value : "))
    arr=round(n)
    print(f"the closest value of {n} is {arr}")

a=True    
while a==True:
    try:
        choice = int(input("Enter the number of the exercise between 1 and 14 : "))
        if choice==1:
            ex1()
            a=False
            break
        elif choice==2:
            ex2()
            a=False
            break
        elif choice==3:
            ex3()
            a=False
            break
        elif choice==4:
            ex4()
            a=False
            break
        elif choice==5:
            ex5()
            a=False
            break
        elif choice==6:
            ex6()
            a=False
            break
        elif choice==7:
            ex7()
            a=False
            break
        elif choice==8:
            ex8()
            a=False
            break
        elif choice==9:
            ex9()
            a=False
            break
        elif choice==10:
            ex10()
            a=False
            break
        elif choice==11:
            ex11()
            a=False
            break
        elif choice==12:
            ex12()
            a=False
            break
        elif choice==13:
            ex13()
            a=False
            break
        elif choice==14:
            ex14()
            a=False
            break
        else:
            print("Enter a number between 1 and 14")
    except ValueError:
        print("Enter a number between 1 and 14")

     