from tools import toolsNets
import numpy as np


# parse CSV file with list of networks for a selected variable (one network for each landclass partition)
def makeNetVars(asset, numNets, variableNum): 
    # get selected network 
    filtered_features =[asset['features'][variableNum]]  # check with Richard (numNets?????????????????????)
    for netNum in range(numNets):
        netVars =makeNets(filtered_features, netNum)
    return netVars

# read coefficients of a network from csv EE asset
def getCoefs(netData, ind):
    return netData['properties']['tabledata%s'%(ind)]

def makeNets(feature, M):
    # get the requested network and initialize the created network
    netData = feature[M]
    net = {}
    
    # input slope
    num = 6
    start = num+1
    end = num+netData['properties']['tabledata%s'%(num)]
    net["inpSlope"] = [getCoefs(netData,ind) for ind in range(start,end+1)] 
    
    #input offset
    num = end+1
    start = num+1
    end = num+netData['properties']['tabledata%s'%(num)]
    net["inpOffset"] = [getCoefs(netData,ind) for ind in range(start,end+1)] 
    
    # hidden layer 1 weight
    num = end+1
    start = num+1
    end = num+netData['properties']['tabledata%s'%(num)]
    net["h1wt"] = [getCoefs(netData,ind) for ind in range(start,end+1)] 

    # hidden layer 1 bias
    num = end+1
    start = num+1
    end = num+netData['properties']['tabledata%s'%(num)]
    net["h1bi"] = [getCoefs(netData,ind) for ind in range(start,end+1)] 

    # hidden layer 2 weight
    num = end+1
    start = num+1
    end = num+netData['properties']['tabledata%s'%(num)]
    net["h2wt"] = [getCoefs(netData,ind) for ind in range(start,end+1)] 
  
    # hidden layer 2 bias
    num = end+1
    start = num+1
    end = num+netData['properties']['tabledata%s'%(num)]
    net["h2bi"] = [getCoefs(netData,ind) for ind in range(start,end+1)] 

    # output slope
    num = end+1
    start = num+1
    end = num+netData['properties']['tabledata%s'%(num)]
    net["outSlope"] = [getCoefs(netData,ind) for ind in range(start,end+1)] 
  
    # output offset
    num = end+1
    start = num+1
    end = num+netData['properties']['tabledata%s'%(num)]
    net["outBias"] = [getCoefs(netData,ind) for ind in range(start,end+1)] 
    return [net]

def applyNet(inp,net):
    [d0,d1,d2]=inp.shape
    inp=inp.reshape(d0,d1*d2)
    inpSlope   =np.array(net[0]['inpSlope'])
    inpOffset  =np.array(net[0]['inpOffset'])
    h1wt       =np.array(net[0]['h1wt'])
    h2wt       =np.array(net[0]['h2wt'])
    h1bi       =np.array(net[0]['h1bi'])
    h2bi       =np.array(net[0]['h2bi']) 
    outBias    =np.array(net[0]['outBias'])
    outSlope   =np.array(net[0]['outSlope']) 
    
    # input scaling
    l1inp2D=(inp*inpSlope[:,None])+inpOffset[:,None]

    # hidden layers
    l12D=np.matmul(np.reshape(h1wt,[len(h1bi),len(inpOffset)]),l1inp2D)+h1bi[:,None]

    # apply tansig 2/(1+exp(-2*n))-1
    l2inp2D=2/(1+np.exp(-2*l12D))-1
     
    # purlin hidden layers
    l22D = np.sum(l2inp2D*h2wt[:,None],axis=0)+h2bi

    # output scaling 
    outputBand = (l22D-outBias[:,None])/outSlope[:,None]
    
    outputBand=outputBand.reshape(d1,d2)
    return outputBand

