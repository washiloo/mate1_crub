# --------------------------------------------
# Operaciones entre conjuntos
# --------------------------------------------
from sympy import FiniteSet

def conjunto(*args): # Devuelve un conjunto definido por extensión con los elementos dados en el argumento, separados por comas
  """
  Devuelve un conjunto definido por extensión con los elementos dados en el argumento, separados por comas

  Parámetros:

  *args-tipo variable: Representa el conjunto de elemntos separados por coma que se usarán para crear el conjunto.
  """
  return set(args)

def cardinalidad(A): # Devuelve la cardinalidad de un conjunto
  """
  Devuelve un entero que representa el cardinal del conjunto

  Parámetros:

  A-tipo Set: Es el conjunto cuyo cardinal se desea averiguar
  """
  return len(A)

def pertenece(x,A): # Devuelve True si el elemento x pertenece al conjunto A, False de lo contrario
  """
  Permite saber si un determinado elemento pertenece o no a un conjunto en particular.

  Parámetros:

  x-tipo variable: Representa el elemento que se desea averiguar si forma o no parte de un conjunto.
  A-tipo Set: Es el conjunto en el cual se revisará si el objeto pasado como parámetro pertenece o no.

  Retorno:

  Retorna True en caso que el elemento x pertenezca al conjunto A. En caso contrario, retorna False.
  """
  return x in A

def subconjunto(A,B): # Devuelve True si A es subconjunto de B, False de lo contrario
  """
  Permite determinar si el conjunto A es subconjunto del conjunto B o no

  Parámetros:

  A-tipo Set: Es el conjunto para el cual se desea saber si es subconjunto del conjunto B
  B-tipo Set: Es el conjunto usado para saber si el conjunto A es subconjunto suyo o no.

  Retorno:

  Retorna True si el conjunto A está incluido o es igual al conjunto B. Caso contrario, retorna False.
  """
  return A.issubset(B)

def complemento(A,U): # Devuelve el complemento de A, dado el universal U
  """
  Devuelve el complemento de un conjunto

  Parámetros:

  A-tipo Set: conjunto cuyo complemento se desea obtener
  U-tipo Set: conjunto universal

  Retorno:

  Retorna un conjunto que representa complemento del conjunto A, dado el conjunto universal U
  """
  return U - A

def union(A,B): # Devuelve la unión de A y B
  """
  Permite obtener por extensión el conjunto resultante de la unión entre los conjuntos A y B.

  Parámetros:

  A-tipo Set: El primer conjunto de la operación
  B-tipo Set: El segundo conjunto de la operación

  Retorno:

  Retorna un conjunto que representa el resultado de la unión entre A y B
  """
  return A.union(B)

def interseccion(A,B): # Devuelve la intersección de A y B
  """
  Permite obtener por extensión el conjunto resultante de la intersección entre los conjuntos A y B.

  Parámetros:

  A-tipo Set: El primer conjunto de la operación
  B-tipo Set: El segundo conjunto de la operación

  Retorno:

  Retorna un conjunto que representa el resultado de la intersección entre A y B
  """
  return A.intersection(B)

def producto_cartesiano(A,B): # Devuelve un conjunto con los elementos del producto cartesiano de A y B
  """
  Permite obtener por extensión el conjunto resultante del producto cartesiano entre los conjuntos A y B.

  Parámetros:

  A-tipo Set: El primer conjunto de la operación
  B-tipo Set: El segundo conjunto de la operación

  Retorno:

  Retorna un conjunto que representa el resultado del producto cartesiano entre A y B como un conjunto de pares ordenados
  """
  return set([i for i in FiniteSet(*A) * FiniteSet(*B)])

def diferencia_simetrica(A,B):
  """
  Permite obtener por extensión el conjunto resultante de la diferencia simétrica entre los conjuntos A y B.

  Parámetros:

  A-tipo Set: El primer conjunto de la operación
  B-tipo Set: El segundo conjunto de la operación

  Retorno:

  Retorna un conjunto que representa el resultado de la diferencia simétrica entre A y B
  """
  return A.symmetric_difference(B)

# --------------------------------------------
# Diagramas de Venn
# https://pypi.org/project/matplotlib-venn/
# --------------------------------------------

import matplotlib.pyplot as plt
from matplotlib_venn import venn3,venn2_circles,venn3_circles

