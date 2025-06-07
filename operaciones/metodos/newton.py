def metodo_newton_raphson(funcion, derivada_funcion, valor_inicial, cantidad_iteraciones):
    tabla_iteraciones = []
    valor_actual = valor_inicial

    for numero_iteracion in range(1, cantidad_iteraciones + 1):
        valor_funcion = funcion(valor_actual)
        valor_derivada = derivada_funcion(valor_actual)

        if valor_derivada == 0:
            break

        siguiente_valor = valor_actual - valor_funcion / valor_derivada

        tabla_iteraciones.append({
            "Iteración": numero_iteracion,
            "x": round(valor_actual, 6),
            "f(x)": round(valor_funcion, 6),
            "f'(x)": round(valor_derivada, 6),
            "x_siguiente": round(siguiente_valor, 6)
        })

        valor_actual = siguiente_valor

    return valor_actual, tabla_iteraciones
