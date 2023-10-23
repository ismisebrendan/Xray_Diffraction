import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt
import scipy.optimize as opt


data_filtered_all = ascii.read("gap_data_filtered.txt")
data_good_all = ascii.read("gap_data_good.txt")


angle_filtered = data_filtered_all['angle']
rate_filtered = data_filtered_all['rate']

angle_good = data_good_all['angle']
rate_good = data_good_all['rate']

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


# Fitting function
def gaussian(x, a, b, c, d):
    return a * np.exp(-((x-b)/c)**2) + d

plt.scatter(angle_filtered, rate_filtered, label='Filtered scan', s=3)
plt.scatter(angle_good, rate_good, label='High-resolution scan', s=3)
plt.scatter(angle_good10, rate_good10, label=r'10$^{\circ}$ ≤ $\beta$ ≤ 14$^{\circ}$ Unfiltered', s=3)
plt.scatter(angle_filtered10, rate_filtered10, label=r'10$^{\circ}$ ≤ $\beta$ ≤ 14$^{\circ}$ Filtered', s=3)
plt.scatter(angle_good16, rate_good16, label=r'16$^{\circ}$ ≤ $\beta$ ≤ 20$^{\circ}$ Unfiltered', s=3)
plt.scatter(angle_filtered16, rate_filtered16, label=r'16$^{\circ}$ ≤ $\beta$ ≤ 20$^{\circ}$ Filtered', s=3)
plt.scatter(angle_good21, rate_good21, label=r'21$^{\circ}$ ≤ $\beta$ ≤ 27$^{\circ}$ Unfiltered', s=3)
plt.scatter(angle_filtered21, rate_filtered21, label=r'21$^{\circ}$ ≤ $\beta$ ≤ 27$^{\circ}$ Filtered', s=3)
plt.xlabel(r'$\beta$ ($^{\circ}$)')
plt.ylabel('R (s$^{-1}$)')
plt.title('Plot of the high-resolution diffracton patterns both filtered and unfiltered of GaP(111) with peaks fitted')


peak1 = np.arange(5.2,6.3,0.1)
p1 = np.rint((peak1-3)*10).astype(int)
fit_peak1 = opt.curve_fit(gaussian, peak1, rate_good[p1], p0=[250, 5.5, 3, 100])[0]
a, b, c, d = fit_peak1
plt.plot(peak1, a * np.exp(-((peak1-b)/c)**2) + d, label="Fit of peak 1")
b = np.around(b,1)
print('Peak 1 occurs at ' + str(b) + ' degrees')


peak2 = np.arange(6,7.3,0.1)
p2 = np.rint((peak2-3)*10).astype(int)
fit_peak2 = opt.curve_fit(gaussian, peak2, rate_good[p2], p0=[600, 6.3, 1, 100])[0]
a, b, c, d = fit_peak2
plt.plot(peak2, a * np.exp(-((peak2-b)/c)**2) + d, label="Fit of peak 2")
b = np.around(b,1)
print('Peak 2 occurs at ' + str(b) + ' degrees')


peak3 = np.arange(10.4,12.4,0.1)
p3 = np.rint((peak3-10)*10).astype(int)
fit_peak3 = opt.curve_fit(gaussian, peak3, rate_good10[p3], p0=[120, 11, 1, 80])[0]
a, b, c, d = fit_peak3
plt.plot(peak3, a * np.exp(-((peak3-b)/c)**2) + d, label="Fit of peak 3")
b = np.around(b,1)
print('Peak 3 occurs at ' + str(b) + ' degrees')


peak4 = np.arange(12.4,14,0.1)
p4 = np.rint((peak4-10)*10).astype(int)
fit_peak4 = opt.curve_fit(gaussian, peak4, rate_good10[p4], p0=[120, 12.7, 1, 80])[0]
a, b, c, d = fit_peak4
plt.plot(peak4, a * np.exp(-((peak4-b)/c)**2) + d, label="Fit of peak 4")
b = np.around(b,1)
print('Peak 4 occurs at ' + str(b) + ' degrees')


peak5 = np.arange(16,18.5,0.1)
p5 = np.rint((peak5-16)*10).astype(int)
fit_peak5 = opt.curve_fit(gaussian, peak5, rate_good16[p5], p0=[120, 17.5, 1, 80])[0]
a, b, c, d = fit_peak5
plt.plot(peak5, a * np.exp(-((peak5-b)/c)**2) + d, label="Fit of peak 5")
b = np.around(b,1)
print('Peak 5 occurs at ' + str(b) + ' degrees')


peak6 = np.arange(18.5,21,0.1)
p6 = np.rint((peak6-3)*10).astype(int)
fit_peak6 = opt.curve_fit(gaussian, peak6, rate_good[p6], p0=[120, 19.5, 1, 80])[0]
a, b, c, d = fit_peak6
plt.plot(peak6, a * np.exp(-((peak6-b)/c)**2) + d, label="Fit of peak 6")
b = np.around(b,1)
print('Peak 6 occurs at ' + str(b) + ' degrees')


peak7 = np.arange(23,25.3,0.1)
p7 = np.rint((peak7-21)*10).astype(int)
fit_peak7 = opt.curve_fit(gaussian, peak7, rate_good21[p7], p0=[120, 23.5, 1, 80])[0]
a, b, c, d = fit_peak7
plt.plot(peak7, a * np.exp(-((peak7-b)/c)**2) + d, label="Fit of peak 7")
b = np.around(b,1)
print('Peak 7 occurs at ' + str(b) + ' degrees')


peak8 = np.arange(26,28,0.1)
p8 = np.rint((peak8-3)*10).astype(int)
fit_peak8 = opt.curve_fit(gaussian, peak8, rate_good[p8], p0=[120, 26.5, 1, 80])[0]
a, b, c, d = fit_peak8
plt.plot(peak8, a * np.exp(-((peak8-b)/c)**2) + d, label="Fit of peak 8")
b = np.around(b,1)
print('Peak 8 occurs at ' + str(b) + ' degrees')


plt.legend(ncol=2)
plt.show()