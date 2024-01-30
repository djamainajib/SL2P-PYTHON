from tools import toolsNets
from tools import dictionariesSL2P 
from tools import SL2PV0 
import numpy 
from datetime import datetime
from tools import read_sentinel2_safe_image

algorithm=SL2PV0 

def makeModel(algorithm,imageCollectionName,variableName):
    collectionOptions = (dictionariesSL2P.make_collection_options(algorithm))
    colOptions=collectionOptions[imageCollectionName]
    networkOptions= dictionariesSL2P.make_net_options()
    netOptions=networkOptions[variableName][imageCollectionName]

    ## Compute numNets
    numNets =len({k: v for k, v in (colOptions["Network_Ind"]['features'][0]['properties']).items() if k != 'Feature Index'})
    SL2P_net = [toolsNets.makeNetVars(colOptions["Collection_SL2P"],numNets,netNum) for  netNum in range(colOptions["numVariables"])][netOptions['variable']]
    errorsSL2P_net = [toolsNets.makeNetVars(colOptions["Collection_SL2Perrors"],numNets,netNum) for  netNum in range(colOptions["numVariables"])][netOptions['variable']]
    return SL2P_net,errorsSL2P_net

def prepare_sl2p_inp(s2,variableName,imageCollectionName):
    networkOptions= dictionariesSL2P.make_net_options()
    netOptions=networkOptions[variableName][imageCollectionName]
    
    # resample sun and view (sensor) angles
    print('Resample sun and view (sensor) angles')
    factor=s2['B03'].shape[0]/s2['SZA'].shape[0]
    s2['SZA']=read_sentinel2_safe_image.resample_image(s2['SZA'],factor,interpolation='bilinear')
    s2['SAA']=read_sentinel2_safe_image.resample_image(s2['SAA'],factor,interpolation='bilinear')
    s2['VZA']=read_sentinel2_safe_image.resample_image(s2['VZA'],factor,interpolation='bilinear')
    s2['VAA']=read_sentinel2_safe_image.resample_image(s2['VAA'],factor,interpolation='bilinear')
    #compute Relative Azimuth angle (RAA)
    s2['RAA']=numpy.absolute(s2['SAA']-s2['VAA'])
    
    # Scaling Surface Reflectance bands:/10000
    print('Scaling Sentinel-2 bands')
    for band in range(3,len(netOptions['inputBands'])):
        s2[netOptions['inputBands'][band]]=(s2[netOptions['inputBands'][band]]+netOptions['inputOffset'][band])*netOptions['inputScaling'][band]
    
    #compute cos(angles)
    print('Computing cosSZA, cosVZA and cosRAA')
    s2['cosSZA']=numpy.cos(numpy.deg2rad(s2['SZA']))
    s2['cosVZA']=numpy.cos(numpy.deg2rad(s2['VZA']))
    s2['cosRAA']=numpy.cos(numpy.deg2rad(s2['RAA']))
    
    # select  sl2p input bands
    print('Selecting sl2p input bands')
    
    sl2p_inp={}
    for band in netOptions['inputBands']:
        sl2p_inp.update({band:s2[band]})
        
    # prepare SL2P input data    
    sl2p_inp=numpy.stack([sl2p_inp[k] for k in sl2p_inp.keys()]) 
    print('Done!')
    return sl2p_inp   
        
def SL2P(sl2p_inp,variableName,imageCollectionName,outPath=None):
    networkOptions= dictionariesSL2P.make_net_options()
    collectionOptions = (dictionariesSL2P.make_collection_options(algorithm))
    netOptions=networkOptions[variableName][imageCollectionName]
    colOptions=collectionOptions[imageCollectionName]
    
    # prepare SL2P networks
    SL2P_net,errorsSL2P_net=makeModel(algorithm,imageCollectionName,variableName) 
    
    # generate sl2p input data flag
    inputs_flag=invalidInput(sl2p_inp,netOptions,colOptions)
       
    # run SL2P
    print('Run SL2P...\nSL2P start: %s' %(datetime.now()))
    estimate   =toolsNets.applyNet(sl2p_inp,SL2P_net)
    uncertainty=toolsNets.applyNet(sl2p_inp,errorsSL2P_net)
    print('SL2P end: %s' %(datetime.now()))
    
     # generate sl2p output product flag
    output_flag=invalidOutput(estimate,variableName)
    print('Done')
    return {variableName:estimate,variableName+'_uncertainty':uncertainty,'sl2p_inputFlag':inputs_flag,'sl2p_outputFlag':output_flag}

def invalidInput(image,netOptions,colOptions):
    print('Generating sl2p input data flag')
    [d0,d1,d2]=image.shape
    sl2pDomain=numpy.sort(numpy.array([row['properties']['DomainCode'] for row in colOptions["sl2pDomain"]['features']]))
    bandList={b:netOptions["inputBands"].index(b) for b in netOptions["inputBands"] if b.startswith('B')}
    image=image.reshape(image.shape[0],image.shape[1]*image.shape[2])[list(bandList.values()),:]
    
    #Image formatting
    image_format=numpy.sum((numpy.uint8(numpy.ceil(image*10)%10))* numpy.array([10**value for value in range(len(bandList))])[:,None],axis=0)
    
    # Comparing image to sl2pDomain
    flag=numpy.isin(image_format, sl2pDomain,invert=True)
    return flag.reshape(d1,d2)

def invalidOutput(estimate,variableName):
    print('Generating sl2p output product flag')
    var_range=dictionariesSL2P.make_outputParams()[variableName]
    return numpy.where(estimate<var_range['outputOffset'],1,numpy.where(estimate>var_range['outputMax'],2,0))
