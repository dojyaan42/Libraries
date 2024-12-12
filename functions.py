def calcular_mediana(lista):
    """
    Calcula la mediana de una lista de números

    Input:
      lista: Una lista de números.

    Output:
      La mediana de la lista.
    """
    n = len(lista)
    if n == 0:
        return None  # Manejar el caso de una lista vacía

    lista_ordenada = sorted(lista)  # Ordenar la lista

    if n % 2 == 0:  # Si la longitud es par
        medio1 = lista_ordenada[n // 2 - 1]
        medio2 = lista_ordenada[n // 2]
        mediana = (medio1 + medio2) / 2
    else:  # Si la longitud es impar
        mediana = lista_ordenada[n // 2]

    return mediana

def calcular_moda(lista):
    """
    Calcula la moda de una lista de números sin usar librerías.

    Input:
      lista: Una lista de números.

    Output:
      La moda de la lista. Si hay varias modas, regresa la primera encontrada.
      Regresa None si la lista está vacía.
    """
    if not lista:
        return None

    conteo = {}
    for elemento in lista:
        conteo[elemento] = conteo.get(elemento, 0) + 1

    moda = None
    max_conteo = 0
    for elemento, frecuencia in conteo.items():
        if frecuencia > max_conteo:
            moda = elemento
            max_conteo = frecuencia

    return moda

def calcular_promedio(lista):
    """
    Calcula el promedio de una lista de números sin usar librerías.

    Input:
      lista: Una lista de números.

    Output:
      El promedio de la lista. Regresa 0 si la lista está vacía para evitar errores de división entre cero.
    """
    if not lista:
        return 0  # Regresar 0 si la lista está vacía
    suma = 0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def calcular_rango(lista):
    """
    Calcula el rango de una lista de números sin utilizar librerías.

    Input:
      lista: Una lista de números.

    Output:
      El rango de la lista (diferencia entre el valor máximo y mínimo).
      Regresa 0 si la lista está vacía o tiene un solo elemento.
    """
    if len(lista) < 2:
        return 0

    minimo = lista[0]
    maximo = lista[0]

    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero

    return maximo - minimo

def calcular_varianza(lista):
    """
    Calcula la varianza de una lista de números sin utilizar librerías.

    Input:
      lista: Una lista de números.

    Output:
      La varianza de la lista. Regresa 0 si la lista tiene menos de dos elementos.
    """
    n = len(lista)
    if n < 2:
        return 0  # Varianza indefinida para menos de dos elementos

    promedio = calcular_promedio(lista)
    suma_cuadrados_diferencias = 0
    for numero in lista:
        suma_cuadrados_diferencias += (numero - promedio) ** 2

    varianza = suma_cuadrados_diferencias / n
    return varianza

def calcular_desviacion_estandar(lista):
    """
    Calcula la desviación estándar de una lista de números sin utilizar librerías.

    Input:
      lista: Una lista de números.

    Output:
      La desviación estándar de la lista. Regresa 0 si la lista tiene menos de dos elementos.

    """
    varianza = calcular_varianza(lista)
    desviacion_estandar = varianza ** (1/2)
    return desviacion_estandar

def calcular_mediana(lista):
    """
    Calcula la mediana de una lista de números

    Input:
      lista: Una lista de números.

    Output:
      La mediana de la lista.
    """
    n = len(lista)
    if n == 0:
        return None  # Manejar el caso de una lista vacía

    lista_ordenada = sorted(lista)  # Ordenar la lista

    if n % 2 == 0:  # Si la longitud es par
        medio1 = lista_ordenada[n // 2 - 1]
        medio2 = lista_ordenada[n // 2]
        mediana = (medio1 + medio2) / 2
    else:  # Si la longitud es impar
        mediana = lista_ordenada[n // 2]

    return mediana

def calcular_rango_intercuartil(lista):
    """
    Calcula el rango intercuartil de una lista de números sin usar librerías.

    Input:
      lista: Una lista de números.

    Output:
      El rango intercuartil de la lista. Regresa 0 si la lista tiene menos de 4 elementos.
    """
    n = len(lista)
    if n < 4:
        return 0

    lista_ordenada = sorted(lista)

    # Calcular la posición de los cuartiles
    q1_index = (n + 1) // 4
    q3_index = 3 * (n + 1) // 4

    # Calcular los cuartiles Q1 y Q3
    q1 = lista_ordenada[q1_index -1] if q1_index <= len(lista_ordenada) else lista_ordenada[-1]
    q3 = lista_ordenada[q3_index-1] if q3_index <= len(lista_ordenada) else lista_ordenada[-1]

    # Calcular el rango intercuartil (IQR)
    rango_intercuartil = q3 - q1

    return rango_intercuartil

def desviacion_mediana_absoluta(lista):
    """
    Calcula la desviación mediana absoluta de una lista de números sin usar librerías.

    Input:
      lista: Una lista de números.

    Output:
      La desviación mediana absoluta de la lista.
    """
    if not lista:
        return 0  # Manejar el caso de una lista vacía

    mediana = calcular_mediana(lista)

    # Calcular las desviaciones absolutas respecto a la mediana
    desviaciones_absolutas = [abs(x - mediana) for x in lista]

    # Calcular la mediana de las desviaciones absolutas
    desviacion_mediana_absoluta = calcular_mediana(desviaciones_absolutas)

    return desviacion_mediana_absoluta

def calcular_covarianza(lista1, lista2):
    """
    Calcula la covarianza de dos listas de números sin utilizar librerías.

    Input:
      lista1: La primera lista de números.
      lista2: La segunda lista de números.

    Output:
      La covarianza de las dos listas. Regresa 0 si las listas tienen longitudes diferentes o menos de dos elementos.
    """
    n = len(lista1)
    if n != len(lista2) or n < 2:
        return 0

    promedio1 = calcular_promedio(lista1)
    promedio2 = calcular_promedio(lista2)

    suma_productos_diferencias = 0
    for i in range(n):
        suma_productos_diferencias += (lista1[i] - promedio1) * (lista2[i] - promedio2)

    covarianza = suma_productos_diferencias / n
    return covarianza

import math

def calcular_coeficiente_correlacion(lista1, lista2):
    """
    Calcula el coeficiente de correlación de Pearson de dos listas de números sin utilizar librerías.

    Input:
      lista1: La primera lista de números.
      lista2: La segunda lista de números.

    Output:
      El coeficiente de correlación de Pearson. Regresa 0 si las listas tienen longitudes diferentes o menos de dos elementos,
      o si alguna de las desviaciones estándar es cero.
    """
    n = len(lista1)
    if n != len(lista2) or n < 2:
        return 0

    covarianza = calcular_covarianza(lista1, lista2)
    desviacion_estandar1 = math.sqrt(calcular_varianza(lista1))
    desviacion_estandar2 = math.sqrt(calcular_varianza(lista2))

    if desviacion_estandar1 == 0 or desviacion_estandar2 == 0:
        return 0  # Evitar división por cero

    coeficiente_correlacion = covarianza / (desviacion_estandar1 * desviacion_estandar2)
    return coeficiente_correlacion

def calcular_coeficiente_determinacion(lista1, lista2):
    """
    Calcula el coeficiente de determinación (r^2) de dos listas de números sin utilizar librerías.

    Input:
      lista1: La primera lista de números (variable independiente).
      lista2: La segunda lista de números (variable dependiente).

    Output:
      El coeficiente de determinación (r^2). Regresa 0 si las listas tienen longitudes diferentes o menos de dos elementos.
    """
    r = calcular_coeficiente_correlacion(lista1, lista2)
    r2 = r**2
    return r2
    