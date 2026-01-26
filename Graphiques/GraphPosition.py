import matplotlib.pyplot as plt
import numpy as np
from GetData import resultPosition

# Points arbitraires
points = np.array(resultPosition)

plt.plot(points[:,0], points[:,1], marker='o')
plt.axis('equal')
plt.grid()
plt.show()