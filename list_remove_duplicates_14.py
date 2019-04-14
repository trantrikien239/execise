import numpy as np
import random as rd

a = np.random.randint(20,size = rd.randint(0,20))
print(a)

def unique(ls):
    return sorted(list(set(ls)))

def unique2(ls):
    uq_ls = []
    for num in ls:
        if num in uq_ls:
            continue
        else:
            uq_ls.append(num)
    return sorted(uq_ls)#.sort()
print(unique(a))
print(unique2(a))
