import numpy as np
from random import *
tab=np.random.randint(0,10,(1,10))
x=float(input())
print(tab)
for n in tab:
    for v in n :
        if v>=x:
            print(v)
        