# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 09:14:26 2023

@author: fanny
"""
#def(*names) si tuple, ** pour dictionnary
def exo1():
    numberstr = input("Enter an int : ")
    liste=[]
    i=0
    while numberstr!="":
        i+=1
        number=int(numberstr)
        liste.append(number)
        numberstr = input("Enter an int : ")
    sum=0
    for ele in liste:
        sum+=ele
    avg=sum/i
    
    print(f"the average of all the values is {avg}")
    
def exo2():
    names=input("Enter the names separated by blanks : ")
    liste=names.split(" ")
    for i in range (len(liste)):
        print(f"Hi {liste[i]}")
    
    print(f"There are {len(liste)} people")


def exo3():
    listatoms=[['H',1.008],['C',12.011],['N',14.007],['O',15.999],['S',32.065],['Cl',35.453]]
    mass=0
    for i in range (len(listatoms)):
        num=int(input(f"Enter the number of the element {listatoms[i][0]} : "))
        mass+=num*listatoms[i][1]
    
    print(f"The molecular mass is {mass}")
    
    
def exo4():
    degree= int(input("Enter the maximum degree of the polynomial : "))
    listecoeff=[]
    
    for i in range(degree+1):
        listecoeff.append(float(input(f"Enter the coefficient of the degree {i} : ")))
    value=float(input("Enter the x value : "))
    sum=0
    for i in range(len(listecoeff)):
        sum+=listecoeff[i]*(value**i)
    print(f"The value of the polynomial with x = {value} is {sum}")




    
exo4()