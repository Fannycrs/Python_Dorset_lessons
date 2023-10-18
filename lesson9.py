# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:23:30 2023

@author: fanny
"""

#if we don t konw the number of parameter : def(*args)
# def(**kwargs)  the function will receive de idctionnary of arguments

# try, except, else, finally

def biggest_nbr(a,b):
    if(a>b):
        max= a
    else:
        max=b
    return max

def biggest_nbr2():
    liste=[]
    for i in range (5):
        n=int(input("Enter an int : "))
        liste.append(n)
    min=liste[0]
    max=liste[0]
    for j in range (5):
        if(min>liste[j]):
            min=liste[j]
        elif(max<liste[j]):
            max=liste[j]
    print(f"{min}, {max}")
    return(min,max)

def exo3():
    num=input("Enter a number : ")
    while type(num)!=int:
        try:
            num=int(num)
        except:
            num=input("Enter a number : ")
    if(num%2)==0 :
        print("{0} is even".format(num))
    else :
        print("{0} is odd".format(num))


def exo4():
    num=input("Enter a number : ")
    while type(num)==int:
        try:
            num=int(num)
            num=input("Enter a number : ")
        except:
            break


def exo8():
    nb = 0
    while type(nb) == int:
        try:
            nb = int(input('Enter a number'))
            if nb%2 == 0:
                print(f"{nb} is Even")
            else:
                print(f"{nb} is Odd")
        except:
            nb="str"

def exo9():
    nb = 0
    sum=1
    while type(nb) == int:
        try:
            nb = int(input('Enter a number : '))
            for i in range (1,nb+1):
                if nb%i == 0:
                    sum+=1
            if(sum==2):
                print("prime number")
            else:
                print("not a prime number")
                
        except:
            nb="str"

def exo10():
    test2= True
    while test2 == True:
        try:
            nb = int(input('Enter a number'))
            test = False
            for i in range(2,nb):
                if nb%i ==0:
                    test = True
            if test == False:
                print(f"{nb} is prime")
            else:
                print(f"{nb} is not prime")
        except ValueError as error:
            test2 = False
            
            
            
            
          
            
exo9()

