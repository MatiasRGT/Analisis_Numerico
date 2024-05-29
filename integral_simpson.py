import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Define aquí la función que deseas integrar
    return np.exp(x**2)  # Ejemplo: f(x) = x^2

def simpson_rule(a, b, n):
    """
    Aproxima la integral de f(x) en el intervalo [a, b] usando la regla de Simpson con n subintervalos.
    """
    if n % 2 == 1:
        raise ValueError("El número de subintervalos debe ser par.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    print(f"Paso 1: Calcular h = (b - a) / n")
    print(f"h = ({b} - {a}) / {n} = {h}")
    
    print("\nPaso 2: Calcular los puntos x y f(x)")
    for i in range(n + 1):
        print(f"x{i} = {x[i]}, f(x{i}) = {y[i]}")

    print("\nPaso 3: Aplicar la fórmula de Simpson")
    S = y[0] + y[-1]
    print(f"S = f(x0) + f(xn) = {y[0]} + {y[-1]} = {S}")

    print("\nPaso 4: Sumar 4*f(x) para los puntos impares")
    for i in range(1, n, 2):
        S += 4 * y[i]
        print(f"S += 4*f(x{i}) = 4*{y[i]} = {4*y[i]}")

    print("\nPaso 5: Sumar 2*f(x) para los puntos pares")
    for i in range(2, n-1, 2):
        S += 2 * y[i]
        print(f"S += 2*f(x{i}) = 2*{y[i]} = {2*y[i]}")

    S *= h / 3
    print(f"\nPaso 6: Multiplicar por h/3")
    print(f"S *= {h}/3 = {S}")

    return S, x, y

# Parámetros de la integral
a = 0  # Límite inferior
b = 1 # Límite superior
n = 4  # Número de subintervalos (debe ser par)

resultado, x, y = simpson_rule(a, b, n)
print(f"\nLa integral aproximada es: {resultado}")

# Graficar la función y los puntos
x_fine = np.linspace(a, b, 1000)
y_fine = f(x_fine)

plt.plot(x_fine, y_fine, label='f(x)')
plt.scatter(x, y, color='red', label='Puntos de Simpson')
plt.title('Aproximación de la Integral por la Regla de Simpson')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
