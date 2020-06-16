## All right, this is a program that finds the stiffness matrix of each element of a truss
## in global coordinates. The next step is to find the global stiffness matrix through the assembly method.
import numpy as np
import math
# k is EA/L, for each element of the truss.Let's define the number of elements of the truss:
x = int(input("How many elements have you got? "))
k = np.zeros([x, 1])
# I define k, that has all the EA/L terms for each element.
for i in range(len(k)):
    l=int(input("insert k in order: "))
    k[i]=0+l
print("k vector is:\n", k)
# let's define the angles between the local and the global frame
teta = np.zeros([x, 1])
for elem in range(len(teta)):
    p=float(input("insert the angles in order: "))
    teta[elem]=0+p
print("angles vector:\n", teta)
# KG will contain the single stiffness matrix for each element
KG=[]
for elem in range(len(teta)):
    #print(elem)
    CS=np.array([[math.cos(math.radians(teta[elem]))**2, math.cos(math.radians(teta[elem]))*math.sin(math.radians(teta[elem])), -math.cos(math.radians(teta[elem]))**2, -math.sin(math.radians(teta[elem]))*math.cos(math.radians(teta[elem]))],
          [math.cos(math.radians(teta[elem]))*math.sin(math.radians(teta[elem])), math.sin(math.radians(teta[elem]))**2, -math.sin(math.radians(teta[elem]))*math.cos(math.radians(teta[elem])), -math.sin(math.radians(teta[elem]))**2],
          [-math.cos(math.radians(teta[elem]))**2, -math.sin(math.radians(teta[elem]))*math.cos(math.radians(teta[elem])), math.cos(math.radians(teta[elem]))**2, math.cos(math.radians(teta[elem]))*math.sin(math.radians(teta[elem]))],
          [-math.sin(math.radians(teta[elem]))*math.cos(math.radians(teta[elem])), -math.sin(math.radians(teta[elem]))**2, math.cos(math.radians(teta[elem]))*math.sin(math.radians(teta[elem])), math.sin(math.radians(teta[elem]))**2]])
    print("the CS matrix is:\n", CS)
    for i in range(len(k)):
        #print(i)
        #print(elem)
        if i==elem:
            KG.append(k[i]*CS)
print("The vector KG is: \n ", KG)
























