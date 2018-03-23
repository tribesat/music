import numpy as np
from random import randint
arr = []
inst = []
index = []
for n in range(7):
    for i in range(15):
        x = randint(0,500)
        inst.append(x)
    arr.append(inst)
#print(arr)
#print(index)
np.savetxt('test_data3.txt', arr, fmt="%1.4e")
