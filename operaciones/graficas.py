import matplotlib.pyplot as plt
import numpy as np
import os
from django.conf import settings

def generar_grafica(funcion, raiz=None):
    # Valores de x para la gráfica
    x = np.linspace(-10, 10, 400)
    y = []

    for valor in x:
        try:
            y.append(funcion(valor))
        except:
            y.append(np.nan)  # Ignorar errores de dominio

    # Crear la gráfica
    plt.figure()
    plt.plot(x, y, label='f(x)', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Si hay raíz, marcarla en la gráfica
    if raiz is not None:
        try:
            y_raiz = funcion(raiz)
            plt.plot(raiz, y_raiz, 'ro', label='Raíz')
            plt.annotate(f"Raíz: {raiz:.4f}", xy=(raiz, y_raiz), xytext=(raiz, y_raiz+1),
                         arrowprops=dict(arrowstyle='->', color='red'), color='red')
        except:
            pass

    plt.grid(True)
    plt.title('Gráfica de f(x)')
    plt.legend()

    # Crear la carpeta si no existe
    ruta_carpeta = os.path.join(settings.BASE_DIR, 'static', 'graficas')
    os.makedirs(ruta_carpeta, exist_ok=True)

    # Ruta absoluta para guardar la imagen
    ruta_imagen = os.path.join(ruta_carpeta, 'grafica.png')
    plt.savefig(ruta_imagen)
    plt.close()

    # Ruta relativa que usará Django en el template
    return 'graficas/grafica.png'
