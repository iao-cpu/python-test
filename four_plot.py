import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,5)
y = x**3
fig, ax = plt.subplot(nrows=2,ncols=2, figsize=(6,6))
ax[0,1].plot([1,2,3,4], [1,4,9,16], "go")
ax[1,0].plot(x,y,"r^")
ax[0,1].set_title("Square")
ax[1,0].set_title("Cubes")
plt.show()