# 2024 ML/AI Capstone Porject Datacard

## Motivation
Data was created as part of the Sloan Digital Sky Survey (SDSS). This is a collection of various systematic imaging programs over many years. The data was created and maintained by the Sloan Digital Sky Survey 
and this the data releases 17.

## Collection Process / Maintenance and Distribution
The data was collected using the SDSS imaging camera, detail here: https://www.sdss4.org/faceplat/. These data was collected as part of the various systemaic collection programs.
The data is maintained and distributed by the SDSS program, see SDSS Publications below.

## Composition

The data consists of 100,000 observations of space taken by the SDSS (Sloan Digital Sky Survey). Every observation is described by 17 feature columns and 1 class column which identifies it to be either a star, galaxy or quasar.

* obj_ID = Object Identifier, the unique value that identifies the object in the image catalog used by the CAS
* alpha = Right Ascension angle (at J2000 epoch)
* delta = Declination angle (at J2000 epoch)
* u = Ultraviolet filter in the photometric system
* g = Green filter in the photometric system
* r = Red filter in the photometric system
* i = Near Infrared filter in the photometric system
* z = Infrared filter in the photometric system
* run_ID = Run Number used to identify the specific scan
* rereun_ID = Rerun Number to specify how the image was processed
* cam_col = Camera column to identify the scanline within the run
* field_ID = Field number to identify each field
* spec_obj_ID = Unique ID used for optical spectroscopic objects (this means that 2 different observations with the same spec_obj_ID must share the output class)
* class = object class (galaxy, star or quasar object)
* redshift = redshift value based on the increase in wavelength
* plate = plate ID, identifies each plate in SDSS
* MJD = Modified Julian Date, used to indicate when a given piece of SDSS data was taken
* fiber_ID = fiber ID that identifies the fiber that pointed the light at the focal plane in each observation

## Uses

Data contains spectral data from various instruments on the imgaging camera and is suitable for astronomical research.


<b>Citation</b>
* fedesoriano. (January 2022). Stellar Classification Dataset - SDSS17. Retrieved from https://www.kaggle.com/fedesoriano/stellar-classification-dataset-sdss17.

* https://www.sdss4.org/faceplat/

<b>Acknowledgements</b>
The data released by the SDSS is under public domain. Its taken from the current data release RD17. More information about the license: http://www.sdss.org/science/image-gallery/

<b>SDSS Publications</b>

Abdurro’uf et al., The Seventeenth data release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 DATA (Abdurro’uf et al. submitted to ApJS) [arXiv:2112.02026]
