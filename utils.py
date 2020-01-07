import numpy as np
from ConfigSpace.configuration_space import Configuration

NAN = np.float64(np.nan)

#helper functions
def isArray(x):
    if isinstance(x, np.ndarray):
        return True
    else:
        return False

def isListOrTuple(x):
    """
    Type List numpy array or tuples
    """
    if isinstance(x, list) or isinstance(x, tuple):
        return True
    else:
        return False

def listOrTupleToArray(x):
    return np.array(x)

def isDictionary(x):
    if isinstance(x, dict):
        return True
    else:
        return False


def dictToArray(x):
    xx = []
    for key, value in x.items():
        xx.append(value)
    return np.array(xx)

def isConfigurationSpace(x):
    if isinstance(x, Configuration):
        print
        return True
    else:
        return False

def configurationSpaceToArray(x):
    xx = []
    for xi in x:
        xx.append(x[xi])
    return np.array(xx)


def convertToArray(x):
    if isArray(x):
        return x
    elif isListOrTuple(x):
        return listOrTupleToArray(x)
    elif isDictionary(x):
        return dictToArray(x)
    elif isConfigurationSpace(x):
        return configurationSpaceToArray(x)
    else:
        raise ValueError('Wrong input error! Type ', str(type(x)), ' not supported.')