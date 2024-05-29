import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos proporcionados
x = np.array([1, 1.5, 2, 2.5, 3, 3.5])
f = np.array([2.475, 2.008, 2.272, 3.204, 4.578, 6.050])

# Definición de la función modelo no lineal
def modelo_no_lineal(x, c1, c2):
    return c1 - c2 * np.sin(x)

# Definición de la función de error cuadrático medio
def error_cuadratico_medio(f_observado, f_modelado):
    return np.mean((f_observado - f_modelado) ** 2)

# Ajuste de los parámetros del modelo utilizando mínimos cuadrados no lineales
parametros_optimos, covarianza = curve_fit(modelo_no_lineal, x, f)

# Valores óptimos de los parámetros
c1_opt, c2_opt = parametros_optimos

# Valores modelados utilizando los parámetros óptimos
f_modelado = modelo_no_lineal(x, c1_opt, c2_opt)

# Cálculo del error cuadrático medio
ecm = error_cuadratico_medio(f, f_modelado)

# Mostrar sumatorias matriziales paso a paso
# Matriz de diseño
X = np.vstack((np.ones_like(x), -np.sin(x))).T

# Sumatorias matriziales
A = np.dot(X.T, X)
B = np.dot(X.T, f)

# Mostrar matrices
print("Matriz de diseño X:")
print(X)
print("\nMatriz A = X^T * X:")
print(A)
print("\nVector B = X^T * f:")
print(B)

# Mostrar valores óptimos de los parámetros
print("\nParámetros óptimos:")
print(f"c1 = {c1_opt}, c2 = {c2_opt}")

# Mostrar error cuadrático medio
print("\nError cuadrático medio (ECM):")
print(ecm)

# Graficar los datos observados y el ajuste del modelo
plt.figure(figsize=(10, 6))
plt.scatter(x, f, label='Datos observados', color='red')
plt.plot(x, f_modelado, label='Modelo ajustado', color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Ajuste del modelo no lineal')
plt.show()
