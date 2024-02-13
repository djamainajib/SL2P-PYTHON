#from tools import toolsS2

def define_input_resolution():
    RESOLUTION_OPTIONS = {    
        'S2_SR': 20,       # Sentinel 2 using 20 m bands:
        'S2_SR_10m': 10    # Sentinel 2 using 10 m bands:
    }
    return(RESOLUTION_OPTIONS)
    
def make_collection_options(fc): 
    COLLECTION_OPTIONS = {
        # Sentinel 2 using 20 m bands:
        'S2_SR': {
        "name": 'S2_SR',
        "description": 'Sentinel 2A',
        "sza": 'MEAN_SOLAR_ZENITH_ANGLE',
        "vza": 'MEAN_INCIDENCE_ZENITH_ANGLE_B8A',
        "saa": 'MEAN_SOLAR_AZIMUTH_ANGLE', 
        "vaa": 'MEAN_INCIDENCE_AZIMUTH_ANGLE_B8A',
        "Collection_SL2P": fc.s2_createFeatureCollection_estimates(),   
        "Collection_SL2Perrors": fc.s2_createFeatureCollection_errors(),        
        "sl2pDomain": fc.s2_createFeatureCollection_domains(),   
        "Network_Ind": fc.s2_createFeatureCollection_Network_Ind(),      
        "numVariables": 7,
        "exportRes": 20,
        },
         # Sentinel 2 using 10 m bands:
        'S2_SR_10m': {
        "name": 'S2_SR_10m',
        "description": 'Sentinel 2A',
        "sza": 'MEAN_SOLAR_ZENITH_ANGLE',
        "vza": 'MEAN_INCIDENCE_ZENITH_ANGLE_B8A',
        "saa": 'MEAN_SOLAR_AZIMUTH_ANGLE', 
        "vaa": 'MEAN_INCIDENCE_AZIMUTH_ANGLE_B8A',
        "Collection_SL2P": fc.s2_10m_createFeatureCollection_estimates(),
        "Collection_SL2Perrors": fc.s2_10m_createFeatureCollection_errors(),  
        "sl2pDomain": fc.s2_10m_createFeatureCollection_domains(),
        "Network_Ind": fc.s2_10m_createFeatureCollection_Network_Ind(),
        "numVariables": 7,
        "exportRes": 10,
        },
    }
    return(COLLECTION_OPTIONS)


def make_net_options():
    NET_OPTIONS = {
        'Albedo': {
            "S2_SR": {
                "Name": 'Albedo',
                "description": 'Black sky albedo',
                "variable": 6,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'Albedo',
                "description": 'Black sky albedo',
                "variable": 6,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
        'fAPAR': {
            "S2_SR": {
                "Name": 'fAPAR',
                "errorName": 'errorfAPAR',
                "maskName": 'maskfAPAR',
                "description": 'Fraction of absorbed photosynthetically active radiation',
                "variable": 2,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'fAPAR',
                "description": 'Fraction of absorbed photosynthetically active radiation',
                "variable": 2,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
        'fCOVER': {
            "S2_SR": {
                "Name": 'fCOVER',
                "description": 'Fraction of canopy cover',
                "variable": 3,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'fCOVER',
                "description": 'Fraction of canopy cover',
                "variable": 3,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
        'LAI': {
            "S2_SR": {
                "Name": 'LAI',
                "description": 'Leaf area index',
                "variable": 1,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'LAI',
                "description": 'Leaf area index',
                "variable": 1,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
        'CCC': {
            "S2_SR": {
                "Name": 'CCC',
                "description": 'Canopy chlorophyll content',
                "variable": 4,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'CCC',
                "description": 'Canopy chlorophyll content',
                "variable": 4,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
        'CWC': {
            "S2_SR": {
                "Name": 'CWC',
                "description": 'Canopy water content',
                "variable": 5,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'CWC',
                "description": 'Canopy water content',
                "variable": 5,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [1, 1, 1, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [0, 0, 0,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
    }
    return(NET_OPTIONS)


def make_outputParams():
    # output parameters
    outputParams = {
        'Albedo': {
            'outputOffset': 0,
            'outputMax': 0.2
        },
        'fAPAR': {
            'outputOffset': 0,
            'outputMax': 1
        },
        'fCOVER': {
            'outputOffset': 0,
            'outputMax': 1
        },
        'LAI': {
            'outputOffset': 0,
            'outputMax': 8
        },
        'CCC': {
            'outputOffset': 0,
            'outputMax': 600
        },
        'CWC': {
            'outputOffset': 0,
            'outputMax': 0.55
        },
        'DASF': {
            'outputOffset': 0,
            'outputMax': 1
        }
    }
    return(outputParams)