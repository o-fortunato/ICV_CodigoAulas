import math as m
import numpy as np

def derive(fnc):
    df = np.zeros(len(fnc)-4)
    A = np.array([[-50, 96, -72, 32, -6],
                 [-6, -20, 36, -12, 2],
                 [2, -16, 0, 16, -2],
                 [-2, 12, -36, 20, 6],
                 [6, -32, 72, -96, 50]])
    i = 0
    while i < len(df)-1:
        for j in range (0, 5):
            for k in range(0, 5):
                if i+k > len(fnc)-1:
                    break
                df[i] += (1/(m.factorial(4) * 0.1)) * A[j][k] * fnc[i+k]
            i += 1
            if i > len(df)-1:
                break
    return df

data = np.genfromtxt('../DadosVoo2.csv', delimiter=';', skip_header=1, invalid_raise=False)
data = data[:, :8]

u       = data[:,2]
w       = data[:,3]
q       = data[:,4]
theta   = data[:,5]

u = np.array(u)
w = np.array(w)
q = np.array(q)
theta = np.array(theta)

du = derive(u)
dw = derive(w)
dq = derive(q)
dtheta = derive(theta)