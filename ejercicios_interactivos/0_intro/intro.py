import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

pi = np.pi # Número pi

def valores(x_min,x_max,N = 100): # Devuelve un array equiespaciado linealmente
  return np.linspace(x_min,x_max,N)

def ejemplo_graficar(x,y): # Grafica funciones
  plt.figure(figsize = (10,10))
  plt.plot(x,y)
  plt.xlabel('x',fontsize = 12)
  plt.ylabel('y',fontsize = 12)
  plt.plot([0,0],[min(y),max(y)],'k-',lw = 1)
  plt.plot([min(x),max(x)],[0,0],'k-',lw = 1)
#   plt.yticks(np.arange(y_lim[0],y_lim[1],step_y))
#   plt.xticks(np.arange(min(x),max(x),step_x))
  plt.grid()
#   plt.legend(fontsize = 12)

def ejemplo_ecuaciones(): # Ejemplo de resolución de un sistema de ecuaciones lineales
  x,y = symbols('x y') # Defino las variables
  eq_1 = Eq(2*x - y - 1) # Primera ecuación
  eq_2 = Eq(x + y - 5)   # Segunda ecuación
  
  return solve((eq_1,eq_2),(x,y))