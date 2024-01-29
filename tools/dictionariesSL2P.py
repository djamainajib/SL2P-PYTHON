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
        "Cloudcover": 'CLOUDY_PIXEL_PERCENTAGE',
        "Watercover": 'WATER_PERCENTAGE',
        "sza": 'MEAN_SOLAR_ZENITH_ANGLE',
        "vza": 'MEAN_INCIDENCE_ZENITH_ANGLE_B8A',
        "saa": 'MEAN_SOLAR_AZIMUTH_ANGLE', 
        "vaa": 'MEAN_INCIDENCE_AZIMUTH_ANGLE_B8A',
        "VIS_OPTIONS": 'VIS_OPTIONS',
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
        "Cloudcover": 'CLOUDY_PIXEL_PERCENTAGE',
        "Watercover": 'WATER_PERCENTAGE',
        "sza": 'MEAN_SOLAR_ZENITH_ANGLE',
        "vza": 'MEAN_INCIDENCE_ZENITH_ANGLE_B8A',
        "saa": 'MEAN_SOLAR_AZIMUTH_ANGLE', 
        "vaa": 'MEAN_INCIDENCE_AZIMUTH_ANGLE_B8A',
        "VIS_OPTIONS": 'VIS_OPTIONS',
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
                "errorName": 'errorAlbedo',
                "maskName": 'maskAlbedo',
                "description": 'Black sky albedo',
                "variable": 6,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'Albedo',
                "errorName": 'errorAlbedo',
                "maskName": 'maskAlbedo',
                "description": 'Black sky albedo',
                "variable": 6,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
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
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'fAPAR',
                "errorName": 'errorfAPAR',
                "maskName": 'maskfAPAR',
                "description": 'Fraction of absorbed photosynthetically active radiation',
                "variable": 2,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
        'fCOVER': {
            "S2_SR": {
                "Name": 'fCOVER',
                "errorName": 'errorfCOVER',
                "maskName": 'maskfCOVER',
                "description": 'Fraction of canopy cover',
                "variable": 3,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'fCOVER',
                "errorName": 'errorfCOVER',
                "maskName": 'maskfCOVER',
                "description": 'Fraction of canopy cover',
                "variable": 3,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
        'LAI': {
            "S2_SR": {
                "Name": 'LAI',
                "errorName": 'errorLAI',
                "maskName": 'maskLAI',
                "description": 'Leaf area index',
                "variable": 1,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'LAI',
                "errorName": 'errorLAI',
                "maskName": 'maskLAI',
                "description": 'Leaf area index',
                "variable": 1,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
        'CCC': {
            "S2_SR": {
                "Name": 'CCC',
                "errorName": 'errorCCC',
                "maskName": 'maskCCC',
                "description": 'Canopy chlorophyll content',
                "variable": 4,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'CCC',
                "errorName": 'errorCCC',
                "maskName": 'maskCCC',
                "description": 'Canopy chlorophyll content',
                "variable": 4,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
        'CWC': {
            "S2_SR": {
                "Name": 'CWC',
                "errorName": 'errorCWC',
                "maskName": 'maskCWC',
                "description": 'Canopy water content',
                "variable": 5,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'CWC',
                "errorName": 'errorCWC',
                "maskName": 'maskCWC',
                "description": 'Canopy water content',
                "variable": 5,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        },
        'DASF': {
            "S2_SR": {
                "Name": 'DASF',
                "errorName": 'errorDASF',
                "maskName": 'maskDASF',
                "description": 'Directional area scattering factor',
                "variable": 7,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
            "S2_SR_10m": {
                "Name": 'DASF',
                "errorName": 'errorDASF',
                "maskName": 'maskDASF',
                "description": 'Directional area scattering factor',
                "variable": 7,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
            },
        }
    }
    return(NET_OPTIONS)


def make_outputParams():
    # output parameters
    outputParams = {
        'Albedo': {
            'outputScale': 1000,
            'outputOffset': 0,
            'outputMax': 0.2
        },
        'fAPAR': {
            'outputScale': 1000,
            'outputOffset': 0,
            'outputMax': 1
        },
        'fCOVER': {
            'outputScale': 1000,
            'outputOffset': 0,
            'outputMax': 1
        },
        'LAI': {
            'outputScale': 1000,
            'outputOffset': 0,
            'outputMax': 8
        },
        'CCC': {
            'outputScale': 1000,
            'outputOffset': 0,
            'outputMax': 6
        },
        'CWC': {
            'outputScale': 1000,
            'outputOffset': 0,
            'outputMax': 0.55
        },
        'DASF': {
            'outputScale': 1000,
            'outputOffset': 0,
            'outputMax': 1
        }
    }
    return(outputParams)