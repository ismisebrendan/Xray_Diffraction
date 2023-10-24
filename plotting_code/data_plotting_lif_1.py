import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})

data = ascii.read("lif_data_1.txt")

angle1 = data['angle1']
angle2 = data['angle2']
angle3 = data['angle3']
angle4 = data['angle4']
angle5 = data['angle5']

rate1 = data['rate1']
rate2 = data['rate2']
rate3 = data['rate3']
rate4 = data['rate4']
rate5 = data['rate5']

# Plot the test scans
plt.plot(angle1, rate1, label='Scan 1')
plt.plot(angle2, rate2, label='Scan 2')
plt.plot(angle3, rate3, label='Scan 3')
plt.plot(angle4, rate4, label='Scan 4')
plt.plot(angle5, rate5, label='Scan 5')

plt.title("Diffraction pattern for LiF(100) for all 5 measured orientations of the LiF mounted on the glass.")
plt.xlabel(r'$\beta$ ($^{\circ}$)')
plt.ylabel('R (s$^{-1}$)')
plt.legend()

plt.show()
