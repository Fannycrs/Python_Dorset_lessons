# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:23:20 2023

@author: fanny
"""
print("""
      
num= int(input("Enter an integer value :"))
while num>0 :
    res=num//3
    print("the integer division of {} by 3 gives : {}".format(num,res))
    num= int(input("Enter an integer value :"))
print("we're done")



num = int (input ("Enter an integer value:"))
ndiv = 1 # We initialize the division counter set to zero
while ndiv< num:
    res = num // ndiv
    print ("The integer division of {} by {} gives: {}". format (num, ndiv, res))
    ndiv = ndiv + 1 # Increase the value of the divisor counter made a unit
print ("We're done")
print ("Total number of divisions: {}". format (ndiv))


num = int (input ("Enter an integer value:"))
ndiv = 0 # We initialize the division counter set to zero
while ndiv< num:
    res = num // 3
    print ("The integer division of {} by {} gives: {}". format (num, ndiv, res))
    ndiv = ndiv + 1 # Increase the value of the divisor counter made a unit
    num = int (input ("Enter an integer value:"))
print ("We're done")
print ("Total number of divisions: {}". format (ndiv))



num= int(input("Enter an integer value : "))
i=0
while num > 0 :
    if (num % 3) == 0 :
        i+=1
    num-=1
print(f"Total of numbers divided by 3 : {i}")




sum=0
i=0
while i<11 :
    sum+=i
    i+=1
print(sum)



i=0
sum=0
while i<10 :
    i+=1
    num=float(input("Enter a float : "))
    sum+=num
avrg = sum/10
print(f"The average of the 10 numbers is : {avrg}")





num=int(input("Enter an integer : "))
num2=num
res=1
while num>0 :
    res=res*num
    num-=1
print(f"the factorial of {num2} is {res}")

""")

name="a7a"
size = len(name)
i=0
while i<size :
    if name[i].isdecimal():
        print(name[i])
        break;
    print(name[i], end=' ')
    i+=1
print("\nThe execution has stopped")




name="a7a"
size = len(name)
i=-1
while i<size -1:
    i+=1
    if not name[i].isalpha():
        continue
    print(name[i], end=' ')
    



























