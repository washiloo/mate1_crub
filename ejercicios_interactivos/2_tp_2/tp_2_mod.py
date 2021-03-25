# --------------------------------------------
# Trabajo práctico 2: Relaciones y funciones
# --------------------------------------------
import matplotlib.pyplot as plt
from IPython import display
import numpy as np

display.set_matplotlib_formats('svg')

#---------------------------------------------------------------------------------------------------------------------
def graficar_funcion(x,y,step_x = None,step_y = None):
  plt.figure(figsize = (8,8))
  y_lim = [-1,1]
    
  if(type(y) == list):
    for i in range(len(y)):
      plt.plot(x,y[i],label = 'f_{}(x)'.format(i + 1))
      y_lim = [min(min(y[i]),y_lim[0]),max(max(y[i]),y_lim[1])]
  else:
    plt.plot(x,y,label = 'f(x)')
    y_lim = [min(y),max(y)]
    
  plt.xlabel('x',fontsize = 12)
  plt.ylabel('y',fontsize = 12)
  plt.axhline(0,color = 'k',lw = 2) # Agrego el eje x
  plt.axvline(0,color = 'k',lw = 2) # Agrego el eje y
  
  if(step_y):
    plt.yticks(np.arange(y_lim[0],y_lim[1],step_y))
  if(step_x):
    plt.xticks(np.arange(min(x),max(x),step_x))
  
  plt.grid()
  plt.legend(fontsize = 12)
#---------------------------------------------------------------------------------------------------------------------
def valores(x_min,x_max,N = 1000): # Devuelve una grilla de pares ordenados (x,y)
  return np.linspace(x_min,x_max,N) # Creo un conjunto de puntos equiespaciados
#---------------------------------------------------------------------------------------------------------------------
def pares_ordenados(x_lim = [0,1],y_lim = [0,1],N = 1000): # Devuelve una grilla de pares ordenados (x,y)
  return np.meshgrid(np.linspace(x_lim[0],x_lim[1],N),np.linspace(y_lim[0],y_lim[1],N)) # Creo una grilla de puntos
#---------------------------------------------------------------------------------------------------------------------
def def_region(x_lim,y_lim,cond):
  x,y = pares_ordenados(x_lim,y_lim) # Creo una grilla de puntos
  if(cond == 'nada'): # Chequeo si hay alguna condición
    r = np.ones(x.shape,dtype = bool) # Grafico todo
  else:
    r = eval(cond) # Defino la región a graficar usando expresiones lógicas

  return r,[x[r].min(),x[r].max()],[y[r].min(),y[r].max()]
#---------------------------------------------------------------------------------------------------------------------
def graficar_region(x,y,cond = 'nada',fronteras = None): # Grafica una región en el plano, dada su expresión por comprensión
  """
  Produce un gráfico en R^2 con la representación gráfica de la región del plano expresada por comprensión en los argumentos.

  Parámetros:

  x-tipo Valores: valores de la coordenada horizontal de los puntos que se incluirán en el gráfico
  y-tipo Valores: valores de la coordenada vertical de los puntos que se incluirán en el gráfico
  region-tipo String: Representa la expresión del conjunto a graficar, dada por comprensión.
  fronteras-tipo Lista: lista de objetos tipo 'frontera' creados con la función frontera().
  """
  region,x_lim,y_lim = def_region(x,y,cond)
    
  fig,ax = plt.subplots(1,figsize = (8,8))
  ax.imshow(region.astype(int),extent = (x[0],x[1],y[0],y[1]),origin = "lower",cmap = "Greys",alpha = 0.3)
  ax.axhline(0,color = 'k',lw = 2) # Agrego el eje x
  ax.axvline(0,color = 'k',lw = 2) # Agrego el eje y
  ax.set_xlabel('x',fontsize = 12)
  ax.set_ylabel('y',fontsize = 12)
  ax.grid(ls = '--')

  ax.set_ylim((y[0],y[1]))
  ax.set_xlim((x[0],x[1]))

  if(fronteras != None): # Grafico las fronteras (si se especificaron)
    for fr in fronteras: 
      if(fr['x'] == None):
        fr['x'] = x_lim
      elif(fr['y'] == None):
        fr['y'] = y_lim
        
      graficar_frontera(ax,**fr)
  plt.show()
#---------------------------------------------------------------------------------------------------------------------
def frontera(x = None,y = None,tipo = '-'):
  '''
  Devuelve un objeto de tipo frontera que representa una parte de la frontera de un conjunto dado. 
  
  x-tipo Variable: si es un String, representa la función x = g(y) que se evaluará sobre los valores de y para definir la frontera.
                   si es una lista con dos elementos, representa los límites de variación de la variable x
  y-tipo Variable: si es un String, representa la función y = f(x) que se evaluará sobre los valores de x para definir la frontera
                   si es una lista con dos elementos, representa los límites de variación de la variable y
  tipo-tipo String: puede tomar dos valores: (a) '-' (frontera incluida en el conjunto); (b) '--' (frontera no incluida en el conjunto)
  '''
  return {'x':x,'y':y,'ls':tipo}
#---------------------------------------------------------------------------------------------------------------------
def graficar_frontera(ax,x,y,ls):
  '''
  Grafica (una parte de) la frontera de un conjunto.
  
  ax-tipo Eje: eje del gráfico sobre el que se graficará la frontera
  frontera-tipo Frontera: objeto de tipo 'frontera' creado con la función frontera()
  '''    
  M = 100 # Número de puntos a graficar

  def fun(var,expr):
    try:
      k = float(eval(expr)) # Evalúo si la función es constante
      if(var == 'x'):
        return lambda x: np.zeros(M) + k # Si es una función constante
      elif(var == 'y'):
        return lambda y: np.zeros(M) + k # Si es una función constante
      else:
        print('Error, la variable debe llamarse x o y.')
    except:
      if(var == 'x'):
        return lambda x: eval(expr) # Si y es función de x
      elif(var == 'y'):
        return lambda y: eval(expr) # Si x es función de y
      else:
        print('Error, la variable debe llamarse x o y.')

  if(isinstance(x,str)):
    X = fun('y',x)(np.linspace(y[0],y[1],M))
  else:
    X = np.linspace(x[0],x[1],M)
  if(isinstance(y,str)):
    Y = fun('x',y)(np.linspace(x[0],x[1],M))
  else:
    Y = np.linspace(y[0],y[1],M)
    
  ax.plot(X,Y,ls = ls,lw = 2,color = 'r')
#---------------------------------------------------------------------------------------------------------------------