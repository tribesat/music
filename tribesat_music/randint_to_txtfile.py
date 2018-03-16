import numpy as np
from random import randint
arr = []
inst = []
index = []
for n in range(7):
    for i in range(20):
        x = randint(0,50)
        inst.append(x)
    arr.append(inst)
#print(arr)
#print(index)
np.savetxt('test_data.txt', arr, fmt="%1.4e")
