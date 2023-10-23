import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})

data = ascii.read("lif_data_filtered.txt")

angle = data['angle']

rate = data['rate']

# Plot the scan
plt.plot(angle, rate, label='Filtered scan')

plt.xlabel(r'$\beta$ ($^{\circ}$)')
plt.ylabel('R (s$^{-1}$)')
plt.title('Plot of the filtered high-resolution scan of LiF (100)')
plt.legend()

plt.show()
