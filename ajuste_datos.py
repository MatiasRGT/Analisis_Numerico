import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Definir los datos
x = np.array([1, 1.5, 2, 2.5, 3, 3.5])
f = np.array([2.475, 2.008, 2.272, 3.204, 4.578, 6.050])

# Definir la función modelo (no lineal en este caso)
def modelo_no_lineal(x, c1, c2):
    return c1 - c2 * np.sin(x)

# Realizar el ajuste usando scipy.optimize.curve_fit
parametros_iniciales = [1, 1]  # Estimación inicial de los parámetros
parametros_optimos, covarianza = curve_fit(modelo_no_lineal, x, f, p0=parametros_iniciales)

# Imprimir los parámetros óptimos
c1_opt, c2_opt = parametros_optimos
print(f"c1 = {c1_opt}")
print(f"c2 = {c2_opt}")

# Crear puntos de la función ajustada para la visualización
x_fit = np.linspace(min(x), max(x), 100)
f_fit = modelo_no_lineal(x_fit, c1_opt, c2_opt)

# Visualizar los datos y la función ajustada
plt.scatter(x, f, color='red', label='Datos')
plt.plot(x_fit, f_fit, color='blue', label='Ajuste no lineal')
plt.xlabel('x')
plt.ylabel('f')
plt.legend()
plt.title('Ajuste no lineal usando mínimos cuadrados')
plt.show()
