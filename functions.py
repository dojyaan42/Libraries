def mediana(lista):
    """
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

def moda(lista):
    """
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

def promedio(lista):
    """
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

    mean = suma / len(lista)
    return mean

def rango(lista):
    """
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

def varianza(lista):
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
    suma = 0
    for numero in lista:
        suma += numero
    mean = suma / len(lista)
    promedio = mean
    suma_cuadrados_diferencias = 0
    for numero in lista:
        suma_cuadrados_diferencias += (numero - promedio) ** 2

    variance = suma_cuadrados_diferencias / n
    return variance

def desviacion_estandar(lista):
    """
    Input:
      lista: Una lista de números.

    Output:
      La desviación estándar de la lista. Regresa 0 si la lista tiene menos de dos elementos.

    """
    n = len(lista)
    if n < 2:
        return 0  # Varianza indefinida para menos de dos elementos

    if not lista:
        return 0  # Regresar 0 si la lista está vacía
    suma = 0
    for numero in lista:
        suma += numero

    mean = suma / len(lista)
    
    promedio = mean
    suma_cuadrados_diferencias = 0
    for numero in lista:
        suma_cuadrados_diferencias += (numero - promedio) ** 2

    varianza = suma_cuadrados_diferencias / n
    desviacion_estandar = varianza ** (1/2)
    return desviacion_estandar


def mediana(lista):
    """
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

percentil(ordenada, percentil):
    pos = percentil * (len(ordenada) - 1)
    piso = int(pos)
    techo = piso + 1
    peso = pos - piso

    if techo < len(ordenada):
        return ordenada[piso] * (1 - peso) + ordenada[techo] * peso
    else:
        return ordenada[piso]

def cuartiles(lista):
    """
    Input:
      lista: Una lista de números.

    Output:
      Una lista con los cuartiles [Q0, Q1, Q2, Q3, Q4].
      Q0: Mínimo
      Q1: Primer cuartil (25%)
      Q2: Mediana (50%)
      Q3: Tercer cuartil (75%)
      Q4: Máximo
    """
    n = len(lista)
    if n == 0:
        return [None, None, None, None, None]  # Lista vacía

    lista_ordenada = sorted(lista)

    # Calcular los índices de los cuartiles
    q0 = lista_ordenada[0]  # Mínimo
    q4 = lista_ordenada[-1]  # Máximo

    # Función para calcular un percentil
    def percentil(ordenada, percentil):
        pos = percentil * (len(ordenada) - 1)
        piso = int(pos)
        techo = piso + 1
        peso = pos - piso

        if techo < len(ordenada):
            return ordenada[piso] * (1 - peso) + ordenada[techo] * peso
        else:
            return ordenada[piso]

    q1 = percentil(lista_ordenada, 0.25)  # Primer cuartil
    q2 = percentil(lista_ordenada, 0.50)  # Mediana
    q3 = percentil(lista_ordenada, 0.75)  # Tercer cuartil

    return [q0, q1, q2, q3, q4]

def rango_intercuartil(lista):
    """
    Input:
      lista: Una lista de números.

    Output:
      El rango intercuartil de la lista. Regresa 0 si la lista tiene menos de 4 elementos.
    """
    n = len(lista)
    if n < 4:
        return 0

    lista_ordenada = sorted(lista)

    q1_index = (n + 1) // 4
    q3_index = 3 * (n + 1) // 4

    q1 = lista_ordenada[q1_index -1] if q1_index <= len(lista_ordenada) else lista_ordenada[-1]
    q3 = lista_ordenada[q3_index-1] if q3_index <= len(lista_ordenada) else lista_ordenada[-1]

    rango_intercuartil = q3 - q1

    return rango_intercuartil

def desviacion_mediana_absoluta(lista):
    """
    Input:
      lista: Una lista de números.

    Output:
      La desviación mediana absoluta de la lista.
    """
    n = len(lista)
    if n == 0:
        return None

    lista_ordenada = sorted(lista)

    if n % 2 == 0:
        medio1 = lista_ordenada[n // 2 - 1]
        medio2 = lista_ordenada[n // 2]
        median_val = (medio1 + medio2) / 2
    else:
        median_val = lista_ordenada[n // 2]

    desviaciones_absolutas = [abs(x - median_val) for x in lista]

    desviacion_median_absoluta = mediana(desviaciones_absolutas)

    return desviacion_median_absoluta

def covarianza(lista1, lista2):
    """
    Input:
      lista1: La primera lista de números.
      lista2: La segunda lista de números.

    Output:
      La covarianza de las dos listas. Regresa 0 si las listas tienen longitudes diferentes o menos de dos elementos.
    """
    n = len(lista1)
    if n != len(lista2) or n < 2:
        return 0

    promedio1 = promedio(lista1)
    promedio2 = promedio(lista2)

    suma_productos_diferencias = 0
    for i in range(n):
        suma_productos_diferencias += (lista1[i] - promedio1) * (lista2[i] - promedio2)

    covarianza = suma_productos_diferencias / n
    return covarianza

import math

def coeficiente_correlacion(lista1, lista2):
    """
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

    covarianza = covarianza(lista1, lista2)
    desviacion_estandar1 = math.sqrt(varianza(lista1))
    desviacion_estandar2 = math.sqrt(varianza(lista2))

    if desviacion_estandar1 == 0 or desviacion_estandar2 == 0:
        return 0

    coeficiente_correlacion = covarianza / (desviacion_estandar1 * desviacion_estandar2)
    return coeficiente_correlacion

def coeficiente_determinacion(lista1, lista2):
    """
    Input:
      lista1: La primera lista de números (variable independiente).
      lista2: La segunda lista de números (variable dependiente).

    Output:
      El coeficiente de determinación (r^2). Regresa 0 si las listas tienen longitudes diferentes o menos de dos elementos.
    """
    r = coeficiente_correlacion(lista1, lista2)
    r2 = r**2
    return r2
    