def venn_line(v,position,color = 'black',ls = '-',lw = 2):
  """
  Grafica una línea sobre un diagrama de Venn, en la posición indicada

  Parámetros:

  v-tipo VennDiagram: diagrama de Venn
  position-tipo String: posición de la línea ('10','11','01')
  color-tipo String: color de la línea. Por defecto es 'black'
  ls-tipo String: tipo de línea. Por defecto es '-'
  lw-tipo Int: ancho de la línea. Por defecto es 2.
  """    
  v.get_patch_by_id(position).set_edgecolor(color) # Asigno el color
  v.get_patch_by_id(position).set_linestyle(ls) # Asigno el tipo de línea
  v.get_patch_by_id(position).set_linewidth(lw) # Asigno el ancho de la línea

def venn(A,B,U,nombre1 = 'A',nombre2 = 'B',fs = 12):
  """
  Grafica y devuelve un diagrama de Venn con el conjunto universal U y los conjuntos A y B

  Parámetros:

  A-tipo Conjunto: el primer conjunto a graficar
  B-tipo Conjunto: el segundo conjunto a graficar
  U-tipo Conjunto: conjunto universal
  nombre1-tipo String: nombre del primer conjunto
  nombre2-tipo String: nombre del segundo conjunto
  fs-tipo Int: tamaño de la fuente
  """
  if(A == B): # Chequeo si los dos conjuntos son iguales
    nombre2 = ''
  
  fig = plt.figure(figsize = (10,10),linewidth=10, edgecolor="black", facecolor="white"); # Creo la figura
  ax = fig.add_subplot(111);
  plt.text(1,1,'U',ha ='right',va = 'top',transform = ax.transAxes,fontsize = fs); # Agrego el label 'U'
  v = venn3([A,B,U - A - B], (nombre1,nombre2,'')) # Creo el diagrama de Venn

  if((A - B) != set()): # Agrego los elementos de la región A - B
    v.get_label_by_id('100').set_text(A - B)
    venn_line(v,'100') # Agrego un contorno


  if(interseccion(A,B) != set()): # Agrego los elementos de la región A&B
    v.get_label_by_id('110').set_text(A&B)
    venn_line(v,'110') # Agrego un contorno

  if((B - A) != set()): # Agrego los elementos de la región B - A
    v.get_label_by_id('010').set_text(B - A)  
    venn_line(v,'010') # Agrego un contorno
    
  if((U - A - B) != set()): # Agrego los elementos de la región U - A - B
    v.get_label_by_id('001').set_text(U - A - B)  
    
  v.get_patch_by_id('001').set_color('white') # Hago transparente el fondo del universo
    
  set_fontsize(v,fs)

  return v

