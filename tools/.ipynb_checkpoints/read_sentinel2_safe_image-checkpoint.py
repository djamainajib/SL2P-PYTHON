import numpy, os
import rasterio
from skimage.transform import resize
import xml.etree.ElementTree as ET
from tqdm import tqdm
import scipy.ndimage

def extract_sun_angles(xml):
    """Extract Sentinel-2 solar angle bands values from MTD_TL.xml.
    Parameters:
       xml (str): path to MTD_TL.xml.
    Returns:
       str, str: sz_path, sa_path: path to solar zenith image, path to solar azimuth image, respectively.
    """
    solar_zenith_values = numpy.empty((23,23,)) * numpy.nan #initiates matrix
    solar_azimuth_values = numpy.empty((23,23,)) * numpy.nan

    # Parse the XML file
    tree = ET.parse(xml)
    root = tree.getroot()

    # Find the angles
    for child in root:
        if child.tag[-14:] == 'Geometric_Info':
            geoinfo = child

    for segment in geoinfo:
        if segment.tag == 'Tile_Angles':
            angles = segment

    for angle in angles:
        if angle.tag == 'Sun_Angles_Grid':
            for bset in angle:
                if bset.tag == 'Zenith':
                    zenith = bset
                if bset.tag == 'Azimuth':
                    azimuth = bset
            for field in zenith:
                if field.tag == 'Values_List':
                    zvallist = field
            for field in azimuth:
                if field.tag == 'Values_List':
                    avallist = field
                
                if field.tag == 'COL_STEP':
                    colstep= float(field.text)   
                if field.tag == 'ROW_STEP':
                    rowstep= float(field.text)   
                    
            for rindex in range(len(zvallist)):
                zvalrow = zvallist[rindex]
                avalrow = avallist[rindex]
                zvalues = zvalrow.text.split(' ')
                avalues = avalrow.text.split(' ')
                values = list(zip(zvalues, avalues)) #row of values
                for cindex in range(len(values)):
                    if ( values[cindex][0] != 'NaN' and values[cindex][1] != 'NaN'):
                        zen = float(values[cindex][0])
                        az = float(values[cindex][1])
                        solar_zenith_values[rindex,cindex] = zen
                        solar_azimuth_values[rindex,cindex] = az
    solar_zenith_values = resize(solar_zenith_values,(22,22))
    solar_azimuth_values = resize(solar_azimuth_values,(22,22))
    return (solar_zenith_values, solar_azimuth_values,colstep,rowstep)

def extract_sensor_angles(xml):
    """Extract Sentinel-2 view (sensor) angle bands values from MTD_TL.xml.
    Parameters:
       xml (str): path to MTD_TL.xml.
    Returns:
       str, str: path to view (sensor) zenith image and path to view (sensor) azimuth image, respectively.
    """
    numband = 13
    sensor_zenith_values = numpy.empty((numband,23,23)) * numpy.nan #initiates matrix
    sensor_azimuth_values = numpy.empty((numband,23,23)) * numpy.nan

    # Parse the XML file
    tree = ET.parse(xml)
    root = tree.getroot()

    # Find the angles
    for child in root:
        if child.tag[-14:] == 'Geometric_Info':
            geoinfo = child

    for segment in geoinfo:
        if segment.tag == 'Tile_Angles':
            angles = segment

    for angle in angles:
        if angle.tag == 'Viewing_Incidence_Angles_Grids':
            bandId = int(angle.attrib['bandId'])
            for bset in angle:
                if bset.tag == 'Zenith':
                    zenith = bset
                if bset.tag == 'Azimuth':
                    azimuth = bset
            for field in zenith:
                if field.tag == 'Values_List':
                    zvallist = field
            for field in azimuth:
                if field.tag == 'Values_List':
                    avallist = field  
                if field.tag == 'COL_STEP':
                    colstep= float(field.text)
                if field.tag == 'ROW_STEP':
                    rowstep= float(field.text)    
                    
            for rindex in range(len(zvallist)):
                zvalrow = zvallist[rindex]
                avalrow = avallist[rindex]
                zvalues = zvalrow.text.split(' ')
                avalues = avalrow.text.split(' ')
                values = list(zip(zvalues, avalues )) #row of values
                for cindex in range(len(values)):
                    if (values[cindex][0] != 'NaN' and values[cindex][1] != 'NaN'):
                        zen = float(values[cindex][0])
                        az = float(values[cindex][1])
                        sensor_zenith_values[bandId, rindex,cindex] = zen
                        sensor_azimuth_values[bandId, rindex,cindex] = az
    sensor_zenith_values = resize(sensor_zenith_values[7],(22,22))
    sensor_azimuth_values = resize(sensor_azimuth_values[7],(22,22))
    return(sensor_zenith_values, sensor_azimuth_values,colstep,rowstep)

