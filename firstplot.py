import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,5)
y = x**3
plt.figure(figsize=(15,5))
plt.plot([1,2,3,4], [1,4,9,16], "go", x,y, 'r^')
plt.title("First Plot")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()

x = np.arange(16).reshape((4, 4))
print("Original array:",x)
print("After splitting horizontally:")
print(np.hsplit(x, [2, 6]))