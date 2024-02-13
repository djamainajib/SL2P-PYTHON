# Welcome to SL2P-PYTHON


SL2P-PYTHON is a python implementation of the Simplified Level 2 Product Prototype Processor (SL2P) described in [Weiss and Baret (2016)](https://step.esa.int/docs/extra/ATBD_S2ToolBox_L2B_V1.1.pdf). It corresponds to the algorithm implemented in the [LEAf-Toolbox](https://github.com/rfernand387/LEAF-Toolbox) that corrects for bugs in the implemention of SL2P within the European Space Agency Sentinel 2 Toolbox as documented in [Fernandes et al. 2023](https://www.sciencedirect.com/science/article/pii/S0034425723001517?via%3Dihub).

SL2P-PYTHON is designed to estimate vegetation biophysical variables (Table 1) at 10 or 20 meters spatial resolution from Sentinel-2 MSI L2A images. 

### Required inputs
---------------
-	[ESA SAFE format Sentinel-2 Level 2A product](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2/data-products)
-	The needed vegetation variable (Table 1)
-	The needed spatial resolution: S2_SR (for 20-m) / S2_SR_10m (for 10-m)

Outputs
-------
SL2P-PYTHON is designed to estimate five vegetation variables (Table 1). 
Products are composed of 4-layers and exported in GeoTIFF format (Table 2). 

<font size="8">Table 1: Vegetation variables supported by SL2P-PYTHON</font>

|Vegetation variable	|Description	|Unit	|Nominal variation range|
|---------------------|-------------|:-----:|:-----------------------:|
|LAI	|Half the total green foliage area per horizontal ground area.	|$m^{2} / m^{2}$ |0 - 8|
|fCOVER	|Fraction of nadir canopy cover	|Ratio	|0 – 1|
|fAPAR	|Fraction of absorbed clear sky PAR at 10:30 am local time	|Ratio	|0 – 1|
|CCC	|Canopy chlorophyll A+B content	|$g / m^{2}$	|0 - 600|
|CWC	|Canopy water content	|$g / m^{2}$	|0 – 1|
|Albedo	|Black sky shortwave albedo at 10:30am local time	|Ratio	|0 – 0.2|


<font size="8">Table 2: SL2P-PYTHON output layers (for one needed vegetation variable)</font>

|Layer                                         |	Description                                              |
|----------------------------------------------|-----------------------------------------------------------|
|Vegetation variable estimate	                 |Map of vegetation variable                                 | 
|Uncertainty of vegetation variable estimates	 |Map of the uncertainty of vegetation variable              |
|SL2P input flag (Quality Code)	               |0: Valid, 1: SL2P input out of SL2P calibration domain     |
|SL2P output flag (Quality Code)               |	0: Valid, 1: estimates out of the nominal variation range|





  
A [test dataset](https://drive.google.com/drive/folders/11BGcS0OA4EjGYb9XGfBtNPFpdgw10uWI?usp=drive_link) is provided for a quick test of SL2P_python as well as for comparison of outputs to the corresponding product obtained using the Sentinel Application Platform (SNAP) implementation of SL2P. 

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

![image](https://github.com/djamainajib/SL2P-PYTHON/assets/33295871/44a270ce-8804-4075-9e5b-e61bce6d97e6)

