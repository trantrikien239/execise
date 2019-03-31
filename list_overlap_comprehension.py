import numpy as np
import random as rd

a = np.random.randint(20,size = rd.randint(0,20))
b = np.random.randint(20,size = rd.randint(0,20))
print("a = ", a)
print("b = ", b)

c = np.unique([x for x in a for y in b if x == y])
print("c = ", c)