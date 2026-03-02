import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

data = np.random.randn(50)
plt.style.use('Solarize_Light2')
plt.plot(data)
plt.show()
