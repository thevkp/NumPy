import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100) # 100 points from 0 to 2π
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine wave")
plt.grid(True)
plt.show()

