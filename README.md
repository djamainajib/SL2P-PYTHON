# Welcome to SL2P-PYTHON


SL2P-PYTHON is a python implementation of the Simplified Level 2 Product Prototype Processor (SL2P) described in [Weiss and Baret (2016)](https://step.esa.int/docs/extra/ATBD_S2ToolBox_L2B_V1.1.pdf). It corresponds to the algorithm implemented in the [LEAf-Toolbox](https://github.com/rfernand387/LEAF-Toolbox) that corrects for bugs in the implemention of SL2P within the European Space Agency Sentinel 2 Toolbox as documented in [Fernandes et al. 2023](https://www.sciencedirect.com/science/article/pii/S0034425723001517?via%3Dihub).

SL2P-PYTHON is designed to estimate vegetation biophysical variables (Table 1) at 10 or 20 meters spatial resolution from Sentinel-2 MSI L2A images. 

Required inputs
---------------
-	[Sentinel-2 MSI L2A product at ESA SAFE format](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjAxLzdlqmEAxUPAHkGHf0SBh8QFnoECA0QAw&url=https%3A%2F%2Fsentinels.copernicus.eu%2Fweb%2Fsentinel%2Ftechnical-guides%2Fsentinel-2-msi%2Flevel-2a%2Fproduct-formatting%23%3A~%3Atext%3DThe%2520Level%252D2A%2520product%2520has%2Ca%2520manifest.&usg=AOvVaw3l2OL2cIPi5idQJfHwqaRQ&opi=89978449)
-	The needed vegetation variable (Table 1)
-	The needed spatial resolution: S2_SR (for 20-m) / S2_SR_10m (for 10-m)

Outputs
-------
SL2P-PYTHON is designed to estimate five vegetation variables (Table 1). 

Products are composed of 4-layers and exported in GeoTIFF format (Table 2). 



<p align="center"> <font size="8">Table 1: Vegetation variables supported by SL2P-PYTHON</font> </p>

|Vegetation variable	|Description	|Unit	|Nominal variation range|
|---------------------|-------------|:-----:|:-----------------------:|
|LAI	|Half the total green foliage area per horizontal ground area.	|$m^{2} / m^{2}$ |0 - 8|
|fCOVER	|Fraction of nadir canopy cover	|Ratio	|0 – 1|
|fAPAR	|Fraction of absorbed clear sky PAR at 10:30 am local time	|Ratio	|0 – 1|
|CCC	|Canopy chlorophyll A+B content	|$g / m^{2}$	|0 - 600|
|CWC	|Canopy water content	|$g / m^{2}$	|0 – 1|
|Albedo	|Black sky shortwave albedo at 10:30am local time	|Ratio	|0 – 0.2|


<p align="center"> <font size="8">Table 2: SL2P-PYTHON output layers (for one needed vegetation variable)</font> </p>

|Layer                                         |	Description                                              |
|----------------------------------------------|-----------------------------------------------------------|
|Vegetation variable estimate	                 |Map of vegetation variable                                 | 
|Uncertainty of vegetation variable estimates	 |Map of the uncertainty of vegetation variable              |
|SL2P input flag (Quality Code)	               |0: Valid, 1: SL2P input out of SL2P calibration domain     |
|SL2P output flag (Quality Code)               |	0: Valid, 1: estimates out of the nominal variation range|

![image](https://github.com/djamainajib/SL2P-PYTHON/assets/33295871/2c42dc0b-2256-4147-860c-48eac8c04813)

<p align="center"> Figure 1: SL2P-PYTHON principles </p>

Test dataset
------------
A [test dataset](https://drive.google.com/drive/folders/11BGcS0OA4EjGYb9XGfBtNPFpdgw10uWI?usp=drive_link) is provided for a quick test of SL2P-PYTHON as well as for comparison with the corresponding product obtained using the Sentinel Application Platform (SNAP) implementation of SL2P. 

For more details about SL2P-PYTHON please see [ATBD document](https://github.com/djamainajib/SL2P_python/blob/main/GEOMATICS%20CANADA%20xx%20-%20SL2P%20PYTHON_version_0.docx).


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
See [CONTRIBUTING.md](https://github.com/djamainajib/SL2P_python/blob/main/CONTRIBUTING.md)


License:
------------
Unless otherwise noted, the source code of this project is covered under Crown Copyright, Government of Canada, and is distributed under the [MIT License](https://github.com/djamainajib/SL2P_python/blob/main/License).

The Canada wordmark and related graphics associated with this distribution are protected under trademark law and copyright law. No permission is granted to use them outside the parameters of the Government of Canada's corporate identity program. For more information, see [Federal identity requirements}9https://www.canada.ca/en/treasury-board-secretariat/topics/government-communications/federal-identity-requirements.html).


