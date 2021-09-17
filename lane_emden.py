import numpy as np

def integrate_LE(n,N=10000,dz=0.001,z_0=0.001):
    W_L = []
    z_L = []

    z = z_0; W = 1.0; f1 = 0.0
    for i in range(N):
        f1 += -(z**2)*(W**(n))*dz
        W += (f1/(z**2))*dz
        z += dz

        W_L.append(W);z_L.append(z)

    return z_L,W_L

def roots_LE(z_L,W_L):
    roots = []
    for i in range(len(z_L)-1):
        if(W_L[i+1].real>=0 and W_L[i].real<0):
            r = (z_L[i+1]+z_L[i])/2.
            roots.append(r)
        if(W_L[i+1].real<=0 and W_L[i].real>0):
            r = (z_L[i+1]+z_L[i])/2.
            roots.append(r)
    return roots

def analytic_LE(z,n):
    if(n==0):
        return 1-(1/6.)*(z**2)
    elif(n==1):
        return np.sin(z)/z
    elif(n==5):
        return 1/(np.sqrt(1+(z**2)/3.))
    else:
        print('No analytic solution for n={}'.format(n))