import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})

data = ascii.read("si111_data_1.txt")

angle1 = data['angle1']
angle2 = data['angle2']
angle3 = data['angle3']
angle4 = data['angle4']

rate1 = data['rate1']
rate2 = data['rate2']
rate3 = data['rate3']
rate4 = data['rate4']

# Plot the test scans
plt.plot(angle1, rate1, label='Scan 1')
plt.plot(angle2, rate2, label='Scan 2')
plt.plot(angle3, rate3, label='Scan 3')
plt.plot(angle4, rate4, label='Scan 4')

plt.title("Diffraction pattern for Si (111) for all 4 measured orientations of the Si mounted on the glass.")
plt.xlabel(r'$\beta$ ($^{\circ}$)')
plt.ylabel('R (s$^{-1}$)')




plt.legend()

plt.show()
