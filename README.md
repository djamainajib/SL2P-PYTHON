SL2P_python is a python implementation of the Simplified Level 2 Product Prototype Processor (SL2P) in [Weiss and Baret (2016)](https://step.esa.int/docs/extra/ATBD_S2ToolBox_L2B_V1.1.pdf) This implementation corresponds to the algorithm implemented in the [LEAf-Toolbox](https://github.com/rfernand387/LEAF-Toolbox) that corrects for bugs in the implemention of SL2P within the European Space Agency Sentinel 2 Toolbox as documented in [Fernandes et al. 2023](https://www.sciencedirect.com/science/article/pii/S0034425723001517?via%3Dihub).


SL2P is designed to estimate vegetation biophysical variables from Sentinel-2 (S2) MSI L2A multi-spectral images: leaf area index (LAI), fraction canopy cover (FCOVER), fraction of absorbed photosynthetically active radiation (FAPAR), canopy chlorophyll content (CCC) and canopy water content (CWC), in addition to the Albedo and the directional area scattering factor (DASF) not considered in the original SL2P version. 

SL2P fCOVER, fAPAR and LAI has been validated using in-situ fiducial reference measurements ([Djamai et al., 2018](https://www.sciencedirect.com/science/article/pii/S0034425719301117?via%3Dihub); [Brown et al., 2021](https://www.sciencedirect.com/science/article/pii/S0924271621000617); [Fernandes et al. 2023](https://www.sciencedirect.com/science/article/pii/S0034425723001517?via%3Dihub)).  Product users should account for documented uncertainty and may wish to apply documented bias corrections.


The user must specify:
-	the location of S2 to be used (locally saved).
-	the spatial resolution of used data: S2_SR (20-m) or S2_SR_10m (10-m}.
-	the needed vegetation variable: LAI, fAPAR, fCOVER, CCC, CWC, Albedo, or DASF,

The provided solution read the S2 image (SAFE format), prepare the SL2P input data (including data re-sampling, data scaling …) run SL2P, and export products in GeoTIFF product.
The outputted product contains: 

-	Estimates of the selected vegetation variable in [geophysical units](https://github.com/rfernand387/LEAF-Toolbox/wiki/Visualisation-Outputs),
  
-	the uncertainty of estimates in  [geophysical units](https://github.com/rfernand387/LEAF-Toolbox/wiki/Visualisation-Outputs),
  
-	SL2P inputs flag map where a value of 0 indicates valid inputs,
  
-	SL2P outputs flag map where a value of 0 indicates valid outputs.
  

A test dataset (https://drive.google.com/drive/folders/11BGcS0OA4EjGYb9XGfBtNPFpdgw10uWI?usp=drive_link) is provided for a quick test of SL2P_python as well as for comparison of outputs to the corresponding product obtained using the original SL2P version implemented on the Sentinel Application Platform (SNAP). 

Dependencies:
------------
- rasterio 1.3.9
- matplotlib 3.7.2
- datetime 5.4
- skimage 0.20.0
- tqdm 4.65.0
- scipy 1.11.1
- pickle 0.0.12

How to contribute?
------------
See CONTRIBUTING.md

License:
------------
Unless otherwise noted, the source code of this project is covered under Crown Copyright, Government of Canada, and is distributed under the MIT License.

The Canada wordmark and related graphics associated with this distribution are protected under trademark law and copyright law. No permission is granted to use them outside the parameters of the Government of Canada's corporate identity program. For more information, see Federal identity requirements.
