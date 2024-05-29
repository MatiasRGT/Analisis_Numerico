import numpy as np

def diferencias_divididas(x, y):
    """
    Calcula la tabla de diferencias divididas de Newton.
    
    Parámetros:
    x : array-like
        Lista de valores de los puntos x.
    y : array-like
        Lista de valores de los puntos y correspondientes a los valores de x.
    
    Retorna:
    np.ndarray
        Tabla de diferencias divididas.
    """
    n = len(x)
    tabla = np.zeros((n, n))
    tabla[:,0] = y

    for j in range(1, n):
        for i in range(n-j):
            tabla[i,j] = (tabla[i+1,j-1] - tabla[i,j-1]) / (x[i+j] - x[i])
    
    return tabla

def polinomio_newton(tabla, x, xi):
    """
    Evalúa el polinomio de interpolación de Newton en un punto dado.
    
    Parámetros:
    tabla : np.ndarray
        Tabla de diferencias divididas de Newton.
    x : array-like
        Lista de valores de los puntos x utilizados para calcular las diferencias divididas.
    xi : float
        Valor en el que se desea evaluar el polinomio de interpolación.
    
    Retorna:
    float
        Valor del polinomio de interpolación en xi.
    """
    n = len(x)
    resultado = tabla[0, 0]
    producto = 1.0

    for i in range(1, n):
        producto *= (xi - x[i-1])
        resultado += tabla[0, i] * producto
    
    return resultado

# Ejemplo de uso
x = [2, 3, 5, 6,1]
y = [8, 27, 125, 216,1]

# Calcular la tabla de diferencias divididas
tabla_diferencias = diferencias_divididas(x, y)
print("Tabla de diferencias divididas:")
print(tabla_diferencias)

# Evaluar el polinomio de interpolación en un punto
xi = 2.5
resultado = polinomio_newton(tabla_diferencias, x, xi)
print(f"El valor del polinomio de interpolación en x = {xi} es {resultado}")
