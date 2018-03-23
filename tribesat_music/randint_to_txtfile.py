import numpy as np
from random import randint
arr = []


for n in range(7):
    inst = []
    for i in range(100):
        x = randint(0,5)
        inst.append(x)
    arr.append(inst)
#print(arr)
#print(index)
np.savetxt('test_data5.txt', arr, fmt="%1.4e")
