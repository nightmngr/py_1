# python -m pip install matplotlib
# za da gi simne matplotlib (ova ne sakase)
# sudo apt-get install python3-matplotlib
# DONE!

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot