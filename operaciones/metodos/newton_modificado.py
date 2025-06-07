def metodo_newton_raphson_modificado(funcion, derivada, valor_inicial, cantidad_iteraciones):
    x_actual = valor_inicial
    tabla = []
    derivada_en_x0 = derivada(x_actual)

    if derivada_en_x0 == 0:
        raise ValueError("La derivada inicial es cero. No se puede continuar.")

    for i in range(1, cantidad_iteraciones + 1):
        f_x = funcion(x_actual)
        x_siguiente = x_actual - f_x / derivada_en_x0

        tabla.append({
            'Iteración': i,
            'x': round(x_actual, 6),
            'f(x)': round(f_x, 6),
            "f'(x0)": round(derivada_en_x0, 6),
            'x siguiente': round(x_siguiente, 6)
        })

        x_actual = x_siguiente

    return x_actual, tabla