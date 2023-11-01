# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:50:11 2023

@author: fanny
"""

def ex1():
    f_name= open("test2.txt")
    for name in f_name:
        print(name)
        


def ex2():
    f=open("test2.txt","r") #reading
    f=open("test2.txt","w") #writing
    f=open("test2.txt","r")
    f=open("test2.txt","a") #appending
    f=open("test2.txt","r+") #read+write
    print(f.name)
    print(f.mode)
    f.close()
    
def ex3():
    with open("test2.txt","r") as f:         #2eme methode
        f_contents=f.read()
        print(f_contents)
def ex4():
    with open("test2.txt","r") as f:         #2eme methode
        f_contents=f.readlines()
        print(f_contents)

def ex5():
    with open("test2.txt","r") as f:         #2eme methode
        f_contents=f.readline()
        print(f_contents, end=' ')
        f_contents=f.readline()
        print(f_contents, end=' ')
        f_contents=f.readline()
        print(f_contents, end=' ')
        
def ex6():
    with open("test5.txt","w") as f:   #creer un nouveau texte
        f.write("Test")        
def ex7():
    with open("test5.txt","w") as f:   #creer un nouveau texte
        val='10'
        val2='niamh'
        f.write(val+val2)
        #f.seek(0)
        #f.write("Test")
        #f.seek(6)
def ex8():                             #copie d'un fichier
    with open('test2.txt','r') as rf:
        with open('test_copy.txt','w') as wf:
            for line in rf:
                wf.write(line)
ex8()