import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})

data_good = ascii.read("gap_data_limited_angles_good.txt")
data_filtered = ascii.read("gap_data_limited_angles_filtered.txt")


angle_good10 = data_good['angle10-14']
rate_good10 = data_good['rate10-14']
angle_filtered10 = data_filtered['angle10-14']
rate_filtered10 = data_filtered['rate10-14']

angle_good16 = data_good['angle16-20']
rate_good16 = data_good['rate16-20']
angle_filtered16 = data_filtered['angle16-20']
rate_filtered16 = data_filtered['rate16-20']

angle_good21 = data_good['angle21-27']
rate_good21 = data_good['rate21-27']
angle_filtered21 = data_filtered['angle21-27']
rate_filtered21 = data_filtered['rate21-27']

# Plot the scans
plt.plot(angle_good10, rate_good10, label=r'10$^{\circ}$ ≤ $\beta$ ≤ 14$^{\circ}$ Unfiltered')
plt.plot(angle_filtered10, rate_filtered10, label=r'10$^{\circ}$ ≤ $\beta$ ≤ 14$^{\circ}$ Filtered')
plt.plot(angle_good16, rate_good16, label=r'16$^{\circ}$ ≤ $\beta$ ≤ 20$^{\circ}$ Unfiltered')
plt.plot(angle_filtered16, rate_filtered16, label=r'16$^{\circ}$ ≤ $\beta$ ≤ 20$^{\circ}$ Filtered')
plt.plot(angle_good21, rate_good21, label=r'21$^{\circ}$ ≤ $\beta$ ≤ 27$^{\circ}$ Unfiltered')
plt.plot(angle_filtered21, rate_filtered21, label=r'21$^{\circ}$ ≤ $\beta$ ≤ 27$^{\circ}$ Filtered')


plt.xlabel(r'$\beta$ ($^{\circ}$)')
plt.ylabel('R (s$^{-1}$)')
plt.title('Plot of the high-resolution scan of GaP(111) for the limited angles')
plt.legend()

plt.show()
