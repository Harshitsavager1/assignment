#question_1
'''Create a numpy array with 10 elements of the shape(10,1) using np.random and find
out the mean of the elements using basic numpy functions'''

import numpy as np
a = np.random.random((10,1))
print(a)
b = np.mean(a, dtype=np.float64)
print('''Mean of random no's:''',b)

print(80*"_")

#question_2
'''Create a numpy array with 20 elements of the shape(20,1) using np.random find the
variance and standard deviation of the elements'''

import numpy as np
c = np.random.random((20,1))
print(c)
d = (np.std(c, dtype=np.float64))
print("Standard Deviation:",d)
e =(np.var(c, dtype=np.float64))
print("Varience:",e)

print(80*"_")


#question_3
'''Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print
the matrix which is the matrix multiplication of A and B. The shape of the new matrix
should be (10,25). Using basic numpy math functions only find the sum of all the
elements of the new matrix'''


import numpy as np
A = np.random.random((10,20))
print("Matrix A:",A)
import numpy as np
B = np.random.random((20,25))
print("Matrix B:",B)
C=np.dot(A,B)
print("Multiplication A*B=C:",C)
print(np.shape(C))

print(80*"_")

#question_4
'''Create a numpy array A of shape(10,1).Using the basic operations of the numpy array
generate an array of shape(10,1) such that each element is the following function
applied on each element of A. 

f(x)=1 / (1 + exp(-x)) 
Apply this function to each element of A and print the new array holding the value
the function returns
Example:

a=[a1,a2,a3]   
n(new array to be printed )=[ f(a1), f(a2), f(a3)]'''


A=([[1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]])
import math
import numpy as np
np_arr = np.array(A)
l1=[]
def x(ele):
    y=1 / (1 + exp(-ele))
    l1.append(y)
for ele in A:
    x(ele)
    
np_arr = np.array(l1)
print(np_arr)

print(80*"_")



      
