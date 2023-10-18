# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:42:49 2023

@author: fanny
"""

#list.append('nvlle var')    : ajout variable fin de liste
#list.remove('var a enlever')
#list.pop(position)
#len(liste) : longueur
#liste[n:n+1]   : affiche l'élement n a n+1 non inclu  , [1:], [:-1] ,[n::n+1]
#liste[5][1]  write index item 1 from the list[5]  si liste de liste
#string ->  string.split('char qui separe la liste et qui est enleveé')

#tuples :  tu=("","","")            tuples immutables (pas de .append)


#set     : se={"","",""}

def exo1() :
    liste =[1,2,3,4,5,6]
    for number in liste :
        print (number)
    liste.append(7)
    for number in liste :
        print (number)
    print("----")
    print(liste[:-1])
    print("----")
    print(liste[::5])
    
    
def exo2() :
    n =int(input("Enter a n value"))
    thelist=[]
    for i in range (1,n+1):
        thelist.append(1/i)
    Sn=sum(thelist)
    
def exo3():
    line=input("enter, in a single line and separated by spaces, the desired temperature value")
    smooth_txt=line.split()
    print("List is now{}".format(smooth_txt))
    temp=[]
    for ele in smooth_txt :
        value=float(ele)
        temp.append(value)
    print("the final list is {}".format(temp))


def exo4():
    a=[1,3,5,7,11]
    b=[13,17]
    c=a+b
    print("first instruction print : {}".format(c))
    b[0]=-1
    d=[]
    for e in a :
        d.append(e+1)
    d.append(b[0]+1)
    d.append(b[-1]+1)
    print(d[1:4])

def exo5():
    n =int(input("Enter a n value"))
    liste=[]
    for i in range (n+1):
        liste.append(i**2)
        print(liste[i])
    
def exo6():
    
    listename=[]
    listenote=[]
    sum=0
    stud="a"
    stud=(input("Enter the student name : "))
    note=float(input("Enter his note : "))
    while(stud!=""):     
        listename.append(stud)
        listenote.append(note)
        sum+=note
        stud=(input("Enter the student name"))
        if (stud!=""):
            note=float(input("Enter his note"))
    n=len(listename)
    for i in range (n):
        print(f"{listename[i]:14} : {listenote[i]:5.1f}")
    print("---------")
    avg=sum/n
    print(f"the average is {avg:5.1f} ")
exo6()