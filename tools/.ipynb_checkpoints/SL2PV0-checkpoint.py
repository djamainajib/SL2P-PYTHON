import pickle

    
 # --------------------
 # Sentinel2 Functions: 
 # --------------------
def s2_createFeatureCollection_estimates():
    with open('nets/s2_sl2p_weiss_or_prosail_NNT3_Single_0_1.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_errors():
    with open('nets/s2_sl2p_weiss_or_prosail_NNT3_Single_0_1_error.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_domains():
    with open('nets/S2_SL2P_WEISS_ORIGINAL_DOMAIN.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_Network_Ind():
    with open('nets/Parameter_file_sl2p.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file


 # Same functions as above using 10 m bands:
    
def s2_10m_createFeatureCollection_estimates():
    with open('nets/s2_sl2p_weiss_or_prosail_10m_NNT1_Single_0_1.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_10m_createFeatureCollection_errors():
    with open('nets/s2_sl2p_weiss_or_prosail_10m_NNT1_Single_0_1_errors.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def  s2_10m_createFeatureCollection_domains():
    with open('nets/s2_sl2p_weiss_or_prosail_10m_domain.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_10m_createFeatureCollection_Network_Ind():
    with open('nets/Parameter_file_sl2p.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file    
    


 


