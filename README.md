# Xray_Diffraction
The code and original data for the x-ray diffraction experiment.

**Note:** when running the data and python scripts should be in the same folder, otherwise the python scripts should be altered to accommodate the folders in which they and the data are placed.

plotting_code contains the code used to plot the data and fit the peaks to Gaussian curves. The files are labelled with the specific crystal they were used to plot the data from and their specific function beyond that:
- Any file with a name ending in _1.py or _2.py was used to plot the initial 4-8 scans used to determine the optimum angle at which to find the diffraction pattern.
- Files with names ending in _good.py were used to plot only the data from the high resolution scan.
= Files with names ending in _filtered.py were used to plot only the data from the high resolution filtered scan.
- Files with names ending in _good_filtered.py were used to plot the data from the high resolution scan, both the filtered and unfiltered versions. These files were also used for all crystals except GaPI(111) to fit Gaussian curves to the peaks and find the angles at which they occurred.
- data_plotting_gap_good_again.py was used to plot the second high resolution scan of the GaP(111) crystal.
- data_plotting_gap_limited_angles.py was used to plot the high resolution scans of GaP(111) over limited angle ranges.
- data_plotting_gap_fitting.py was used to fit Gaussian curves to the peaks and find the angles at which they occurred for GaP(111).

data shows the original data for the experiment. The files are labelled with the specific crystal they contain the data from and the specific dataset beyond that:
- Any file with a name ending in _1.txt or _2.txt is the original data for the initial 4-8 scans used to determine the optimum angle at which to find the diffraction pattern.
- Files with names ending in _good.txt are the the data from the high resolution scan.
= Files with names ending in _filtered.txt are the the data from the high resolution filtered scan.
- gap_data_good_again.txt is the data from the second high resolution scan of the GaP(111) crystal.
- gap_data_limited_angles_good.txt is the data from the high resolution unfiltered scans of GaP(111) over limited angle ranges.
- gap_data_limited_angles_filtered.txt is the data from the high resolution filtered scans of GaP(111) over limited angle ranges.
