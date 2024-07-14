import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import tkinter as tk
from tkinter import messagebox

# Función para interpretar y graficar una expresión matemática
def interpretar_y_graficar(expr_str):
    try:
        # Definir el símbolo x
        x = sp.symbols('x')
        
        # Interpretar la expresión
        expr = sp.sympify(expr_str)
        
        # Convertir la expresión en una función lambda para evaluación numérica
        expr_lambda = sp.lambdify(x, expr, "numpy")
        
        # Crear un rango de valores para x
        x_vals = np.linspace(-10, 10, 400)
        y_vals = expr_lambda(x_vals)
        
        # Crear la gráfica
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'y = {sp.pretty(expr)}')
        plt.title(f'Gráfica de y = {expr_str}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.legend()
        
        # Mostrar la gráfica
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo interpretar la expresión: {e}")

# Función que se ejecuta al hacer clic en el botón
def graficar():
    expr_str = entry.get()
    interpretar_y_graficar(expr_str)

# Crear la ventana principal
root = tk.Tk()
root.title("Graficador de Expresiones Matemáticas")

# Crear y colocar los widgets
label = tk.Label(root, text="Escribe una expresión matemática:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Graficar", command=graficar)
button.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
