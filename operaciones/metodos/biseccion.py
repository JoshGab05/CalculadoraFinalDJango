def metodo_biseccion(funcion, limite_inferior, limite_superior, cantidad_iteraciones):
    tabla_iteraciones = []
    for numero_iteracion in range(1, cantidad_iteraciones + 1):
        punto_medio = (limite_inferior + limite_superior) / 2
        valor_funcion_medio = funcion(punto_medio)
        valor_funcion_inferior = funcion(limite_inferior)

        tabla_iteraciones.append({
            "Iteración": numero_iteracion,
            "a": round(limite_inferior, 6),
            "b": round(limite_superior, 6),
            "pm": round(punto_medio, 6),
            "f(pm)": round(valor_funcion_medio, 6)
        })

        if valor_funcion_inferior * valor_funcion_medio < 0:
            limite_superior = punto_medio
        else:
            limite_inferior = punto_medio

    return punto_medio, tabla_iteraciones
