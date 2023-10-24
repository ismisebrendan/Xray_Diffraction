import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt
import scipy.optimize as opt

plt.rcParams.update({'font.size': 15})

data_filtered = ascii.read("si111_data_filtered.txt")
data_good = ascii.read("si111_data_good.txt")


angle_filtered = data_filtered['angle']
rate_filtered = data_filtered['rate']

angle_good = data_good['angle']
rate_good = data_good['rate']

# Plot the scans
plt.plot(angle_filtered, rate_filtered, label='Filtered scan')
plt.plot(angle_good, rate_good, label='High-resolution scan')


plt.xlabel(r'$\beta$ ($^{\circ}$)')
plt.ylabel('R (s$^{-1}$)')
plt.title('Plot of the high-resolution scans both filtered and unfiltered of Si(111)')
plt.legend()
plt.show()


# Fitting function
def gaussian(x, a, b, c, d):
    return a * np.exp(-((x-b)/c)**2) + d

plt.scatter(angle_filtered, rate_filtered, label='Filtered scan', s=3)
plt.scatter(angle_good, rate_good, label='High-resolution scan', s=3)
plt.xlabel(r'$\beta$ ($^{\circ}$)')
plt.ylabel('R (s$^{-1}$)')
plt.title('Plot of the high-resolution diffracton patterns both filtered and unfiltered of Si(111) with peaks fitted')


peak1 = np.arange(5.1,6.4,0.1)
p1 = np.rint((peak1-3)*10).astype(int)
fit_peak1 = opt.curve_fit(gaussian, peak1, rate_good[p1], p0=[400, 5.5, 3, 200])[0]
a, b, c, d = fit_peak1
plt.plot(peak1, a * np.exp(-((peak1-b)/c)**2) + d, label="Fit of peak 1")
b = np.around(b,1)
print('Peak 1 occurs at ' + str(b) + ' degrees')


peak2 = np.arange(6.2,7.3,0.1)
p2 = np.rint((peak2-3)*10).astype(int)
fit_peak2 = opt.curve_fit(gaussian, peak2, rate_good[p2], p0=[600, 6.5, 1, 200])[0]
a, b, c, d = fit_peak2
plt.plot(peak2, a * np.exp(-((peak2-b)/c)**2) + d, label="Fit of peak 2")
b = np.around(b,1)
print('Peak 2 occurs at ' + str(b) + ' degrees')


peak3 = np.arange(16,19,0.1)
p3 = np.rint((peak3-3)*10).astype(int)
fit_peak3 = opt.curve_fit(gaussian, peak3, rate_good[p3], p0=[100, 17, 1, 60])[0]
a, b, c, d = fit_peak3
plt.plot(peak3, a * np.exp(-((peak3-b)/c)**2) + d, label="Fit of peak 3")
b = np.around(b,1)
print('Peak 3 occurs at ' + str(b) + ' degrees')


peak4 = np.arange(19,21,0.1)
p4 = np.rint((peak4-3)*10).astype(int)
fit_peak4 = opt.curve_fit(gaussian, peak4, rate_good[p4], p0=[100, 19.5, 1, 60])[0]
a, b, c, d = fit_peak4
plt.plot(peak4, a * np.exp(-((peak4-b)/c)**2) + d, label="Fit of peak 4")
b = np.around(b,1)
print('Peak 4 occurs at ' + str(b) + ' degrees')


peak5 = np.arange(23,25,0.1)
p5 = np.rint((peak5-3)*10).astype(int)
fit_peak5 = opt.curve_fit(gaussian, peak5, rate_good[p5], p0=[100, 23.8, 1, 20])[0]
a, b, c, d = fit_peak5
plt.plot(peak5, a * np.exp(-((peak5-b)/c)**2) + d, label="Fit of peak 5")
b = np.around(b,1)
print('Peak 5 occurs at ' + str(b) + ' degrees')


peak6 = np.arange(25,30,0.1)
p6 = np.rint((peak6-3)*10).astype(int)
fit_peak6 = opt.curve_fit(gaussian, peak6, rate_good[p6], p0=[100, 27, 1, 20])[0]
a, b, c, d = fit_peak6
plt.plot(peak6, a * np.exp(-((peak6-b)/c)**2) + d, label="Fit of peak 6")
b = np.around(b,1)
print('Peak 6 occurs at ' + str(b) + ' degrees')


peak7 = np.arange(33,35,0.1)
p7 = np.rint((peak7-3)*10).astype(int)
fit_peak7 = opt.curve_fit(gaussian, peak7, rate_good[p7], p0=[100, 34, 1, 20])[0]
a, b, c, d = fit_peak7
plt.plot(peak7, a * np.exp(-((peak7-b)/c)**2) + d, label="Fit of peak 7")
b = np.around(b,1)
print('Peak 7 occurs at ' + str(b) + ' degrees')

plt.legend()
plt.show()