def extract_boa_add_offset_values(xml):
    # Parse the XML file
    tree = ET.parse(xml)
    root = tree.getroot()
    # Find the angles
    for child in root:
        if child.tag[-12:] == 'General_Info':
            general_info = child       
    for segment in general_info:
        if segment.tag == 'Product_Image_Characteristics':
            image_characteristics = segment
    for sub_segment in image_characteristics: 
        if sub_segment.tag == 'BOA_ADD_OFFSET_VALUES_LIST':  
            BOA_ADD_OFFSET={'band_%s'%(value.attrib ['band_id']):float(value.text) for value in sub_segment if value.tag[:14]=='BOA_ADD_OFFSET'} 
    return BOA_ADD_OFFSET

def extract_quantification_values(xml):
    # Parse the XML file
    tree = ET.parse(xml)
    root = tree.getroot()
    # Find the angles
    for child in root:
        if child.tag[-12:] == 'General_Info':
            general_info = child       
    for segment in general_info:
        if segment.tag == 'Product_Image_Characteristics':
            image_characteristics = segment
    for sub_segment in image_characteristics: 
        if sub_segment.tag == 'QUANTIFICATION_VALUES_LIST':
            QUANTIFICATION={value.tag:float(value.text) for value in sub_segment}
    return QUANTIFICATION


def resample_image(img,factor,interpolation='nearest'):
    if interpolation=='nearest':
        order=0
    elif interpolation=='bilinear':
        order=1
    elif interpolation=='cubic':
        order=2  
    else:
        raise ValueError("interpolation algorithm must be one of the following:  nearest, bilinear, cubic ")
    return scipy.ndimage.zoom(img, factor, order=order)

def read_s2(safe,res='20'):
    inpath=safe+'/GRANULE/'+os.listdir(safe+'/GRANULE/')[0]+'/IMG_DATA/R%sm/'%(str(res))
    MTD_TL=safe+'/GRANULE/%s/MTD_TL.xml'%(os.listdir(safe+'/GRANULE/')[0])
    MTD_MSIL2A=safe+'/MTD_MSIL2A.xml'
    
    boa_add_offset=extract_boa_add_offset_values(MTD_MSIL2A)
    qualification=extract_quantification_values(MTD_MSIL2A)
    
    s2={}
    print('Reading Sentinel-2 image')
    for fn in tqdm([os.path.join(inpath,f) for f in os.listdir(inpath) if f.endswith('.jp2')]): 
        with rasterio.open(fn) as src:
            s2.update({'profile':src.profile})
            s2.update({fn.split('_')[-2]:(src.read(1)+boa_add_offset['band_%s'%(0)])/qualification['BOA_QUANTIFICATION_VALUE']})  #change 0 by the correspending band id 
    #add geometry of acquisition
    (SZA, SAA, colstep,rowstep)=extract_sun_angles(MTD_TL)
    (VZA, VAA, colstep,rowstep)=extract_sensor_angles(MTD_TL)
    s2.update({'SZA':SZA,'SAA':SAA,'VZA':VZA,'VAA':VAA})
    s2['profile'].update({'count':len(s2)-1})
    return s2