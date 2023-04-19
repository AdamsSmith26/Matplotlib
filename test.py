import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints, "h") #function is used to draw points (markers) in a diagram,  x-axis, y-axis
# plt.show()

# xpoints = np.array([1, 2, 6, 8, 3])  #(1, 3) -> (2, 8) -> (6,  1) -> (8, 10) -> (3, 6)
# ypoints = np.array([3, 8, 1, 10, 6]) 

# plt.plot(xpoints, ypoints)
# plt.show()

ypoints = np.array([3, 8, 1, 10, 5, 7]) # x-axis dafault [0, 1, 2, 3, 4 .....]

plt.plot(ypoints)
plt.show()