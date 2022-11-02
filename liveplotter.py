import numpy as np
import matplotlib.pyplot as plt
import pythonbno055
import math

previousi = 0
previousy = 0

while True:
    matrix = pythonbno055.values(1)
    i = (1/2*matrix[0]*.001**2) + previousi
    previousi = i
    y = (1/2*matrix[1]*.001**2) + previousy
    previousy = y

print(i)
print(y)


