import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5]
a=[100,140,160,170,120]
b=[89,96,170,56,100]
plt.barh(x,a,height=.50)
plt.barh(x+.50,b,height=.50)

plt.show()

