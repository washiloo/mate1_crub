# --------------------------------------------
# Trabajo práctico 1: Conjuntos
# --------------------------------------------
from sympy import FiniteSet

def conjunto(*args): # Devuelve un conjunto definido por extensión con los elementos dados en el argumento, separados por comas
  """
  Devuelve un conjunto definido por extensión con los elementos dados en el argumento, separados por comas

  Parámetros:

  *args-tipo variable: Representa el conjunto de elemntos separados por coma que se usarán para crear el conjunto.
  """
  if(isinstance(args[0],list)):
    return set(args[0])
  return set(args)

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