import numpy as np
from scipy.stats import ortho_group

def Tosz(x):
    """
    Function from the COCO benchmarks
    x is a numpy array
    :param x:
    :return:
    """
    i = 0
    xhat=[]
    c1=[]
    c2=[]
    signx =[]
    if np.size(x)==1:
        x = np.array([x])
    for xi in x:
        if xi==0:
            xhat.append(0)
            signx.append(0)
            c1.append(5.5)
            c2.append(3.1)
        if xi !=0:
            xhat.append(np.log(np.abs(xi)))
            if xi >0:
                signx.append(1)
                c1.append(10)
                c2.append(7.9)
            if xi<0:
                signx.append(-1)
                c1.append(5.5)
                c2.append(3.1)
        i = i+1
    signx = np.array(signx)
    xhat = np.array(xhat)
    c1 = np.array(c1)
    c2 = np.array(c2)
    z = signx*np.exp(xhat + 0.049*np.sin(c1*xhat) +np.sin(c2*xhat))
    return np.array(z)

def Tasy(x,beta):
    x=np.array(x)
    D = np.size(x)
    xret = np.zeros(D)
    j=0
    i=1
    for xi in x:
        if xi >0:
            xret[j]= np.power(xi, 1 + beta* (i-1)/(D-1) *np.sqrt(xi) )
        else:
            xret[j] = xi
        j=j+1
        i=i+1
    return xret

def DiagAlpha(alpha,D):
    i = np.arange(1, D+1)
    diag = np.power(alpha, 0.5* (i-1)/(D-1))
    m = np.diag(diag)
    return m

def zeroVec(D):
    return np.zeros(D)

def onesVec(D):
    return np.ones(D)

def fpen(x):
    x=np.array(x)
    D=np.size(x)
    return np.sum((np.maximum(np.zeros(D), np.abs(x)-5))**2)

def Iplusminus(D):
    return np.random.choice([-1.0, 1.0], p=[0.5, 0.5], size=D)

def QR(D):
    a=ortho_group.rvs(dim=D)
    return a, a.T
