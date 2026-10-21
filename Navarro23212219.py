#Librerías

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd

#Datos Generales de la Simulacion

u = np.array(pd.read_excel('signal.xlsx', header=None))
x0,t0,tend,dt,w,h = 0,0,15,1e-3,10,5
N = round((tend-t0)/dt) + 1
t = np.linspace(t0,tend,N)
u = np.reshape(signal.resample(u,len(t)),-1)

#Componentes Circuito RLC
def cardiovascular(Z,R,L,C):
    num = [L*R, R*Z]
    den = [C*L*R*Z, L*R+L*Z, Z*R]
    sys = ctrl.tf(num,den)
    L = np.roots(den)
    return sys,L

#Funcion de transferencia hipotenso
Z,R,L,C = 0.01,1.000, 0.001, 3.500
sishipo,L = cardiovascular(Z,R,L,C)
print(f"Función de transferencia del sistema hipotenso (caso 1): {sishipo}")
print(f"Polos del sistema hipotenso: L1= {L[0]:.3e}, L2= {L[1]:.3e}\n")

#Funcion de transferencia normotenso
Z,R,L,C = 0.01,1.00, 0.001, 1.500
sisnormo,L = cardiovascular(Z,R,L,C)
print(f"Función de transferencia del sistema normotenso (control1): {sisnormo}")
print(f"Polos del sistema normotenso: L1= {L[0]:.3e}, L2= {L[1]:.3e}\n")

#Funcion de transferencia hipertenso
Z,R,L,C = 0.010, 1.00 , 0.001, 1.000
sishiper,L = cardiovascular(Z,R,L,C)
print(f"Función de transferencia del sistema hipertenso (caso 3): {sishiper}")
print(f"Polos del sistema hipertenso: L1= {L[0]:.3e}, L2= {L[1]:.3e}\n")

#Respuestas en lazo abierto
_,PpN=ctrl.forced_response(sisnormo,t,u,x0)
_,PpL=ctrl.forced_response(sishipo,t,PpN,x0)
_,PpH=ctrl.forced_response(sishiper,t,PpN,x0)

clr1 = np.array([46, 41, 16])/255
clr2 = np.array([44, 87, 69])/255
clr3 = np.array([235, 125, 0])/255

#Componentes del controlador
def controlador(kP,kI,kD,sys):
    Cr = 1e-6
    Re = 1/(kI*Cr)
    Rr = kP*Re
    Ce = kD/Rr
    numPID = [Re*Rr*Ce*Cr, (Re*Ce + Rr*Cr), 1]
    denPID = [Re*Cr, 0]
    PID = ctrl.tf(numPID, denPID)
    sysPID = ctrl.feedback(ctrl.series(PID, sys), 1, sign=-1)
    return sysPID


hipoPID = controlador(458.483, 1118300.387, 0.00627, sishipo)
print(f"Función de transferencia del hipotenso en lazo cerrdado: {hipoPID}")
hiperPID = controlador(126.595,293327.703,0.00140, sishiper)
print(f"Función de transferencia del hipertenso en lazo cerrdado: {hiperPID}")


fg1= plt.figure()
plt.plot(t,PpL, ("-"), linewidth=0.5, color=clr1, label="Pp(t): Hipotenso")
plt.plot(t,PpN, ("-"), linewidth=0.5, color=clr2, label="Pp(t): Normotenso")
plt.plot(t,PpH, ("-"), linewidth=0.5, color=clr3, label="Pp(t): Hipertenso")
plt.grid(False)
plt.title("Respuesta del sistema en lazo abierto")
plt.xlim(0, 15); plt.xticks(np.arange(0, 16, 1))
plt.ylim(-0.4,1.2); plt.yticks(np.arange(-0.4, 1.4, 0.2))
plt.xlabel("t [s]")
plt.ylabel('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5, -0.2), loc="center", ncol=3)
fg1.set_size_inches(w,h)
fg1.tight_layout()
fg1.savefig('Individuos_python.pdf')
plt.show()


_,PIDL = ctrl.forced_response(hipoPID,t,PpN,x0)
_,PIDH = ctrl.forced_response(hiperPID,t,PpN,x0)

fg2= plt.figure()
plt.plot(t,PpL, ("-"), linewidth=0.5, color=clr1, label="Pp(t): Hipotenso")
plt.plot(t,PpN, ("-"), linewidth=0.5, color=clr2, label="Pp(t): Normotenso")
plt.plot(t,PIDL, ("-."), linewidth=1.2, color=clr3, label="PID(t): Hipotenso")
plt.grid(False)
plt.xlim(0, 15); plt.xticks(np.arange(0, 16, 1))
plt.ylim(-0.4,1.2); plt.yticks(np.arange(-0.4, 1.4, 0.2))
plt.xlabel("t [s]")
plt.ylabel('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5,-0.2), loc="center", ncol=3)
fg2.set_size_inches(w,h)
fg2.tight_layout()
fg2.savefig('hipotenso_python.pdf')
plt.show()

fg3= plt.figure()
plt.plot(t,PpH, ("-"), linewidth=0.5, color=clr1, label="Pp(t): Hipertenso")
plt.plot(t,PpN, ("-"), linewidth=0.5, color=clr2, label="Pp(t): Normotenso")
plt.plot(t,PIDH, ("-."), linewidth=1.2, color=clr3, label="PID(t): Hipertenso")
plt.grid(False)
plt.xlim(0, 15); plt.xticks(np.arange(0, 16, 1))
plt.ylim(-0.4,1.4); plt.yticks(np.arange(-0.4, 1.4, 0.2))
plt.xlabel("t [s]")
plt.ylabel('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5,-0.2), loc="center", ncol=3)
fg3.set_size_inches(w,h)
fg3.tight_layout()
fg3.savefig('Hipertenso_python.pdf')
plt.show()