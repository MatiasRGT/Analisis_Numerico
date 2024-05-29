import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Define aquí la función que deseas integrar
    return np.exp(x**2)  # Función: e^(x^2)

def trapezoidal_rule(a, b, n):
    """
    Aproxima la integral de f(x) en el intervalo [a, b] usando la regla del trapecio con n subintervalos.
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    print(f"Paso 1: Calcular h = (b - a) / n")
    print(f"h = ({b} - {a}) / {n} = {h}")
    
    print("\nPaso 2: Calcular los puntos x y f(x)")
    for i in range(n + 1):
        print(f"x{i} = {x[i]}, f(x{i}) = {y[i]}")

    print("\nPaso 3: Aplicar la fórmula del trapecio")
    S = (y[0] + y[-1]) / 2
    print(f"S = (f(x0) + f(xn)) / 2 = ({y[0]} + {y[-1]}) / 2 = {S}")

    print("\nPaso 4: Sumar 2*f(x) para los puntos interiores")
    for i in range(1, n):
        S += y[i]
        print(f"S += f(x{i}) = {y[i]}")

    S *= h
    print(f"\nPaso 5: Multiplicar por h")
    print(f"S *= {h} = {S}")

    return S, x, y

# Parámetros de la integral
a = 0  # Límite inferior
b = 1  # Límite superior
n = 5  # Número de subintervalos

resultado, x, y = trapezoidal_rule(a, b, n)
print(f"\nLa integral aproximada es: {resultado}")

# Graficar la función y los puntos
x_fine = np.linspace(a, b, 1000)
y_fine = f(x_fine)

plt.plot(x_fine, y_fine, label='f(x) = e^(x^2)')
plt.scatter(x, y, color='red', label='Puntos del Trapecio')
plt.title('Aproximación de la Integral por la Regla del Trapecio')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
