# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:17:16 2023

@author: fanny
"""
#{: .2f}  arrondir au superieur
#a la fin d'un print, ( ,end=", ")
def sum():
    n = int(input("Enter a positive integer"))
    sum=0
    for i in range (n+1):
        sum+=i
    print("the sum is {}".format(sum))
    
    
def sum2():
    n = int(input("Enter a positive integer"))
    sum=0
    for i in range (1,n+1):
        sum+=(i+1)/i**2
    print("the sum is {: .2f}".format(sum))
        

def factorial():
    n= int(input("Enter a positive integer"))
    prod=1
    for i in range(1,n+1):
        prod*=i
    print("the factorial is {}".format(prod))
        
        
def d2():
    for i in range(1,10):
        for j in range(1,10):
            print("{}{}".format(i,j))
               
def d3():
    for i in range(1,10):
        for j in range(1,10):
            if(i!=j):
                print("{}{}".format(i,j))


def d4():
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                print("{}{}{}".format(i,j,k), end=", ")

def d5():
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                if(i+j+k == 22):
                    print("{}{}{}".format(i,j,k), end=", ")

def d6():
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                if(i**3+j**3+k**3 == i*100+j*10+k):
                    print("{}{}{}".format(i,j,k), end=", ")

def d7():
    n= int(input("Enter a positive integer"))
    for i in range (1,n+1):
        if(n%i==0):
            print(i)
 
    
 
def d8():
    n1=1
    n2=1
    n3=0
    for i in range (2,10):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)
    
    
d8()




