import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt


plt.rcParams.update({'font.size': 15})

data_filtered = ascii.read("gap_data_filtered.txt")
data_good = ascii.read("gap_data_good.txt")


angle_filtered = data_filtered['angle']
rate_filtered = data_filtered['rate']

angle_good = data_good['angle']
rate_good = data_good['rate']

# Plot the scans
plt.plot(angle_filtered, rate_filtered, label='Filtered scan')
plt.plot(angle_good, rate_good, label='High-resolution scan')


plt.xlabel(r'$\beta$ ($^{\circ}$)')
plt.ylabel('R (s$^{-1}$)')
plt.title('Plot of the high-resolution scans both filtered and unfiltered of GaP (111)')
plt.legend()
plt.show()