def graficar_interseccion(A,B,nombre1='A',nombre2='B'):
  """
  Grafica la intersección entre dos conjuntos y muestra los datos de la operación

  Parámetros:

  A-tipo Conjunto: Es el primer conjunto para la operación.
  B-tipo Conjunto: Es el segundo conjunto para la operación.
  nombre1-tipo String: Nombre del primer conjunto. Por defecto es 'A'
  nombre2-tipo String: Nombre del segundo conjunto. Por defecto es 'B'
  """
  operacion=nombre1 +" ∩ "+ nombre2
  resultado=interseccion(A,B)

  plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
  
  if cardinalidad(A)==0 and cardinalidad(B)==0:
    C={1,2,3,4,5,6,7}
    v = venn2(subsets = [C,C],set_labels = (operacion,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [C,C],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(chr(216))
    v.get_label_by_id('10').set_visible(False)
    v.get_patch_by_id('10').set_color('green')
    v.get_patch_by_id('11').set_color('green')
  elif cardinalidad(A)==0:
    v = venn2(subsets = [B,B],set_labels = (operacion,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [B,B],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(resultado)
  elif cardinalidad(B)==0:
    v = venn2(subsets = [A,A],set_labels = (operacion,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,A],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(resultado)
  elif cardinalidad(resultado)==0:
    v = venn2(subsets = [A,B],set_labels = (etiqueta1,etiqueta2)) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B])
    v.get_label_by_id('01').set_text(B)
    v.get_label_by_id('10').set_text(A)
  else:
    v = venn2(subsets = [A,B],set_labels = (etiqueta1,etiqueta2)) # Creo los dos conjuntos
    v.get_label_by_id('10').set_visible(False)
    v.get_label_by_id('11').set_text(resultado)
    v.get_label_by_id('01').set_visible(False)
    v.get_patch_by_id('10').set_color('white')
    v.get_patch_by_id('01').set_color('white')
    v.get_label_by_id('10').set_color('black')
    v.get_label_by_id('01').set_color('black')
    c = venn2_circles(subsets = [A,B])
    c[0].set_ls('solid')
    c[1].set_ls('solid')

  tablaResultados(A,B,operacion,resultado,etiqueta1,etiqueta2)
  plt.show()

def graficar_union(conj1,conj2,etiqueta1="A",etiqueta2="B"):
  """
  Permite graficar la unión de ambos conjuntos y muestra los datos de la operación

  Parámetros:

  conj1-tipo Set : Es el primer conjunto para la operación. Este conjunto ya ha sido formateado para su uso.
  conj2-tipo Set : Es el segundo conjunto para la opeación. Este conjunto ya ha sido formateado para su uso.
  etiqueta1-tipo String: Es la etiqueta para el primer conjunto. Por defecto se etiqueta como 'A'
  etiqueta2-tipo String: Es la etiqueta para el segundo conjunto. Por defecto se etiqueta como 'B'
  """
  A = conj1 # Convierto el conjunto al objeto de sympy para graficar
  B = conj2 # Convierto el conjunto al objeto de sympy para graficar
  carA=cardinalidad(A)
  carB=cardinalidad(B)
  operacion=etiqueta1 + " U " + etiqueta2
  resultado=union(A,B)
  lista=resultado #sirve para crear el diagrama y adaptarlo en caso de que el resultado sea vacio
  elementos=resultado #sirve para mostrar los elementos resultabtes de la operacion y adaptarla en caso que sea vacío
  if cardinalidad(resultado)==0:
    elementos=chr(216)
    lista={1,2,3,4,5,6,7}

  plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
  v = venn2(subsets = [lista,lista],set_labels = (operacion,'')) # Creo los dos conjuntos
  c = venn2_circles(subsets = [lista,lista],linestyle = 'dashed')
  v.get_label_by_id('11').set_text(elementos)
  v.get_label_by_id('01').set_visible(False)
  v.get_label_by_id('10').set_visible(False)
  	
  #v.get_label_by_id('A').set_color('white')
 # v.get_patch_by_id('11').set_color('green')
 # v.get_patch_by_id('10').set_color('green')
 # v.get_patch_by_id('01').set_color('green')
 # v.get_label_by_id('10').set_visible(False)
  #v.get_label_by_id('01').set_visible(False)
  
  tablaResultados(A,B,operacion,resultado,etiqueta1,etiqueta2)
  plt.show()

def graficar_diferencia(conj1,conj2,etiqueta1='A',etiqueta2='B',eleccion=True):
  """
  Grafica la diferencia entre conjuntos y muestras los datos de la operación

  Parámetros:
  conj1-tipo Set : Es el primer conjunto para la operación. Este conjunto ya ha sido formateado para su uso.
  conj2-tipo Set : Es el segundo conjunto para la opeación. Este conjunto ya ha sido formateado para su uso.
  etiqueta1-tipo String: Es la etiqueta para el primer conjunto. Por defecto se etiqueta como 'A'
  etiqueta2-tipo String: Es la etiqueta para el segundo conjunto. Por defecto se etiqeuta como 'B'
  eleccion-tipo Integer: Sirve para saber qué conjunto graficar. Ignorar si no se usa interfaz gráfica.
  """
  if eleccion:
    A=conj1
    B=conj2
  else:
    A=conj2
    B=conj1

  lbl1=etiqueta1
  lbl2=etiqueta2
  resultado=None
  operacion=etiqueta1 + " - " + etiqueta2
  incluido=subconjunto(A,B)
  v=None
  c=None
  resultado=A-B
  plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
   
 
    
  if(cardinalidad(resultado)==0) and cardinalidad(B)!=0:
    v = venn2(subsets = [B,B],set_labels = ('',etiqueta1+"-"+etiqueta2)) # Creo los dos conjuntos
    c = venn2_circles(subsets = [B,B],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(chr(216))
    v.get_label_by_id('10').set_visible(False)
    v.get_patch_by_id('10').set_color('green')
    v.get_patch_by_id('11').set_color('green')
  elif cardinalidad(A)==0 and cardinalidad(B)==0:
    C={1,2,3,4,5,6,7}# un conjunto accesorio para poder graficar el diagrama ya que ambos son vacíos
    v = venn2(subsets = [C,C],set_labels = ('',etiqueta1+"-"+etiqueta2)) # Creo los dos conjuntos
    c = venn2_circles(subsets = [C,C],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(chr(216))
    v.get_label_by_id('10').set_visible(False)
    v.get_patch_by_id('10').set_color('green')
    v.get_patch_by_id('11').set_color('green') 
  elif cardinalidad(A)!=0 and cardinalidad(B)==0:
    v = venn2(subsets = [A,A],set_labels = (etiqueta1+"-"+etiqueta2,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,A],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(A-B) 
  elif(cardinalidad(interseccion(A,B))==0):
    v = venn2(subsets = [A,B],set_labels = (str(etiqueta1),str(etiqueta2))) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('10').set_text(resultado)
    #v.get_patch_by_id('11').set_color('white')
    v.get_patch_by_id('01').set_color('white')
    v.get_label_by_id('01').set_visible(False)
    c[0].set_ls('solid')
    #v.get_label_by_id('11').set_visible(False)
  else:
    v = venn2(subsets = [A,B],set_labels = (str(etiqueta1),str(etiqueta2))) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('10').set_text(resultado)
    v.get_patch_by_id('11').set_color('white')
    v.get_patch_by_id('01').set_color('white')
    v.get_label_by_id('01').set_visible(False)
    v.get_label_by_id('11').set_visible(False)
 
  
  tablaResultados(A,B,operacion,resultado,etiqueta1,etiqueta2)
  plt.show()

def graficar_difsim(conj1,conj2,etiqueta1='A',etiqueta2='B',eleccion=True):
  """
  Permite graficar la diferencia simétirica entre dos conjuntos y muestra los datos de la operación
  Parámetros:

  conj1-tipo Set : Es el primer conjunto para la operación. Este conjunto ya ha sido formateado para su uso.
  conj2-tipo Set : Es el segundo conjunto para la opeación. Este conjunto ya ha sido formateado para su uso.
  etiqueta1-tipo String: Es la etiqueta para el primer conjunto. Por defecto se etiqueta como 'A'.
  etiqueta2-tipo String: Es la etiqueta para el segundo conjunto. Por defecto se etiqeuta como 'B'.
  eleccion-tipo Integer: Sirve para saber qué conjunto graficar. Ignorar si no se usa interfaz gráfica.
  """

  if eleccion:
    A=conj1
    B=conj2
  else:
    A=conj2
    B=conj1

  resultado=None
  operacion=etiqueta1+" ∆ "+etiqueta2
  difAB=A-B
  difBA=B-A
  c=None
  plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
  resultado=simetricdif(A,B)

  if (cardinalidad(A)==0 and cardinalidad(B)==0) or A==B:
    C={1,2,3,4,5,6,7}# un conjunto accesorio para poder graficar el diagrama ya que ambos son vacíos
    v = venn2(subsets = [C,C],set_labels = ('',operacion)) # Creo los dos conjuntos
    c = venn2_circles(subsets = [C,C],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(chr(216))
    v.get_label_by_id('10').set_visible(False)
    v.get_patch_by_id('10').set_color('green')
    v.get_patch_by_id('11').set_color('green') 
  elif cardinalidad(A)==0:
    v = venn2(subsets = [A,B],set_labels = ('',str(etiqueta2))) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('01').set_text(B)
    v.get_label_by_id('10').set_visible(False)
  elif cardinalidad(B)==0:
    v = venn2(subsets = [A,B],set_labels = (str(etiqueta1),'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('10').set_text(A)
    v.get_label_by_id('01').set_visible(False)
  elif subconjunto(A,B):
    v = venn2(subsets = [A,B],set_labels = (operacion,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('01').set_text(resultado)
    v.get_patch_by_id('11').set_color('white')
    v.get_patch_by_id('10').set_color('white')
    v.get_label_by_id('10').set_visible(False)
    v.get_label_by_id('11').set_visible(False)
  elif subconjunto(B,A):
    v = venn2(subsets = [A,B],set_labels = (operacion,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('10').set_text(resultado)
    v.get_patch_by_id('11').set_color('white')
    v.get_patch_by_id('01').set_color('white')
    v.get_label_by_id('01').set_visible(False)
    v.get_label_by_id('11').set_visible(False)
  else:
    v = venn2(subsets = [A,B],set_labels = (str(etiqueta1),str(etiqueta2))) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_patch_by_id('11').set_color('white')
    v.get_label_by_id('11').set_visible(False)
    v.get_label_by_id('10').set_text(interseccion(simetricdif(A,B),A))
    v.get_label_by_id('01').set_text(interseccion(simetricdif(A,B),B))
   
    
  tablaResultados(A,B,operacion,resultado,etiqueta1,etiqueta2)
  plt.show()
 

def graficar_conjunto(conjunto,U,nombre1 = "A",nombreU = 'U',mostrar_datos = True):
   """
   Permite graficar y mostrar los datos de un sólo conjunto.

   Parámetros:
   conjunto-tipo Set: conjunto que se graficará
   U-tipo Set: conjunto universal
   nombre1-tipo String: nombre que se asignará al conjunto. Por defecto es 'A'
   nombre2-tipo String: nombre que se asignará al conjunto universal. Por defecto es 'U'
   mostrar_Datos-tipo Boolean: si se asigna True, se mostrará una tabla de resultados
   """   
   if cardinalidad(conjunto)==0:
    C = {1} # un conjunto accesorio para poder graficar el diagrama ya que ambos son vacíos
    v = venn(C,C,U,nombre1 = nombre1,nombre2 = '',nombre3 = nombreU) # Creo el diagrama de venn para el conjunto vacío
    v.get_label_by_id('11').set_text(chr(216))
    v.get_label_by_id('10').set_visible(False)
    v.get_patch_by_id('10').set_color('green')
    v.get_patch_by_id('11').set_color('green')
   else:
    v = venn(conjunto,conjunto,U,nombre1 = nombre1,nombre2 = '',nombre3 = nombreU) # Creo el diagrama de venn para el conjunto único
   
   v.subset_labels[0].set_visible(False);
   v.subset_labels[1].set_visible(False);
   
   if(mostrar_datos):
     tabla_conj_unico(conjunto,nombre1)

def tablaResultados(A,B,operacion,resultado,etiqueta1,etiqueta2):
  """
  Muestra una leyenda con los conjuntos, operación, resultado y cardinalidades

  Parámetros:

  A-tipo Set: Primer conjunto resultante después de pasar por todos los controles.
  B-tipo Set: Segundo conjunto resultante después de pasar por todos los controles.
  etiqueta1-tipo String: Se usa para etiquetar al primer conjunto.
  etiqueta2-tipo String: Se usa para etiquetar al segundo conjunto.
  operación-tipo String: Representa qué operación fue realizada.
  resultado-tipo FiniteSet De Int: El conjunto resultado de la operación.
  """
  resultadoFinal=resultado
  lbl1=etiqueta1
  lbl2=etiqueta2
  resul1=None
  resul2=None
  if cardinalidad(resultado)==0:
    resultadoFinal=chr(216)# el vacío
  
  if cardinalidad(A)==0:
    resul1=chr(216)
  else:
    resul1=A

  if cardinalidad(B)==0:
    resul2=chr(216)
  else:
    resul2=B
  

  print("----------------------Señalando Datos Y Diagrama de la Operación " +operacion+"------------------------------")
  print("*************************************************************************************************************")
  print( " " + lbl1 + " = ",resul1,"\n",lbl2 + " = ",resul2,"\n","Cardinal " + lbl1 + " = ",cardinalidad(A),"\n","Cardinal " + lbl2+" = ",
    cardinalidad(B),"\n", operacion+" = ",resultadoFinal,"\n","Cardinal "+ operacion+" = ",cardinalidad(resultado))
  print("************************************************************************************************************")


def tabla_conj_unico(conjunto,nombre_conjunto):
  """
  Muestra los datos de un único conjunto
	Parámetros:
	conjunto-tipo Set: Es el conjunto cuyos datos se mostrará
	nombre_conjunto-tipo String: Es el nombre del conjunto

  """
  resultadoFinal=conjunto
  if cardinalidad(conjunto)==0:
   resultadoFinal=chr(216)# el vacío

  print("----------------------Señalando Datos Y Diagrama de " + nombre_conjunto +"------------------------------")
  print("*************************************************************************************************************")
  print(" "+nombre_conjunto + " = ",resultadoFinal,"\n","Cardinal " + nombre_conjunto + " = ",cardinalidad(conjunto),"\n")
  print("************************************************************************************************************")

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Funciones para diagramas de venn con tres conjuntos
#-----------------------------------------------------------------------------------------------------------------------------------------------
def graficar_union3(A,B,C,etiqueta1="A",etiqueta2="B",etiqueta3="C"):
    """
    Grafica la unión de tres conjunto

    Parámetros:

    A-tipo Set: Es el primer conjunto de la operación.
    B-tipo Set: Es el segundo conjunto de la operación.
    C-tipo Set: Es el tercer conjunto de la operación.
    etiqueta1-tipo String: La etiqueta para el primer conjunto. Por defecto tiene el valor "A".
    etiqueta2-tipo String: La etiqueta para el segundo conjunto. Por defecto tiene el valor "B".
    etiqueta3-tipo String: La etiqueta para el tercer conjunto. Por defecto tiene el valor "C".
    """
    D=union(A,B)
    H=union(D,C)
    operacion=etiqueta1 + "U" + etiqueta2 + "U" + etiqueta3
    plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
    v = None # Creo los dos conjuntos
    c = None
    if cardinalidad(A)==0 and cardinalidad(B)==0 and cardinalidad(C)==0:
      aux={1}
      v = venn3(subsets = [aux,aux,aux],set_labels = (operacion,'','')) # Creo los dos conjuntos
      c = venn3_circles(subsets = [aux,aux,aux],linestyle = 'dashed')
      v.get_label_by_id('111').set_text(chr(216))
    else:
      v = venn3(subsets = [H,H,H],set_labels = (operacion,'','')) # Creo los dos conjuntos
      c = venn3_circles(subsets = [H,H,H],linestyle = 'dashed')	
      v.get_label_by_id('111').set_text(H)


def graficar_interseccion3(A,B,C,etiqueta1="A",etiqueta2="B",etiqueta3="C"):
  """
  Grafica la intersección de tres conjunto

  Parámetros:

  A-tipo Set: Es el primer conjunto de la operación.
  B-tipo Set: Es el segundo conjunto de la operación.
  C-tipo Set: Es el tercer conjunto de la operación.
  etiqueta1-tipo String: La etiqueta para el primer conjunto. Por defecto tiene el valor "A".
  etiqueta2-tipo String: La etiqueta para el segundo conjunto. Por defecto tiene el valor "B".
  etiqueta3-tipo String: La etiqueta para el tercer conjunto. Por defecto tiene el valor "C".
  """
  D=interseccion(A,B)
  H=interseccion(D,C)
  #compruebo si algún conjunto es subconjunto de otro
  inter1= not (subconjunto(A,B) or subconjunto(A,C))
  inter2= not (subconjunto(B,C) or subconjunto(B,A))
  inter3= not (subconjunto(C,A) or subconjunto(C,B))

  #reviso si son disyuntos. 
  graficar_disyuntos=(cardinalidad(H)==0 and cardinalidad(A)!=0 and cardinalidad(B)!=0) and inter1 and inter2 and inter3

  operacion=etiqueta1 + " ∩ " + etiqueta2 + " ∩ " + etiqueta3
  plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
  v = None 
  c = None
  #grafica a los conjuntos por separados al ser disyuntos y no hay vacíos
  if graficar_disyuntos:
      v = venn3(subsets = [A,B,C],set_labels = (etiqueta1,etiqueta2,etiqueta3)) # Creo los dos conjuntos
      c = venn3_circles(subsets = [A,B,C],linestyle = 'dashed') 
      v.get_label_by_id('100').set_text(A)
      v.get_label_by_id('010').set_text(B)
      v.get_label_by_id('001').set_text(C)
    #grafica el vacío si es que alguno al menos es el vacío
  elif cardinalidad(H)==0:
      aux={1}
      v = venn3(subsets = [aux,aux,aux],set_labels = (operacion,'','')) # Creo los dos conjuntos
      c = venn3_circles(subsets = [aux,aux,aux],linestyle = 'dashed')
      v.get_label_by_id('111').set_text(chr(216))
  elif A==B and B==C:
      graficar_union3(A,B,C)
  else:
      v = venn3(subsets = [A,B,C],set_labels = (etiqueta1,etiqueta2,etiqueta3)) # Creo los dos conjuntos
      c = venn3_circles(subsets = [A,B,C],linestyle = 'dashed')
      v.get_label_by_id('111').set_text(H)
      v.get_patch_by_id('111').set_color('green') 
      #revisa si cada zona existe y de ser así elimina el texto y color de éstas, excepto la zona de la inter
      #sección
      if v.get_label_by_id('100'):
        v.get_label_by_id('100').set_text('')
        v.get_patch_by_id('100').set_color('white') 

      if v.get_label_by_id('110'):
        v.get_label_by_id('110').set_text('')
        v.get_patch_by_id('110').set_color('white')

      if v.get_patch_by_id('010'):
        v.get_label_by_id('010').set_text('')
        v.get_patch_by_id('010').set_color('white')

      if v.get_label_by_id('011'):
        v.get_label_by_id('011').set_text('')
        v.get_patch_by_id('011').set_color('white') 

      if v.get_label_by_id('001'):
        v.get_label_by_id('001').set_text('')
        v.get_patch_by_id('001').set_color('white')

      if v.get_label_by_id('101'):
        v.get_label_by_id('101').set_text('')
        v.get_patch_by_id('101').set_color('white') 

def graficar_diferencia3(A,B,C,etiqueta1="A",etiqueta2="B",etiqueta3="C"):
    """
    Grafica la diferencia de tres conjunto

    Parámetros:

    A-tipo Set: Es el primer conjunto de la operación.
    B-tipo Set: Es el segundo conjunto de la operación.
    C-tipo Set: Es el tercer conjunto de la operación.
    etiqueta1-tipo String: La etiqueta para el primer conjunto. Por defecto tiene el valor "A".
    etiqueta2-tipo String: La etiqueta para el segundo conjunto. Por defecto tiene el valor "B".
    etiqueta3-tipo String: La etiqueta para el tercer conjunto. Por defecto tiene el valor "C".
    """
    H=A-B-C
    
    operacion=etiqueta1 + " - " + etiqueta2 + "  - " + etiqueta3
    plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
    v = None # Creo los dos conjuntos
    c = None
    #grafico si el resultado es el vacío
    if cardinalidad(H)==0:
      aux={1}
      v = venn3(subsets = [aux,aux,aux],set_labels = (operacion,'','')) # Creo los dos conjuntos
      c = venn3_circles(subsets = [aux,aux,aux],linestyle = 'dashed')
      v.get_label_by_id('111').set_text(chr(216))
    else:
      v = venn3(subsets = [A,B,C],set_labels = (operacion,etiqueta2,etiqueta3)) # Creo los dos conjuntos
      c = venn3_circles(subsets = [A,B,C],linestyle = 'dashed')
      v.get_label_by_id('100').set_text(H)
      v.get_patch_by_id('100').set_color('green') 
      #revisa si cada zona existe y de ser así elimina el texto y color de éstas, en caso de que haya una
      #inclusión entre el primer conjunto y alguno de los otros, los pinta del mismo color
      if v.get_label_by_id('111'):
        v.get_label_by_id('111').set_text('')
        v.get_patch_by_id('111').set_color('white') 

      if v.get_label_by_id('110'):
        v.get_label_by_id('110').set_text('')
        if subconjunto(B,A):
          v.get_patch_by_id('110').set_color('green')
        else:
          v.get_patch_by_id('110').set_color('white')

      if v.get_patch_by_id('010'):
        v.get_patch_by_id('010').set_color('white')
        v.get_label_by_id('010').set_text('')

      if v.get_label_by_id('011'):
        v.get_patch_by_id('011').set_color('white')
        v.get_label_by_id('011').set_text('') 

      if v.get_label_by_id('001'):
        v.get_label_by_id('001').set_text('')
        v.get_patch_by_id('001').set_color('white')

      if v.get_label_by_id('101'):
        v.get_label_by_id('101').set_text('')
        if subconjunto(C,A):
          v.get_patch_by_id('101').set_color('green') 
        else:
          v.get_patch_by_id('101').set_color('white') 

def graficar_difsim3(A,B,C,etiqueta1="A",etiqueta2="B",etiqueta3="C"):
    """
    Grafica la diferencia simétrica de tres conjunto

    Parámetros:

    A-tipo Set: Es el primer conjunto de la operación.
    B-tipo Set: Es el segundo conjunto de la operación.
    C-tipo Set: Es el tercer conjunto de la operación.
    etiqueta1-tipo String: La etiqueta para el primer conjunto. Por defecto tiene el valor "A".
    etiqueta2-tipo String: La etiqueta para el segundo conjunto. Por defecto tiene el valor "B".
    etiqueta3-tipo String: La etiqueta para el tercer conjunto. Por defecto tiene el valor "C".
    """
    H=simetricdif(simetricdif(A,B),C)
    operacion=etiqueta1 + " ∆ " + etiqueta2 + " ∆ " + etiqueta3
    plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
    v = None # Creo los dos conjuntos
    c = None
    #grafico el vacío porque, aunque sean disyuntos, hay algunos conjuntos que tienen elementos en común
    if cardinalidad(H)==0:
      aux={1}
      v = venn3(subsets = [aux,aux,aux],set_labels = (operacion,'','')) # Creo los dos conjuntos
      c = venn3_circles(subsets = [aux,aux,aux],linestyle = 'dashed')
      v.get_label_by_id('111').set_text(chr(216))
    elif A==B and B==C:
      v = venn3(subsets = [A,B,C],set_labels = (operacion,'','')) # Creo los dos conjuntos
      c = venn3_circles(subsets = [A,B,C],linestyle = 'dashed')
      v.get_label_by_id('111').set_text(H)
    else:
      v = venn3(subsets = [A,B,C],set_labels = (etiqueta1,etiqueta2,etiqueta3)) # Creo los dos conjuntos
      c = venn3_circles(subsets = [A,B,C],linestyle = 'dashed') 
      #revisa si cada zona existe y de ser así elimina el texto y color de éstas. Si hay alguna inclusión
      #entre los cojuntos, se asegura de dejar vacío las etiquetas y pintarlo de blanco.
      #Si son disyuntos, muestra los tres conjuntos por separado.
      #Si uno solamente es disyunto con los otros dos, muestra a los dos primeros intersectados (dejando en
      # blanco la parte de la intersección) y el tercer conjunto se grafica por separado
      if v.get_label_by_id('111'):
        v.get_label_by_id('111').set_text('')
        v.get_patch_by_id('111').set_color('white') 

      if v.get_label_by_id('110'):
        v.get_label_by_id('110').set_text('')
        v.get_patch_by_id('110').set_color('white')

      if v.get_patch_by_id('010'):
        resultado=B-A-C
        if cardinalidad(resultado)==0:
          v.get_patch_by_id('010').set_color('white')
          v.get_label_by_id('010').set_text('')
        else:
          v.get_patch_by_id('010').set_color('red')
          v.get_label_by_id('010').set_text(resultado)

      if v.get_label_by_id('011'):
        v.get_patch_by_id('011').set_color('white')
        v.get_label_by_id('011').set_text('') 

      if v.get_label_by_id('001'):
        resultado=C-A-B
        if cardinalidad(resultado)==0:
          v.get_label_by_id('001').set_text('')
          v.get_patch_by_id('001').set_color('white')
        else:
          v.get_label_by_id('001').set_text(resultado)
          v.get_patch_by_id('001').set_color('green')

      if v.get_label_by_id('101'):
        v.get_label_by_id('101').set_text('')
        v.get_patch_by_id('101').set_color('white')

      if v.get_label_by_id('100'):
        resultado=A-B-C
        if cardinalidad(resultado)==0:
          v.get_label_by_id('100').set_text('')
          v.get_patch_by_id('100').set_color('white')
        
        else:
          v.get_label_by_id('100').set_text(resultado)
          v.get_patch_by_id('100').set_color('blue')
            
def documentacion():
    print("------------------------------------------------------------------------------------------------------------------")
    help(complemento)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_diferencia)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_interseccion)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_union)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_difsim)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_diferencia3)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_interseccion3)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_union3)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_difsim3)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_conjunto)
    print("------------------------------------------------------------------------------------------------------------------")
    help(conjunto)
    print("------------------------------------------------------------------------------------------------------------------")
    help(cardinalidad)
    print("------------------------------------------------------------------------------------------------------------------")
    help(pertenece)
    print("------------------------------------------------------------------------------------------------------------------")
    help(subconjunto)
    print("------------------------------------------------------------------------------------------------------------------")
    help(union)
    print("------------------------------------------------------------------------------------------------------------------")
    help(interseccion)
    print("------------------------------------------------------------------------------------------------------------------")
    help(producto_cartesiano)
    print("------------------------------------------------------------------------------------------------------------------")
    help(simetricdif)
    

#--------- MÉTODOS AUXILIARES ---------------------------------
def printm(s): # Imprime usando formato LaTeX.
  '''
  Argumentos:

  s: tipo RAW STRING, debe ser inicializado como s = r'...'
  '''
  display(Math(s))
    
def set_fontsize(v,fs):
  """
  Cambia el tamaño de la fuente en todos los labels

  Parámetros:

  v-tipo venn: diagrama de venn retornado por la función venn()
  fs-tipo int: tamaño de fuente (entero positivo)
  """
  for t in v.set_labels: 
    if(t is not None): 
        t.set_fontsize(fs)

  for t in v.subset_labels: 
    if(t is not None): 
        t.set_fontsize(fs)