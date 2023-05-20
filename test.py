import matplotlib.pyplot as plt
import numpy as np
from math import *

Ka = 0.3
Ko = 0.1
Kv = 0.1
vr = 14
theta = -pi/180*45 #en radian
v0 = 10
m= 200


def vitesse(lv, invdt):
    vx = lv[0]
    vy = lv[1]
    ax = (sqrt(2)/4*Ka*((vy-vr)**2+vx**2)-Ko*vx*(sqrt(vx**2+vy**2)))/m
    ay = (sqrt(2)/4*Ka*((vy-vr)**2+vx**2)-Ko*vy*(sqrt(vx**2+vy**2))+Kv*(vr-vy)**2)/m
    lv[0]+= ax/invdt
    lv[1]+= ay/invdt
    
    return lv

def position(lp, invdt, lv):
    x = lp[0]+lv[0]/invdt
    y = lp[1]+lv[1]/invdt
    print(lv[0])
    return [x, y]

def liste_vit(t, invdt):
    v = []
    vx = []
    vy = []
    vx.append(cos(theta)*v0)
    vy.append(sin(theta)*v0)   

    for i in range(0, t*invdt-1):
        v = vitesse([vx[i], vy[i]], invdt)
        vx.append(v[0])
        vy.append(v[1])
    return [vx, vy]

def liste_pos(t, invdt, lv):
    x = []
    y = []
    x.append(0)
    y.append(0)
    for i in range(0, t*invdt-1):
        p = position([x[i], y[i]], invdt, [lv[0][i], lv[1][i]])
        x.append(p[0])
        y.append(p[1])
    return [x, y]

# On fera varier le temps entre t0 et tmax
temps =np.linspace ( 0, 100, 10000 ) # On pourra adapter le nombre de points.


plt.legend()
# Tracé de la courbe
"""
plt.subplot(311)
plt.grid (True)
plt.ylabel ("Vx")
plt.plot (temps, np.array(liste_vit(100, 100)[0]), label='Vx')
plt.subplot(312)
plt.grid (True)
plt.ylabel ("Vy")
plt.plot (temps, np.array(liste_vit(100, 100)[1]), label='vy')
plt.subplot(313)
"""
pos = np.array(liste_pos(100, 100, liste_vit(100, 100)))
plt.plot(pos[0], pos[1], label='trajectoire')


plt.xlabel ("x")
plt.ylabel ("y")
plt.grid (True)
plt.show ()