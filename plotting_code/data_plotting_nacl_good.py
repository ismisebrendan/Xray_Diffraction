import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt
import scipy.optimize as opt

plt.rcParams.update({'font.size': 15})

data = ascii.read("nacl_data_good.txt")

angle = data['angle']

rate = data['rate']

# Plot the test scans
plt.plot(angle, rate, label='High-resolution scan')

plt.xlabel(r'$\beta$ ($^{\circ}$)')
plt.ylabel('R (s$^{-1}$)')
plt.title('Plot of the high-resolution scan of NaCl(100)')
plt.legend()
plt.show()
