# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:12:28 2023

@author: fanny
"""

import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline
"""
#exemple1
x=np.linspace(-2,2,101)
y=x**2
print(x)
plt.plot(x,y)
plt.title("Graph of x^2 vs x")
plt.show()

#exemple 2
x=np.linspace(0,3*np.pi,500)
plt.plot(x,np.sin(x**2))
plt.title("A simple chirp")
plt.show()

#nom abscisse et ordonee
plt.xlabel("x")
plt.ylabel("f (x)")
plt.xlim(-1.5,1.5)
plt.ylim(-0.5,2.5)
plt.title("Chart title")
plt.plot(x,y)
plt.show()

x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f (x)")
y=x**2
plt.plot(x,y, "g",label="x**2")
y2=x**4
plt.plot(x,y2, "r",label="x**4")
plt.show()

#plt.savefig("fig1.png")
#plt.savefig("fig1.jpg")


nb=int(input("Enter the number of points : "))
x=np.linspace(-1,1,nb)
plt.plot(x,np.cos(2*x*np.pi))
plt.title("Body function (2pix)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("cos2pix.png")
plt.show()




nb=int(input("Enter the number of points : "))
x=np.linspace(-1,1,nb)
y1=np.cos(2*x*np.pi)
y2=np.sin(2*x*np.pi)
plt.plot(x,y1, label="cos2pix")
plt.plot(x,y2, label="sin2pix")
plt.legend()
plt.title("Body function (2pix)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("trigonometric.png")
plt.show()





nb=int(input("Enter the number of points : "))
x=np.linspace(0,4,nb)
y=np.sin(np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x))
plt.plot(x,y)
plt.legend()
plt.title("Body function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()




temp=float(input("Enter a temperature : "))
vm=np.linspace(2,10,100)
y=0.08206*temp/vm
plt.plot(vm,y)
plt.legend()
plt.title("Isotherm (ideal gas)")
plt.xlabel("Vm (in L/mol)")
plt.ylabel("pressure (in Pa)")
plt.show()

plt.savefig("isotherm.jpg")




nb=int(input("Enter the number of temperature you want : "))
for i in range (nb):
    temp=float(input("Enter a temperature : "))
    vm=np.linspace(2,10,100)
    y=0.08206*temp/vm
    plt.plot(vm,y, label =f"T={temp}K")

plt.legend()
plt.title("Isotherm (ideal gas)")
plt.xlabel("Vm (in L/mol)")
plt.ylabel("pressure (in Pa)")
plt.show()

plt.savefig("isotherms.jpg")

#exo1

nb=int(input("Enter the number of points : "))
x0=int(input("x0 = :"))
s=float(input("s = :"))
start = float(input("Enter the start value : "))
final = float(input("Enter the final value : "))
x=np.linspace(start,final,nb)
y=(1/np.sqrt(2*np.pi))*np.exp((-1/2)*(x-x0)**(2)/s**(2))
plt.plot(x,y)
plt.legend()
plt.title("Gaussian function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()





#exo2



nb=int(input("Enter the number of points : "))
x=np.linspace(0,3,nb)
y1=np.exp(-x)
y2=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y1, label="exp(-x)")
plt.plot(x,y2, label="sin(3pix)exp(-x)")
plt.legend()
plt.title("2 functions")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()



#exo3

curves = int(input("Enter the number of curves you want : "))
nb=int(input("Enter the number of points : "))

start = float(input("Enter the start value : "))
final = float(input("Enter the final value : "))

for i in range (curves):
    x0=int(input("x0 = :"))
    s=float(input("s = :"))
    x=np.linspace(start,final,nb)
    y=(1/np.sqrt(2*np.pi))*np.exp((-1/2)*(x-x0)**(2)/s**(2))
    plt.plot(x,y, label=f"x0 = {x0}, s = {s}")
plt.legend()
plt.title("Gaussian function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()



#exo3



x=np.linspace(0,3,nb)
y1=np.exp(-x)
y2=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y1, label="exp(-x)")
plt.plot(x,y2, label="sin(3pix)exp(-x)")
plt.legend()
plt.title("2 functions")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()



x=np.linspace(-2,2,150)
y1=((x**(2/3)-np.sqrt(x**(4/3)+4-4*x**(2))))/2
y2=((x**(2/3)+np.sqrt(x**(4/3)+4-4*x**(2))))/2
plt.plot(x,y1,"r")
plt.plot(x,y2,"g")
plt.title("Bonne chance!!!")
plt.show()

"""
x=np.linspace(0,5,100)

y1=x-2.5
y2=-x
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()





















