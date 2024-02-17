import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6])
y=[100,180,190,120,150,180]
z=[270,240,210,180,130,100]
plt.bar(x,y,width=0.5,color=["r","b","g","y","m","c"])
plt.bar(x+.5,z,width=0.5,color=["k","orange","violet","indigo","r","b"])
plt.plot(x,z,marker="+",ls="--",markersize=5,markeredgecolor="k",label="old employ")
plt.plot(x,y,marker="+",ls="--",markersize=5,markeredgecolor="k",label="new employ")
plt.xlabel("EMPLOYEES NAME")
plt.ylabel("EFFORT PERCENTAGE")
plt.title("Best Graph")
plt.xticks(x,["E1","E2","E3","E4","E5","E6"])
plt.legend(loc="best")
plt.show()


