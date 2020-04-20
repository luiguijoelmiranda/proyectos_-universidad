import numpy as np
from math import exp
import scipy.constants as sc
from matplotlib import pyplot as plt

Nptos = 101
pc = 50
#nombramos matrices de campo magnetico
Hx = np.zeros((Nptos,Nptos), dtype = "float64")
Hxp = np.zeros((Nptos,Nptos), dtype = "float64")
Hy = np.zeros((Nptos,Nptos), dtype = "float64")
Hyp = np.zeros((Nptos,Nptos), dtype = "float64")
#nombramos constantes
dt = 0.13e-9
dx = 0.054
dy = dx
E0 = 1.0
Total = 100
#matrices de campo electtrico 
Ez= np.zeros((Nptos,Nptos), dtype = "float64")# matriz Ez 2D
Ezp= np.zeros((Nptos,Nptos), dtype = "float64")# matriz Ez 2D
for n in range(0, Total): # for para el tiempo 
    for i in range (1, (Nptos-1) ):#for para recorrer las matrices de campo magnetico
        for j in range (1, (Nptos-1) ):
            Hx[i,j] = Hx[i,j] - (dt/(sc.mu_0))*(((Ez[i,j-1] -Ez[i,j+1])/dy))
            Hy[i,j] = Hy[i,j] + (dt/(sc.mu_0))*(((Ez[i-1,j] -Ez[i+1,j])/dx))
    for i in range(0, (Nptos-1)):#for para recorrer mariz de campo electrico 
        for j in range(0, (Nptos-1)):
            Ez[i,j] = Ez[i,j] + (dt/(sc.epsilon_0))*(((Hy[i+1,j] - Hy[i-1,j])/dx)-((Hx[i,j+1] - Hx[i,j-1])/dy))
            
    Hyp = Hy             
    Hxp = Hx
    Ezp = Ez
    Ez[pc,pc] = E0*exp((-(n - 8.0)**2)/16.0)# pulso gausina
    #diferentes tipos de plotear
    x0 =(np.linspace(-50,50, num = Nptos))*dx
    y0 =(np.linspace(-20,20, num = Nptos))*dx
    plt.plot(x0,Ez[0,:])#plotear vector
    fig1 = plt.figure(1)#graficamos la matriz de potencial 
    #f1 = plt.contourf(Ezp, 10, cmap ='jet') # plotear figura 2D
    #plt.colorbar(f1) #Barra de color al lado de la gráfica
    plt.xlabel("X [m]") #nombre eje x
    plt.ylabel("Y [m]") #nombre eje plt.plot(x0,Hx[0,:])
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    